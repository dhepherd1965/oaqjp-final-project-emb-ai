from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import *

app = Flask("emotionDetector")

@app.route('/')
def display_start():
    """show index page"""
    return render_template("index.html")

@app.route('/emotionDetector')
def analysis():
    """Push button and show results"""
    texttoprocess=request.args.get('textToAnalyze')
    result=emotion_detector(texttoprocess)
    output=f"For the given statement, the system response is 'anger' : {result['anger']}, 'disgust' : {result['disgust']}, 'fear' : {result['fear']}, 'joy' : {result['joy']}, 'sadness' : {result['sadness']}. The dominant emotion is {result['dominant_emotion']}"
    return (str(output))

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)