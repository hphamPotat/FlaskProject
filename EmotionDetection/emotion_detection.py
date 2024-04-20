import json
import requests


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    
    emotions = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }
    if response.status_code == 400:
        return emotions

    formatted = json.loads(response.text)
    highest = -1
    val = ''

    for key, value in formatted['emotionPredictions'][0]['emotion'].items():
        emotions[key] = value
        if value > highest:
            highest = value
            val = key

    emotions['dominant_emotion'] = val
    return emotions
