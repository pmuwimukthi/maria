import speech_recognition as sr
import whisper
import os
from ollama import Client
import asyncio
import edge_tts
import pyttsx3

# Initialize the speech recognition components
source = sr.Microphone()
recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = False
recognizer.energy_threshold = 400
base_model_path = os.path.expanduser('~/.cache/whisper/base.en.pt')
base_model = whisper.load_model(base_model_path)


ollama_client = Client()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)

def listen_for_command():
    with source as s:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        with open("command.wav", "wb") as f:
            f.write(audio.get_wav_data())
        results = base_model.transcribe("command.wav")
        #print("You said:", results["text"])
        return results["text"].lower()
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError:
        print("Unable to access the speech recognition service.")
        return None

def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak_sync(text):
    asyncio.run(speak(text))

def initialize_conversation():
    return [{'role': 'system', 'content': '''Act like my girlfriend and be very friendly. 
             You are very supportive and always help me to make my dreams a reality. 
             You are a kind-hearted girl. Your name is Maria. Use simple and short sentences in response. 
             Give the response from your point of view. Keep a natural tone in conversation.
             don't us any emoji in your response.'''}]

def generate_response(messages):
    response = ollama_client.chat(model='llama3.1:latest', messages=messages)
    response_text = response['message']['content']
    speak_sync(response_text)
    return response_text
