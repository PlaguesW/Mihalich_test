from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DeviceCreate(BaseModel):
    device_uid: str
    name: Optional[str] = None


class ScanSessionCreate(BaseModel):
    device_id: int
    scanned_at: datetime
    scanned_to: Optional[datetime] = None
    notes: Optional[str] = None
    # status: Optional[str] = None #* For future maybe


class AccessPointCreate(BaseModel):
    session_id: int
    bssid: str
    essid: str
    channek: int
    encryption: str
    signal_level: int


class StationCreate(BaseModel):
    session_id: int
    mac_adress: str
    signal_level: int
    associated_bssid: Optional[str] = None


class ScanFileCreate(BaseModel):
    session_id: Optional[int] = None
    device_id: Optional[int] = None
    file_path: str
