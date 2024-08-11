import os
import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
import subprocess
import webbrowser

# Initialize recognizer
recognizer = sr.Recognizer()

# API key
api_key = "Your_api_key"

# Configure the generative AI client
genai.configure(api_key=api_key)

# Instantiate the generative model
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

print("pk Assistant is running...")

while True:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for activation phrase 'hello pk'...")

        # Capture the audio for the activation phrase
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            if  "hello pk" in text.lower():
                engine.say("PK is listening..")
                engine.runAndWait()
                print("Activating...")


                print("Listening for command...")

                # Capture the audio for the command
                audio = recognizer.listen(source,timeout=10,phrase_time_limit=10)

                try:
                    # Use Google Web Speech API to recognize the speech
                    prompt = recognizer.recognize_google(audio)
                    print(f"You said: {prompt}")
                except sr.UnknownValueError:
                    print("Sorry, I could not understand the audio")
                    continue
                except sr.RequestError:
                    print("Could not request results from the service")
                    continue

                # Generate content based on the prompt
                response = model.generate_content(f"As a virtual assistant like Google, tell in short about {prompt}")

                # Check the recognized text and perform the corresponding action
                if prompt.lower() == "open calculator":
                    subprocess.Popen(["calc.exe"])
                elif prompt.lower() == "open notepad":
                    subprocess.Popen(["notepad.exe"])
                elif prompt.lower() == "open chrome":
                    subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe"])
                elif prompt.lower() == "open youtube":
                    webbrowser.open_new("https://www.youtube.com/")
                elif "play" in prompt.lower():
                    webbrowser.open_new("https://youtu.be/u2NAuswnTKs?feature=shared")
                else:
                    # Print the generated content
                    print("\n", response.text)

                    # Write the text in a new file "text.md"
                    with open("text.md", "w") as f:
                        f.write(response.text)

                    # Text to speech
                    engine.say(response.text)
                    engine.runAndWait()
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio")
        except sr.RequestError:
            print("Could not request results from the service")
