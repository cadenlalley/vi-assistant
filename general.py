import pyttsx3
import os
import speech_recognition as sr


engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


# TTS Function to Speak the Input Text
def speak(tts_string):
    engine.say(tts_string)
    engine.runAndWait()


# Function to Interpret Voice and Create a String
def interpret_voice():
    interpreter = sr.Recognizer()
    microphone = sr.Microphone(device_index=int(os.getenv("MICROPHONE_INDEX")))

    with microphone as source:
        print("Interpreter: Listening...")
        interpreter.pause_threshold = 0.5
        pre_processed_sentence = interpreter.listen(source)

    try:
        print("Interpreter: Recognizing...")
        sentence = interpreter.recognize_google(
            pre_processed_sentence, language="en-us"
        )
        print(f"Interpreter: You said: {sentence}.")

    except Exception as exception:
        print(exception)
        print("Interpreter: Unable to recognize your input as any text.")
        return ""

    return sentence
