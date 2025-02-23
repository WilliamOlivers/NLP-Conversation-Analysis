import tkinter as tk
import speech_recognition as sr

# Crée une fonction pour effectuer la reconnaissance vocale
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio_data = r.record(source, duration=10)
            result_label.config(text="Traitement...")
            text = r.recognize_google(audio_data, language="fr-FR")
            result_label.config(text="Résultat: " + text)
        except sr.UnknownValueError:
            result_label.config(text="Impossible de reconnaître la voix.")
        except sr.RequestError:
            result_label.config(text="Erreur de connexion à l'API de reconnaissance vocale.")

# Crée une fenêtre Tkinter
window = tk.Tk()
window.title("Reconnaissance Vocale")

# Crée un bouton pour lancer la reconnaissance vocale
start_button = tk.Button(window, text="Démarrer la reconnaissance vocale", command=recognize_speech)
start_button.pack(pady=20)

# Crée une étiquette pour afficher le résultat
result_label = tk.Label(window, text="", wraplength=300)
result_label.pack()

# Exécute la boucle principale de l'interface Tkinter
window.mainloop()
