import openai
import speech_recognition as sr
import pyaudio
from gradio_client import Client
import re
import os
import simpleaudio as sa


#voice recognition
def voice_to_text():
    global says 

    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 400

    def record_audio():
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.8)
            audio = recognizer.listen(source)
        return audio

    def recognize_speech(audio):
        try:
            #says = ""
            text = recognizer.recognize_google(audio)
            says =  text
        except sr.UnknownValueError:
            recognize_speech(audio)
        except sr.RequestError:
            recognize_speech(audio)

        return says

    if __name__ == "__main__":
        audio = record_audio()
        recognize_speech(audio)

    says = recognize_speech(audio)

    if says == "":
        says = "I didn't hear that. Can you please repeat?"
    else:
        says = says

    return says

#file parth conversion
def convert_path(path):

    # Use a regular expression to find all backslashes
    backslash_pattern = r"\\"  # Escape the backslash character in the pattern
    escaped_path = re.sub(backslash_pattern, r"\\\\", path)

    return escaped_path


#text completion
openai.api_type = "open_ai"
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "Whatever"


messages = [{'role': 'system', 'content': f'''act like my girlfriend and be very friendly. 
             she is very suppotive and always help me to make my dreams a reality. 
             she is kind hearted girl. her name is maria.use simple and short sentences in response. give the response in her point of view. keep natural tone in convertion.'''}]

#back and forward convertion 
while True:
    user_input = voice_to_text()
    print(f"you said : {user_input}")
    
    messages.append({'role': 'user', 'content': user_input})
    
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=messages,
        temperature=0.7,
        max_tokens=-1
    )

    # print(response)
    talking = (response.choices[0].message.content)
    print("she said : " , talking)
    
    messages.append({'role': 'assistant', 'content': response.choices[0].message.content})

    #text to speech
    client = Client("http://127.0.0.1:7860/")
    result = client.predict(
    		talking,	# str  in 'Text Prompt' Textbox component
    		"friendly",	# str (Option from: [('default', 'default'), ('whispering', 'whispering'), ('cheerful', 'cheerful'), ('terrified', 'terrified'), ('angry', 'angry'), ('sad', 'sad'), ('friendly', 'friendly')]) in 'Style' Dropdown component
    		"C:\\Users\\pmask\\OneDrive\\Desktop\\temp\\don't_delete\\voice.mp3",	# str (filepath on your computer (or URL) of file) in 'Reference Audio' Audio component
    		"C:\\Users\\pmask\\pinokio\\cache\\GRADIO_TEMP_DIR\\0d8e01ee653df11921987ce0381745cf6b65b639\\speaker1.mp3",	# str (filepath on your computer (or URL) of file) in 'Use Microphone for Reference' Audio component
    		False,	# bool  in 'Use Microphone' Checkbox component
    		True,	# bool  in 'Agree' Checkbox component
    		fn_index=1
    )
    out = result[1]

    original_path = out[0:-11]
    #print(original_path)

    converted_path = convert_path(original_path)
    #print(converted_path)

    os.chdir(converted_path)
    #time.sleep(1)
    #print(os.getcwd())

    wave_obj = sa.WaveObject.from_wave_file("output.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

