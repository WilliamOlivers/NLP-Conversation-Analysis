import tkinter as tk
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Crée une fonction pour effectuer la reconnaissance vocale
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio_data = r.listen(source, timeout=10)  # Enregistre jusqu'à 10 secondes (ajustez au besoin)
            result_label.config(text="Traitement...")

            # Convertit AudioData en AudioSegment
            audio_segment = AudioSegment.from_raw(
                audio_data.get_raw_data(),
                frame_rate=audio_data.sample_rate,
                sample_width=audio_data.sample_width,
                channels=1
            )

            # Utilise split_on_silence pour découper l'audio en segments de parole
            segments = split_on_silence(audio_segment, silence_thresh=-40, min_silence_len=3000)

            recognized_text = ""

            for segment in segments:
                try:
                    # Utilise l'option de décodage explicite
                    text = r.recognize_google(segment, language="fr-FR", show_all=False, key=None)
                    recognized_text += text + " "
                except sr.UnknownValueError:
                    pass

            result_label.config(text="Résultat: " + recognized_text)

        except sr.WaitTimeoutError:
            result_label.config(text="Aucune parole détectée pendant 10 secondes.")
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
