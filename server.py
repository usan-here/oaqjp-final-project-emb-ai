"""
server.py

This Flask application serves an NLP-based Emotion Detection web service.
Users can input text and get detected emotions and the dominant emotion.
"""

import json
from flask import Flask, request, render_template, Response
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the home page of the Emotion Detection web application.
    
    Returns:
        HTML template for the home page.
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Process the text input from the user, detect emotion using the emotion_detector,
    and return the JSON response or error message if input is invalid.
    
    Returns:
        Response: JSON response with emotions and dominant emotion, or
                  plain string for invalid input.
    """
    text_to_analyse = request.args.get('textToAnalyze', '')

    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # dominant_emotion first in JSON
    response_dict = {
        'dominant_emotion': result['dominant_emotion'],
        'anger': result['anger'],
        'disgust': result['disgust'],
        'fear': result['fear'],
        'joy': result['joy'],
        'sadness': result['sadness']
    }

    return Response(json.dumps(response_dict), mimetype='application/json')


if __name__ == '__main__':
    # Run the Flask app on host 0.0.0.0 and port 5000 in debug mode
    app.run(host='0.0.0.0', port=5000, debug=True)
