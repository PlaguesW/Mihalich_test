from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    device_uid = Column(String, unique=True, index=True)
    name = Column(String, nullable=True)

    sessions = relationship("ScanSession", back_populates="device")


class ScanSession(Base):
    __tablename__ = "scan_sessions"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"), nullable=False)
    scanned_at = Column(DateTime)
    scanned_to = Column(DateTime)
    notes = Column(String, nullable=True)
    # status = Column(String, nullable=True) #* For future maybe

    device = relationship("Device", back_populates="sessions")

    access_points = relationship("AccessPoint", back_populates="session")
    stations = relationship("Station", back_populates="session")


class AccessPoint(Base):
    __tablename__ = "access_points"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("scan_sessions.id"), nullable=False)
    bssid = Column(String)
    essid = Column(String)
    channel = Column(Integer)
    encryption = Column(String)
    signal_level = Column(Integer)

    session = relationship("ScanSession", back_populates="access_points")


class Station(Base):
    __tablename__ = "stations"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("scan_sessions.id"), nullable=False)
    mac_address = Column(String)
    signal_level = Column(Integer)
    associated_bssid = Column(String, nullable=True)

    session = relationship("ScanSession", back_populates="stations")


class ScanFile(Base):
    __tablename__ = "scan_files"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("scan_sessions.id"), nullable=True)
    device_id = Column(Integer, ForeignKey("devices.id"), nullable=True)
    file_path = Column(String)
    uploaded_at = Column(DateTime)