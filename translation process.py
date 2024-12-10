from googletrans import Translator

text = " hello how are you doing today and what about tommarow"
translator = Translator()
translation = translator.translate(text,"es")
print("Translation: ",translation.text)
