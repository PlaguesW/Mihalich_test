from fastapi import APIRouter, Depends
from app.auth import get_current_user
from app.models_db import User

router = APIRouter()

@router.get("/secret")
def secret_data(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}!"}