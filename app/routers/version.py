# app/routers/version.py
from fastapi import APIRouter
import os

router = APIRouter(tags=["Version"])

COMMIT_HASH = os.getenv("BUILD_COMMIT", "")

@router.get("/")
def version():
    return {"commit": COMMIT_HASH, "service": "sentiment-api"}
