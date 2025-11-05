import requests
import json

def sentiment_analyzer(text_to_analyse):
    # 1️⃣ Endpoint URL (Skills Network)
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # 2️⃣ Input text to send
    myobj = {"raw_document": {"text": text_to_analyse}}

    # 3️⃣ Header required by the API
    headers = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }

    # 4️⃣ Send POST request
    response = requests.post(url, json=myobj, headers=headers)

    # 5️⃣ Convert response text to JSON
    formatted_response = response.json()

    # 6️⃣ Extract sentiment label and score
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']

    # 7️⃣ Return both values
    return {'label': label, 'score': score}
