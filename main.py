import os
from general import *
from commands import *
from lights import *
from dotenv import load_dotenv


# Load Environment Variables from .env File
load_dotenv()
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME")
NAME = os.getenv("NAME")



speak(
    f"Welcome, {NAME}. I am your personal assistant. I go by the name {ASSISTANT_NAME}."
)

# Clear the Terminal when starting the program
if __name__ == "__main__":
    clear = lambda: os.system("cls")

    # Initiate Main Loop
    while True:
        sentence = interpret_voice().lower()
        if ASSISTANT_NAME.lower() in sentence:
            if "open" in sentence:
                if "open youtube" in sentence:
                    speak(open_youtube())
                else:
                    speak(open_app(sentence))
            elif "date" in sentence:
                speak(get_date())
            elif "wikipedia" in sentence:
                speak(search_wikipedia(sentence))
            elif "google" in sentence:
                speak(search_google(sentence))
            elif "color lights" in sentence:
                speak(switch_group_lights(sentence))
            elif "lights" in sentence:
                speak(switch_all_lights(sentence))

        else:
            None
