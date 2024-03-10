# Import the necessary modules.
import speech_recognition as sr
import pyttsx3
import datetime
import os
import subprocess as sp
import webbrowser

# Initialize the speech recognition engine.
r = sr.Recognizer()

# Initialize the text-to-speech engine.
engine = pyttsx3.init()

# Set the voice of the text-to-speech engine.
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_user():
    hour = datetime.datetime.now().hour

    if (hour >= 4) and (hour < 12):
        speak(f"Good Morning Amit")
    elif (hour >= 12) and (hour < 18):
        speak(f"Good afternoon Amit")
    elif (hour >= 18) and (hour < 21):
        speak(f"Good Evening Amit")
    elif hour in (21, 22, 23, 0, 1, 2, 3):
        speak(f"Good night Amit")
    speak(f"How may I assist you?")


def open_google():
    os.system("Start https://www.google.com")


def open_camera():
    sp.run("start microsoft.windows.camera:", shell=True)


def ds_news():
    webbrowser.open("https://www.kdnuggets.com")
    webbrowser.open(
        "https://www.analyticsvidhya.com/blog/category/guide/?utm_source=blog_navbar&utm_medium=machine_learning_button"
    )
    webbrowser.open("https://www.analyticsvidhya.com/blog/")
    webbrowser.open("https://realpython.com/")
    webbrowser.open("https://engineering.atspotify.com/category/data-science/")
    webbrowser.open("https://blog.duolingo.com/tag/engineering/")
    webbrowser.open("https://netflixtechblog.com/")
    webbrowser.open(
        "https://www.datasciencecentral.com/category/technical-topics/data-science/"
    )
    webbrowser.open(
        "https://www.datasciencecentral.com/category/technical-topics/tools-and-techniques/"
    )
    webbrowser.open("https://www.advancinganalytics.co.uk/blog")


# Define the main function.
def main():
    greet_user()

    # Continuously listen for voice commands.
    i = 0
    while True:
        # Wait for the user to say something.
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        # Try to recognize the user's speech.
        try:
            text = r.recognize_google(audio)
            print("You said: {}".format(text))
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            i += 1
            if i > 4:
                break
            continue
        except sr.RequestError:
            print("Sorry, there was a problem with the speech recognition service.")
            continue

        # Process the user's speech.
        if text.lower() == "hello":
            speak("Hello there!")
        elif text.lower() == "what time is it":
            now = datetime.datetime.now()
            time = now.strftime("%H:%M")
            speak("The time is {}".format(time))
        elif text.lower() == "open google":
            open_google()
        elif text.lower() == "open camera":
            open_camera()
        elif text.lower() == "data news":
            ds_news()
        elif text.lower() == "exit" or text.lower() == "quit":
            break


# Run the main function.
if __name__ == "__main__":
    main()
