import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse.strip():
        # Blank input: return None for dominant_emotion
        return {
            'dominant_emotion': None,
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 400:
        # API failed
        return {
            'dominant_emotion': None,
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None
        }

    data = response.json()
    emotions = data['emotionPredictions'][0]['emotion']

    # Determine dominant emotion
    dominant = max(emotions, key=emotions.get)

    return {
        'dominant_emotion': dominant,  # first key
        'anger': emotions.get('anger'),
        'disgust': emotions.get('disgust'),
        'fear': emotions.get('fear'),
        'joy': emotions.get('joy'),
        'sadness': emotions.get('sadness')
    }
