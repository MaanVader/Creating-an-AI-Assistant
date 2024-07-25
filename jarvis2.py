# /path/to/your/jarvis.py

import speech_recognition as sr
import pyttsx3
from interpreter import interpreter

# Configure the Open Interpreter
interpreter.offline = True  # Disables online features like Open Procedures
interpreter.llm.model = "openai/x"  # Tells OI to send messages in OpenAI's format
interpreter.llm.api_key = "fake_key"  # LiteLLM, which we use to talk to LM Studio, requires this
interpreter.llm.api_base = "http://localhost:1234/v1"  # Point this at any OpenAI compatible server

def listen_for_jarvis():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    engine = pyttsx3.init()

    with microphone as source:
        while True:
            print("Listening for 'Jarvis'...")
            audio = recognizer.listen(source)

            try:
                speech = recognizer.recognize_google(audio).lower()
                if 'jarvis' in speech:
                    # Process the command using Open Interpreter
                    response = interpreter.chat(speech.replace('jarvis', '').strip())
                    print(f"Jarvis: {response.content}")

                    # Using the text-to-speech engine to speak out the response
                    engine.say(response)
                    engine.runAndWait()

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError:
                print("Request failed")

if __name__ == "__main__":
    listen_for_jarvis()
