"""Docstrings
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector')
def emotion_analyze():
    """
    Calls API to analyze emotions from text
    """
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyze)
    if not res['dominant_emotion']:
        return 'Invalid text! Please try again!'
    return_str = 'For the given statement, the system response is '
    for key, value in res.items():
        if key == 'dominant_emotion':
            return_str += f" The dominant emotion is {value}."
        else:
            return_str += f" \'{key}\': {value}, "
    return return_str


@app.route("/")
def index():
    """Renders index page"""
    return render_template('index.html')


if __name__ == '__main__':
    """Main function goes here"""
    app.run()
