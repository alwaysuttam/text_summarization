# Text Summarization and Text-to-Speech Web Application

This web application allows users to input text and receive an extractive summary of the text along with an audio version of the summary. The application uses Flask for the web framework, `gTTS` for text-to-speech conversion, and a custom extractive summarization function.

## Project Structure

- `app.py`: The main Flask application script.
- `text_sum.py`: Contains the `extractive_summarization` function for summarizing text.
- `templates/`: Directory containing HTML templates for the web pages.
  - `index.html`: The main page where users can input text for summarization.
- `static/`: Directory where generated audio files are saved.
- `screeshots/`: Directory where capture the window after execution of the program.

## Setup Instructions

### Prerequisites

- Python 
- Flask
- `gTTS` (Google Text-to-Speech)
- Necessary NLP libraries for the summarization function (assumed to be in `text_sum.py`)

### Installation

1. Clone the Repository:
  
   git clone https://github.com/uttam-bn/text_summarization.git
   cd text-summarization-tts

2. Install the Required Packages    

3. Set Up Google API Credentials

### Running the Application

1. Run the Flask Application:
    python server.py

2 . Open Your Web Browser:
    Go to http://127.0.0.1:5000/ to access the application.

### Screenshots of the application