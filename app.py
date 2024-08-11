from flask import Flask, render_template, request, jsonify
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

app = Flask(__name__)

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Your existing functions (speak, wishMe, takeCommand, sendEmail) go here
# ...

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_voice', methods=['POST'])
def process_voice():
    query = request.json['voice_input'].lower()
    response = ""

    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        response = f"According to Wikipedia: {results}"
        speak(response)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        response = "Opening YouTube"

    # Add more elif conditions for other commands...

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)