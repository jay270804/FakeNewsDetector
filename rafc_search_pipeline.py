import faiss
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from brave_articles import brave_search
import json
import pandas as pd
from openai import OpenAI
import os
import constants
from GPT_model import parse_openai_response

load_dotenv()
openai = OpenAI()
api_key = os.getenv("OPENAI_API_KEY")

class RAFCHybrid:
    def __init__(self):
        self.local_index = faiss.read_index("data/local_real_claims.index")
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        self.true_claims = pd.read_csv("data/Real_df_for_RAFC.csv")

    def retrieve(self, claim, threshold=0.3):
        # Local FAISS search
        claim_embed = self.model.encode([claim])
        D, I = self.local_index.search(claim_embed, k=3)
        distance = D[0][0]
        index = I[0].tolist()
        if distance < threshold:  # Good local match
            confidence = max(0, 1 - (distance / threshold))  # Clamped to 0-1

        # Step 4: Get matched claim text (optional)
        try:
            matched_claim = self.true_claims.iloc[index]['title']
        except:
            matched_claim = "Claim not found"
            return {
                "veracity": "True",
                "confidence": round(float(confidence), 2),
                "reason": f"Matched a verified claim in local database: '{matched_claim}' (confidence: {confidence:.2f})"
            }
        else:
            # Brave API
            news_articles = brave_search(claim)
            fetched_input = ""
            news_urls = []
            for article in news_articles:
                fetched_input+=f"Title: {article['title']}\n"
                fetched_input+=f"Description: {article['text']}\n"
                news_urls.append(article['url'])

            response = openai.chat.completions.create(
                model=constants.MODEL_NAME,
                messages=[
                    {"role":"system","content":constants.SYSTEM_PROMPT_RAFC},
                    {"role":"user","content":f"claims:{fetched_input}"}
                ]
            )
            openai_RAFC_response = parse_openai_response(response_text=response.choices[0].message.content)
            # TODO: call the openai api for return response as {"veracity","confidence", "reason"}
            # Basically use the verify_claim method here only.
            if openai_RAFC_response['veracity'] == constants.TRUE:
                self.add_to_index(claim=claim)
            return {
                "veracity": openai_RAFC_response['veracity'],
                "confidence": openai_RAFC_response['confidence'],
                "reason": openai_RAFC_response['reason'],
                "url": news_urls
            }

    def add_to_index(self, claim:str):
        # Update FAISS index with new verified claim
        new_embed = self.model.encode([claim])
        self.local_index.add(new_embed)

        # Add to DataFrame
        new_row = {
            'source': "EVIDENCE_VERIFIED",
            'title': claim,
            'label': "TRUE"
        }
        self.true_claims.loc[len(self.true_claims)] = new_row
        self.true_claims.to_csv('data/Real_df_for_RAFC.csv')

    # Add to DataFrame
        faiss.write_index(self.local_index, "data/local_real_claims.index")
        # (Optional: Store metadata in SQLite/JSON)

#         return verdict
claim = "Ukraine says Russian drone attack hits Chernobyl"
retriever = RAFCHybrid()
evidence = retriever.retrieve(claim)
print(evidence)