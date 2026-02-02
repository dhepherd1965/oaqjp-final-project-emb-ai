import requests
import json

def emotion_detector(text_to_analyse):
    """function for emotion detection"""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=30)
    reply=json.loads(response.text)
    emotions=['anger','disgust','fear','joy','sadness']
    final_reply={}
    for temp in emotions:
        final_reply[temp]=reply['emotionPredictions'][0]['emotion'][temp]
    final_reply['dominant_emotion']=sorted(final_reply,key=final_reply.get, reverse=True)[0]
    return final_reply