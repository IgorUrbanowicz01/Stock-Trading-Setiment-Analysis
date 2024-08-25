import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

def finbert_analysis(text):
    MODEL = "ProsusAI/finbert"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)

    tokenized_text = tokenizer('EU gives generous taxbreaks to Apple', return_tensors="pt", )
    with torch.no_grad():
        logits = model(**tokenized_text).logits
    scores = logits[0].detach().numpy()
    scores = scores.squeeze()
    scores = softmax(scores)
    score_dict = {
        'neg_score': scores[0],
        'neu_score': scores[1],
        'pos_score': scores[2]
    }
    return score_dict
