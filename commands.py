import webbrowser
import datetime
import wikipedia
import wolframalpha
from AppOpener import open


def clean_command(unsanitized_string, keywords):
    command = unsanitized_string.replace("assistant", "")
    for word in keywords:
        command = command.replace(word, "")
        command = command.strip()
    return command


def error_string(application):
    return (
        f"Cannot find the {application} executable. Check your path in the .env file."
    )


def open_youtube():
    webbrowser.open("www.youtube.com")
    return "Opening YouTube."


def get_date():
    return datetime.datetime.now().strftime("%m/%d/%Y, %I:%M %p")


def search_wikipedia(command):
    command.replace("wikipedia", "")
    results = wikipedia.summary(command, sentences=3)
    return f"According to Wikipedia, {results}."


def search_google(command):
    command = clean_command(command, ["google"])
    webbrowser.open(f"www.google.com/search?q={command}")
    return f"Searching Google for {command}."


def open_app(command):
    command = clean_command(command, ["open"])
    open(command)
    return f"Attempting to open{command}."


def calculate(command):
    client = wolframalpha.Client("Wolframalpha api id")
    command = clean_command(command, ["calculate"])
    response = client.query(" ".join(command))
    return next(response.results).text
