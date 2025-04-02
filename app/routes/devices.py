from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register_devices(data: dict):
    # Create rec into DB
    return {"status": "registered", "device_uid": "abc"}