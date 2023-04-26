import os
from general import *
from commands import *
from dotenv import load_dotenv

# Load Environment Variables from .env File
load_dotenv()
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME")
USER_NAME = os.getenv("USER_NAME")

"""
speak(
    f"Welcome, {USER_NAME}. I am your personal assistant. I go by the name {ASSISTANT_NAME}."
)
"""

# Clear the Terminal when starting the program
if __name__ == "__main__":
    clear = lambda: os.system("cls")

    # Initiate Main Loop
    while True:
        sentence = interpret_voice().lower()

        if ASSISTANT_NAME.lower() in sentence:
            if "open" in sentence:
                if "open discord" in sentence:
                    speak(open_discord(os.getenv("DISCORD_PATH")))
                elif "open dota 2" in sentence:
                    speak(open_dota(os.getenv("DOTA_PATH")))
                elif "open youtube" in sentence:
                    speak(open_youtube(sentence))
            elif "date" in sentence:
                speak(get_date())
            elif "wikipedia" in sentence:
                speak(search_wikipedia(sentence))
            elif "google" in sentence:
                speak(search_google(sentence))
            elif "calculate" in sentence:
                speak(calculate(sentence))

        else:
            None
