import tkinter as tk
import speech_recognition as sr
from gtts import gTTS
import playsound
import os

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            display_text(text)
            respond(text)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            display_text("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

def respond(text):
    # Here, you would send 'text' to your API and get a response
    response = "This is a sample response."
    display_response(response)
    speak(response)

def display_text(text):
    text_area.insert(tk.END, f"You: {text}\n")

def display_response(response):
    text_area.insert(tk.END, f"Zelda: {response}\n")

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    playsound.playsound("response.mp3")
    os.remove("response.mp3")

app = tk.Tk()
app.title("Voice Assistant")

text_area = tk.Text(app, wrap='word')
text_area.pack(pady=20, padx=20)

listen_button = tk.Button(app, text="Talk", command=listen)
listen_button.pack(pady=10)

app.mainloop()
