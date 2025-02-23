import speech_recognition as sr

# Création de l'objet de reconnaissance.
r = sr.Recognizer()

with sr.Microphone() as source:
    # lecture de l'audio par le micro par défault
    print("Je vous écoute")
    audio_data = r.record(source, duration=10)
    print("Traitement")
    # conversion voix-text
    text = r.recognize_google(audio_data, language="fr-FR")
    print(text)