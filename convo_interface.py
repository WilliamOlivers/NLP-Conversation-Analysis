import gradio as gr
import cohere

co = cohere.Client("YOUR API KEY")

def chat_summarizer(conversation):
    response = co.summarize(conversation, model = 'summarize-xlarge', length = 'short', extractiveness = 'high', temperature = 0.5)
    summary = response.summary
    return summary

chat_input = gr.Textbox(lines = 10, label = "Conversation")
chat_output = gr.Textbox(label = "Résumer")

chat_interface = gr.Interface(
    fn = chat_summarizer,
    inputs = chat_input,
    outputs = chat_output,
    title = "Condenser l'info",
    description = "Résumer vos conversations pro!"
)

chat_interface.launch()