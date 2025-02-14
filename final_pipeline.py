from BERT_response import analyze_claim_with_BERT
from brave_articles import brave_search
import constants
from openai import OpenAI
from dotenv import load_dotenv
from GPT_model import parse_openai_response

load_dotenv()

openai = OpenAI()

def final_pipeline(claim:str):
    response_BERT = analyze_claim_with_BERT(claim=claim)

    response_EVIDENCE = analyze_claim_with_evidence(claim=claim)
    if not response_EVIDENCE:
        return {"error": "Nonetype object returned during evidence analysis."}

    url = response_EVIDENCE['url']
    veracity = response_EVIDENCE['veracity']
    evidence_confidence = response_EVIDENCE['confidence']
    bert_confidence = response_BERT['confidence']
    reason = response_EVIDENCE['reason']

    credibility = (bert_confidence * constants.WEIGHTAGE_1) + (evidence_confidence * constants.WEIGHTAGE_2)

    return {
        "url":url,
        "veracity":veracity,
        "reason":reason,
        "credibility": credibility
    }

def analyze_claim_with_evidence(claim:str):
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
            {"role":"user","content":f"claim by user:{claim}\nevidence for you to take reference:{fetched_input}"}
        ]
    )
    openai_RAFC_response = parse_openai_response(response_text=response.choices[0].message.content)
    # TODO: call the openai api for return response as {"veracity","confidence", "reason"}
    return {
        "veracity": openai_RAFC_response['veracity'],
        "confidence": openai_RAFC_response['confidence'],
        "reason": openai_RAFC_response['reason'],
        "url": news_urls
    }

response = final_pipeline(claim="infosys layoffs 1000 in mysuru")
print(response)