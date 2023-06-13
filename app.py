from flask import Flask, request, render_template, jsonify
import os
import speech_recognition as sr
import subprocess
import openai
import re

# Load OpenAI API key
openai.api_key = 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file'}), 400

    audio = request.files['audio']

    # Save the uploaded audio file
    audio.save('temp.wav')

    # Convert the audio file to wav using ffmpeg
    subprocess.run(['C:\\ffmpeg\\bin\\ffmpeg', '-i', 'temp.wav', 'converted.wav'])

    # Read the audio file
    recognizer = sr.Recognizer()
    with sr.AudioFile('converted.wav') as source:
        audio_data = recognizer.record(source)
        text_content = recognizer.recognize_google(audio_data)

    # Generate response using OpenAI
    desired_word_count = 220  # Specify the desired word count here
    response = generate_response(text_content, desired_word_count)

    return jsonify({'transcript': text_content, 'response': response})

def generate_response(prompt, desired_word_count):
    total_words = 0
    generated_chunks = []

    while total_words < desired_word_count:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=desired_word_count * 5,  # Set a higher value to allow for trimming
            temperature=0.7,
            n=1,
            stop=None
        )
        generated_text = response.choices[0].text.strip()
        generated_chunks.append(generated_text)

        # Update the total word count
        total_words += len(re.findall(r'\w+', generated_text))

    # Concatenate the generated chunks
    generated_text = ' '.join(generated_chunks)

    # Trim the concatenated response to the desired word count while preserving sentence boundaries
    generated_text = trim_to_word_count(generated_text, desired_word_count)

    return generated_text


def trim_to_word_count(text, desired_word_count):
    words = text.split()
    trimmed_text = ''

    for word in words:
        if len(trimmed_text.split()) < desired_word_count or word[-1] in '.!?':
            trimmed_text += ' ' + word
        else:
            break

    return trimmed_text.strip()

def split_text_into_chunks(text, desired_word_count):
    words = text.split()
    chunks = []
    current_chunk = ''
    
    for word in words:
        if len(current_chunk) + len(word) < desired_word_count:
            current_chunk += ' ' + word
        else:
            chunks.append(current_chunk.strip())
            current_chunk = word
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

if __name__ == "__main__":
    app.run(debug=True)

