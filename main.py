import pyttsx3

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)
