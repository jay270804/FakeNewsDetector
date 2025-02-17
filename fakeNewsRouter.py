from http import HTTPStatus
# import constants
from fastapi.responses import JSONResponse
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from getVerifiedFakeNewsRepository import get_verified_news_data, store_fake_news_data
from schemas import VerifiedFakeNewsResponse, NewsRequest, NewsDetectionResponse
from final_pipeline import final_pipeline
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",  # Your frontend URL
    "http://localhost:5173/search",  # Your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/me")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    try:
        # Try to execute a simple query
        db.execute("SELECT 1")
        return {"status": "Database connection successful"}
    except Exception as e:
        return {"status": "Database connection failed", "error": str(e)}

@app.get("/get-verified-fake-news", response_model=list[VerifiedFakeNewsResponse], status_code=HTTPStatus.OK)
def get_verified_fake_news(db: Session = Depends(get_db)):
    verified_news = get_verified_news_data(db=db)
    if not verified_news:
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={"detail": "No Data Found In DB"}
        )
    return verified_news

@app.post("/predict-fake-news", response_model=NewsDetectionResponse, status_code=HTTPStatus.OK)
def detect_fake_news(req: NewsRequest, db: Session = Depends(get_db)):
    text = req.text.strip()
    if not text:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="News text cannot be empty")

    try:
        response = final_pipeline(text)
        # return
        # print("Before veracity check")
        # if response['veracity'] == constants.FALSE:
        #     print("inside vercity check")
        #     store_fake_news_data(db=db,news_title=text, confidence=response['credibility'])
        return NewsDetectionResponse(
            veracity=response['veracity'],
            credibility=response['credibility'],
            reason=response['reason'],
            sources=response['url']
        )
    except TypeError:
        raise HTTPException(status_code=HTTPStatus.BAD_GATEWAY, detail="Please retry, check your internet connection")