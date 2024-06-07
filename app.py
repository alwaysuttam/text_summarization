from flask import Flask, request, jsonify, render_template, send_from_directory
from text_sum import extractive_summarization
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def handle_summarization_request():
    request_data = request.get_json()

    if 'text' not in request_data:
        return jsonify({'error': 'Missing required field "text"'}), 400

    text = request_data['text']
    num_sentences = int(request_data.get('num_sentences', 3))

    summary = extractive_summarization(text, num_sentences)

    static_dir = 'static'
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)

    tts = gTTS(summary)
    audio_path = os.path.join(static_dir, 'summary.mp3')
    tts.save(audio_path)

    return jsonify({'summary': summary, 'audio_url': '/static/summary.mp3'})

@app.route('/static/<path:filename>')
def download_file(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
