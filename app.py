import gradio as gr
import dotenv
from transformers import pipeline
from langchain import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import requests
import os

dotenv.load_dotenv()

HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# image to text
def imgToText(url):
    img_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = img_to_text(url)[0]['generated_text']
    return text

# LLM
def generate_story(scenario):
    template = """
               You are a story teller.
               You can generate a short story based on a simple narrative, the story should be no more than 40 words:

               CONTEXT: {scenario}
               STORY:
            """
    prompt = PromptTemplate(template=template, input_variables=["scenario"])
    story_llm = LLMChain(llm=OpenAI(model_name="gpt-3.5-turbo"), prompt=prompt, verbose=True)
    story = story_llm.predict(scenario=scenario)
    return story

def textToSpeech(story):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": "Bearer " + HUGGINGFACEHUB_API_TOKEN}
    payload = {"inputs": story}
    response = requests.post(API_URL, headers=headers, json=payload)
    with open("story.flac", "wb") as f:
        f.write(response.content)

def generate_story_and_play_audio(image):
    scenario = imgToText(image.name)
    story = generate_story(scenario)
    textToSpeech(story)
    return "story.flac"

iface = gr.Interface(
    fn=generate_story_and_play_audio,
    inputs=gr.inputs.File(label="Upload an image"),
    outputs=gr.outputs.Audio(label="Generated Story", type="filepath")
)

iface.launch()
