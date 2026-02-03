from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import *

app = Flask("emotionDetector")

@app.route('/')

def display_start():
    return render_template("index.html")

@app.route('/emotionDetector/<string:textToAnalyze>',methods=['GET','POST'])
def runanalysus(textToAnalyze):
    texttoprocess=request.form['textToAnalyze']
    result=emotion_detector(texttoprocess)


if __name__ == "__main__":    app.run(debug=True)