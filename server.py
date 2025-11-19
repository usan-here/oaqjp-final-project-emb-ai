from flask import Flask, request, render_template, Response
import json
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    # Get input text
    if request.method == 'POST':
        text_to_analyse = request.form.get('text', '')
    else:
        text_to_analyse = request.args.get('textToAnalyze', '')

    # Call the emotion detector
    result = emotion_detector(text_to_analyse)

    # Build dictionary with dominant_emotion first
    response_dict = {
        "dominant_emotion": result['dominant_emotion'],
        "anger": result['anger'],
        "disgust": result['disgust'],
        "fear": result['fear'],
        "joy": result['joy'],
        "sadness": result['sadness']
    }

    # Use json.dumps to preserve key order
    return Response(json.dumps(response_dict), mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
