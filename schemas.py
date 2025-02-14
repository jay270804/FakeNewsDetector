from pydantic import BaseModel
from typing import List

# Response for GET request
class VerifiedFakeNewsResponse(BaseModel):
    news_id: int
    news_title: str
    credibility: float

# Request for POST (news text input)
class NewsRequest(BaseModel):
    text: str

# Response for POST (detection results)
class NewsDetectionResponse(BaseModel):
    veracity: str
    credibility: float
    reason: str
    sources: List[str]