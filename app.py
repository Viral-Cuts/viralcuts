from langchain.document_loaders import YoutubeLoader
import os
from dotenv import load_dotenv
from langchain import OpenAI
import streamlit as st

load_dotenv()

llm = OpenAI(temperature=0, streaming=True,
             openai_api_key=os.getenv("OPENAI_API_KEY"))


loader = YoutubeLoader.from_youtube_url(
    "https://www.youtube.com/watch?v=QRy4JJNTAiA", add_video_info=True
)

document = loader.load()

# print loader results
print(document)
