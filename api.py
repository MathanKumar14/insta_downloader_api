from fastapi import FastAPI
from pydantic import BaseModel
from myapp import MyApp


app = FastAPI()


@app.post("/video_url/")
async def process_url(url: str):
    obj = MyApp(url)
    link = obj.get_link()
    
    return {"media_url": link}

