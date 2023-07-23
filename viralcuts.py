# cd /var/www/datawb.com/public_html
# pm2 start viralcuts.py --name viralcuts-app --interpreter python3
# pm2 save
# pm2 restart viralcuts-app

from fastapi import FastAPI, Form
from langchain.document_loaders import YoutubeLoader
import os
from dotenv import load_dotenv
from langchain import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


load_dotenv()

app = FastAPI()


@app.post("/generate")
def generate(
    video: str = Form(...),
):
    
    loader = YoutubeLoader.from_youtube_url(
        video, add_video_info=True
    )
    document = loader.load()

    page_content = document[0].page_content

    # transcript = document.page_content
    # print(document)

    data = {"transcript": page_content}

    
    llm = OpenAI(temperature=0, streaming=True, openai_api_key=os.environ.get("OPENAI_API_KEY"))

    prompt = PromptTemplate(
    template = """You are an expert video script writer / editor. 

    The client has provided you with the raw transcript he needs broken down into 5 short clips.
    Here is the transcript: {transcript}

    Read through the transcript and pull out 5 EXACT section unedited that fit the clients requirements:
    - between 100-150 words each
    - have high viral potential

    If there is not enough text in the transcript to get 5 then stop.""",

    input_variables = ["transcript"]
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    # print()

    results = chain.run(data)

    return results


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5070)
