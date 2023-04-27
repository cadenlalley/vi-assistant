# Import Modules
import webbrowser
import datetime
import wikipedia
from AppOpener import open
from dotenv import load_dotenv
import os

# Load Environment Variables
load_dotenv()
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME")


"""Clean input string by removing keywords and leading & trailing spaces.
:param unsanitized_string: string to be cleaned of spaces and keywords.
:param keywords: list of keyword strings that you wish to be removed from the unsanitzed_string.
:returns: sanitized string.
"""
def clean_command(unsanitized_string, keywords):
    command = unsanitized_string.replace(ASSISTANT_NAME.lower(), "")
    for word in keywords:
        command = command.replace(word, "")
        command = command.strip()
    return command


"""Opens YouTube in the OS's default browser.
:returns: string to be spoken by the TTS engine.
"""
def open_youtube():
    webbrowser.open("www.youtube.com")
    return "Opening YouTube."


"""Gets the OS's time in Date-Time format.
:returns: string to be spoken by the TTS engine.
"""
def get_date():
    return datetime.datetime.now().strftime("%m/%d/%Y, %I:%M %p")


"""Uses the Wikipedia Library to get information on a specified topic. Summarized to three sentences.
:param command: command given by the voice recognizing engine.
:returns: string to be spoken by the TTS engine.
"""
def search_wikipedia(command):
    command = clean_command(command, ["wikipedia"])
    results = wikipedia.summary(command, sentences=3)
    return f"According to Wikipedia, {results}."


"""Searches Google for specified topic in your OS's default webbrowser.
:param command: command given by the voice recognizing engine.
:returns: string to be spoken by the TTS engine.
"""
def search_google(command):
    command = clean_command(command, ["google"])
    webbrowser.open(f"www.google.com/search?q={command}")
    return f"Searching Google for {command}."


"""Opens application specified by command given in the voice recognition engine.
:param command: command given by the voice recognizing engine.
:returns: string to be spoken by the TTS engine.
"""
def open_app(command):
    command = clean_command(command, ["open"])
    open(command)
    return f"Attempting to open{command}."


