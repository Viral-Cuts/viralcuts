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
    # print(document)

    data = {"video": video, "document": document}

    
    llm = OpenAI(temperature=0, streaming=True, openai_api_key=os.environ.get("OPENAI_API_KEY"))

    prompt = PromptTemplate(
    template = """You are the worlds short video expert.

    Analyze the youtube video transcript: {transcript}

    Find a snippet from the video transcript with high viral potential as a short, then critique it for how viral the resulting short clip will be, then and rank them out of 10. If the score is not 10, repeat the process until a snippet worthy of a score of 10 is generated.?""",

    input_variables = ["transcript"]
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    # print()

    results = chain.run(data)

    return results


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5070)
