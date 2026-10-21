
from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI(title="YouTube Comments Sentiment API")


def sentiment(score):
    if score > 0.3:
        return "Positive"
    elif score < -0.3:
        return "Negative"
    else:
        return "Neutral"


class CommentInput(BaseModel):
    comment: str


@app.get("/")
def home():
    return {"message": "YouTube Sentiment API is running!"}


@app.post("/analyze")
def analyze_comment(data: CommentInput):
    polarity = TextBlob(data.comment).sentiment.polarity

    return {
        "comment": data.comment,
        "polarity": polarity,
        "sentiment": sentiment(polarity)
    }
