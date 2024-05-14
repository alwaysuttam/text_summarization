# app.py

from flask import Flask, request, jsonify , render_template
from text_sum import hybrid_summarization

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def handle_summarization_request():
    # Get input data from request
    request_data = request.get_json()

    # Check if 'text' field exists in request data
    if 'text' not in request_data:
        return jsonify({'error': 'Missing required field "text"'}), 400

    # Extract text and num_sentences from request data
    text = request_data['text']
    num_sentences = int(request_data.get('num_sentences', 3))  # Default to 3 sentences

    # Summarize the text
    summary = hybrid_summarization(text, num_sentences)

    # Return the summary as JSON response
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
