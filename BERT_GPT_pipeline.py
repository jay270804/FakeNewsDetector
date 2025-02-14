from GPT_model import parse_openai_response, cached_analyze_claim_with_openai
from BERT_response import analyze_claim_with_BERT

def validate_claim(claim):
    # Analyze the claim with OpenAI

    openai_response = cached_analyze_claim_with_openai(claim)
    openai_data = parse_openai_response(openai_response)
    bert_data = analyze_claim_with_BERT(claim)

    if openai_data:
        # Compare OpenAI's veracity with DistilBERT's prediction
        openai_veracity = openai_data.get("veracity")
        confidence = openai_data.get("confidence")
        reason = openai_data.get("reason")

        if openai_veracity == "True" and bert_data.get("veracity") == "True":
            print("Consistent: Both models agree the claim is true.")
        elif openai_veracity == "False" and bert_data.get("veracity") == "False":
            print("Consistent: Both models agree the claim is false.")
        else:
            print("Inconsistent: Models disagree.")
            print(f"OpenAI Reason: GPT-4o-mini predicts the claim is {openai_veracity} with {confidence}% confidence.\n-> {reason}")
            print(f"BERT Reason: {bert_data.get("reason")}")
    else:
        print("Failed to parse OpenAI response.")

# validate_claim("PM Modi offers Pinaka rocket systems to France")
# validate_claim("Tonight in Ohio, more people came out to vote for Barack Obama in an unopposed race than voted for (Mitt) Romney and (Rick) Santorum combined.")