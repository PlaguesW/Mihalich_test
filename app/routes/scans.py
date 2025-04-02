from fastapi import APIRouter
from typing import List
from .rabbitmq import publish_message
from ..models import ScanSessionCreate, AccessPointCreate, StationCreate

router = APIRouter()

@router.post("/", summary="Create a new scan session")
def create_scan_session(payload: ScanSessionCreate):
    session_id = 123  # Return ID from DB
    publish_message(f"New ScanSession created with id={session_id}")
    return {"status": "created", "session_id": session_id}

@router.post("/{session_id}/access-points", summary="Add access points to a session")
def add_access_points(session_id: int, aps: List[AccessPointCreate]):
    # СSave list into DB
    return {"status": "added", "count": len(aps)}

@router.post("/{session_id}/stations", summary="Add stations to a session")
def add_stations(session_id: int, stations: List[StationCreate]):
    # Save station into DB
    return {"status": "added", "count": len(stations)}