from transformers import AutoModelForSequenceClassification, AutoTokenizer
# from title_tokenizer import tokenize_data
import torch


model_path = "./saved_model"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
label_map = {1: "True", 0: "False"}

def analyze_claim_with_BERT(claim:str):

    inputs = tokenizer(
        claim,
        padding=True,  # Add [PAD] tokens when sequences are too long
        truncation=True,  # Truncate sequences that exceed max length
        max_length=128,  # Set maximum sequence length
        return_tensors='pt'  # Return tensors in PyTorch format
    )

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    inputs = {key: val.to(device) for key, val in inputs.items()}

    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    probabilites = torch.softmax(logits, dim=-1)

    predicted_label_index = torch.argmax(probabilites, dim=-1).item()
    predicted_label = label_map[predicted_label_index]
    confidence_score = probabilites[0][predicted_label_index].item()
    confidence_score = round(confidence_score, 2)
    return {
        "veracity": predicted_label,
        "confidence": confidence_score,
        "reason": f"The model predicts the claim is {predicted_label} with {confidence_score}% confidence."
    }

# response = analyze_claim_with_BERT(claim="Wisconsin is on pace to double the number of layoffs this year.")
# response = analyze_claim_with_BERT(claim="Bellamy Young Opens Up About Being Adopted, Her Real First Name and How She Almost Missed Out on Scandal")
response = analyze_claim_with_BERT(claim="Taylor Swift announced a new album yesterday")
print(response)
