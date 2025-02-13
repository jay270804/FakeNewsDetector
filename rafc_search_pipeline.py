import faiss
from sentence_transformers import SentenceTransformer
from brave_articles import brave_search
import json
import pandas as pd

class RAFCHybrid:
    def __init__(self):
        self.local_index = faiss.read_index("data/local_real_claims.index")
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        self.true_claims = pd.read_csv("data/Real_df_for_RAFC.csv")

    def retrieve(self, claim, threshold=0.3):
        # Local FAISS search
        claim_embed = self.model.encode([claim])
        D, I = self.local_index.search(claim_embed, k=1)
        distance = D[0][0]
        if distance < threshold:  # Good local match
            confidence = max(0, 1 - (distance / threshold))  # Clamped to 0-1

        # Step 4: Get matched claim text (optional)
            matched_claim = self.true_claims[I[0][0]] or "Not found in local db"

            return {
                "veracity": "True",
                "confidence": round(float(confidence), 2),
                "reason": f"Matched a verified claim in local database: '{matched_claim}' (confidence: {confidence:.2f})"
            }
        else:
            # Brave API
            news_articles = brave_search(claim)
            # TODO: call the openai api for return response as {"veracity","confidence", "reason"}
            # Basically use the verify_claim method here only.
            return {
                "veracity": "openai_response_here",
                "confidence": "openai_confidence_here",
                "reason": "openai_reason_here"
            }

    def add_to_index(self, claim):
        # Update FAISS index with new verified claim
        new_embed = self.model.encode([claim])
        self.local_index.add(new_embed)
        # TODO: If you save the claim to index, then save it to local dataframe as well for retreiving matched_claim.
        faiss.write_index(self.local_index, "data/local_real_claims.index")
        # (Optional: Store metadata in SQLite/JSON)

def verify_claim(claim):
    # 1. Retrieve evidence
    retriever = RAFCHybrid()
    evidence = retriever.retrieve(claim)

    # 2. Local match found
    if evidence['source'] == "local":
        return {"verdict": "Local DB Match", "confidence": 0.95}

    # 3. Web evidence + OpenAI verification
    else:
        # Extract key snippets from scraped articles
        snippets = " ".join([a['text'][:500] for a in evidence['results']])

        # Send to OpenAI for verification
        from openai import OpenAI
        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{
                "role": "user",
                "content": f"Claim: {claim}\nEvidence: {snippets}\nIs this true? Respond with JSON: {{'verdict': 'true/false', 'confidence': 0-1}}"
            }]
        )

        # Cache verified claim
        verdict = json.loads(response.choices[0].message.content)
        # Only add if the news is real
        retriever.add_to_index(claim, verdict)

        return verdict

