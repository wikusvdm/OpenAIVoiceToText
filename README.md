# OpenAIVoiceToText

This program takes a spoken prompt, converts it into a string, sends it to OpenAI, and ultimately displays the response from an OpenAI engine. It's a fascinating application that demonstrates a full-stack solution potentially useful in customer service support scenarios, tailoring AI responses to specific queries. 

A challenge that one might encounter with OpenAI is the management of text output. If you don't limit the text count, 

OpenAI can yield large chunks of text. To mitigate this, I've throttled my word count to 220 words, resulting in a reasonably-sized response. OpenAI operates under a 4097 token limit (which could change over time), preventing the submission of overly lengthy responses. 

This is because not only does your prompt contribute to these tokens, but OpenAI also includes its own response when calculating the total token limit. 

Roughly speaking, a 300-word paragraph can amount to as many as 400 tokens, with each word and character counting as a token. 

This depends on how accurately you want the AI to interpret your text. Another challenge lies in smart prompting: simply providing a clear code pattern to OpenAI isn't sufficient; you also need to incorporate principles of prompt engineering to save time.

 If OpenAI gets confused based on the code hints you provide, it may not return the desired output, even if the code is clean. 

One workaround I've discovered is to use savvy prompt engineering, which involves instructing OpenAI explicitly on what you want it to do, and customizing the program to adjust the output given by OpenAI.

Here's a rough breakdown:

First, I run app.py from the directory folder. In this case, it's one found in downloads.
Next, I head over to the port given in the terminal.
Thereafter, I click on the button to record and go ahead.
After this, I go with "Y" in the terminal area such that the conversation can take place back to text.
Lastly, I'll witness an output of both my initial prompt and, of course, openai's response.
This code - as with every other developer's arsenal - is only in the beginning phases. It could be adjusted for a better aesthetic, but I wanted to stress my skill for implementing the task: converting speech to a string of text, sending it to openai, and getting a response back.

Feel free to watch my video on how it is used (As uploaded on my YouTube Channel): https://drive.google.com/file/d/1HvsNXBqRz7spkVP0lMcGTyAPFuCItroe/view?usp=share_link

Here is a detailed breakdown:

First, necessary libraries and modules are imported. This includes Flask (a lightweight web framework for Python), request and render_template from flask (to handle HTTP requests and rendering HTML files), jsonify (to convert Python data structures to JSON), os and subprocess (for interacting with the system), speech_recognition (to convert speech to text), openai (to interact with OpenAI's API), and re (for regular expression operations).

Then, OpenAI's API key is set using the openai.api_key attribute.

A new Flask web application is created.

Two routes are set up for the Flask web application:

a. @app.route('/', methods=['GET']): This route is the homepage. It simply renders an 'index.html' file when a GET request is made to the root URL of the application.

b. @app.route('/speech-to-text', methods=['POST']): This route is set to accept POST requests. It handles the conversion of the uploaded audio file to text and then generates a response using OpenAI's language model. If no audio file is provided, it returns an error message.

The speech_to_text() function accepts an audio file, saves it, and converts it to a WAV file using the ffmpeg software (a complete solution to record, convert, and stream audio and video). Then, the function reads the converted audio file and transcribes it to text using Google's Speech Recognition API. Next, it generates a response from OpenAI's language model using the transcribed text and a specified word count, and then returns the transcribed text and the response as a JSON object.

The generate_response() function creates a response using OpenAI's language model. It starts with an initial prompt and continues generating chunks of text until the total word count reaches a desired limit. The function uses the openai.Completion.create() method to generate the text, specifying parameters like the engine to use, the prompt to start with, the maximum number of tokens, the temperature (which affects randomness), and the number of completions to generate.

The trim_to_word_count() function trims the generated text to a desired word count, while preserving sentence boundaries.

The split_text_into_chunks() function splits the text into chunks where each chunk's length is less than or equal to the desired word count.

Finally, if this script is run directly (i.e., not imported as a module in another script), it starts the Flask web application in debug mode using app.run(debug=True). This means the server will automatically reload if code changes are detected and it will provide detailed error messages if something goes wrong.
