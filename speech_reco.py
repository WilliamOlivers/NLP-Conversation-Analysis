import speech_recognition as sr
import cohere

# initialize Cohere client
co = cohere.Client("YOUR API KEY")

def chat_summarizer(conversation):
    response = co.summarize(conversation, model = 'summarize-xlarge', length = 'short', extractiveness = 'high', temperature = 0.5)
    summary = response.summary
    return summary

filename = "audio/Test.wav"

# initialize the recognizer
r = sr.Recognizer()

# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)
    #print(chat_summarizer(text))

