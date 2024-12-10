import speech_recognition as sr
import pyaudio
import keyboard

recognizer = sr.Recognizer()
# set up an reconizerobject which enables methods like listen() , reconize_google()
with sr.Microphone() as source:
# set up an microphone object and handle opening and closing of microphone automatically

    print("plz click 'enter' to Say something:") 
    keyboard.wait('enter')
    print("Recording...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Could not understand audio")


