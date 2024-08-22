import speech_recognition as sr
import os
import pyttsx3
import pywhatkit
import webbrowser
import datetime
import openai
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say("Hello i am Jarvis, welcome to the virtual world")
engine.runAndWait()

def use_openai(prompt):

    openai.api_key = "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"
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="What is the meaning of life?",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response["choices"][0]["text"]
    return text


def talk(text):
    # Split the text into chunks of 200 characters
    chunks = [text[i:i + 200] for i in range(0, len(text), 200)]

    for chunk in chunks:
        engine.say(chunk)
        engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "jarvis" in command:
                command= command.replace("jarvis","")
                print(command)

    except:
        pass
    return command
def run_jarvis():

    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play","")
        talk("playing"+ song)
        pywhatkit.playonyt(song)
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
             ["google", "https://www.google.com"], ]
    for site in sites:
        if f"Open {site[0]}".lower() in command.lower():
            talk(f"Opening {site[0]} ...")
            webbrowser.open(site[1])
    # write a code to tell date and time
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is " + time)
    elif "Using ai".lower() in command.lower():
        ab=use_openai(prompt=command)
        talk(ab)
        print(ab)




while True:
    run_jarvis()
