# cd /var/www/datawb.com/public_html
# pm2 start viralcuts.py --name viralcuts-app --interpreter python3
# pm2 save
# pm2 restart viralcuts-app

from fastapi import FastAPI, Form
from langchain.document_loaders import YoutubeLoader
import os
from dotenv import load_dotenv
from langchain import OpenAI

load_dotenv()

app = FastAPI()


@app.post("/generate")
def generate(
    video: str = Form(...),
):
    # llm = OpenAI(temperature=0, streaming=True, openai_api_key=os.getenv("OPENAI_API_KEY"))
    loader = YoutubeLoader.from_youtube_url(
        video, add_video_info=True
    )
    document = loader.load()
    # print(document)

    data = {"video": video, "document": document}
    return data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5070)
