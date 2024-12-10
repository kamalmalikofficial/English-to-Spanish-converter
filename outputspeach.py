from gtts import gTTS
import os

# Properly encoded text with correct characters
text = "Hola, ¿cómo estás hoy y qué tal mañana?"
tts = gTTS(text=text, lang="es")
tts.save("translation.mp3")
os.system("start translation.mp3")

