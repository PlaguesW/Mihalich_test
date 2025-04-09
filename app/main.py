import uvicorn
from fastapi import FastAPI
import logging

from .routes import devices, scans
from .rabbitmq import rabbit_init
from app.routes import secret_routes


app = FastAPI(title="Scan API")

#* Setup endpoints
app.include_router(devices.router, prefix="/api/v1/devices", tags=["Devices"])
app.include_router(scans.router, prefix="/api/v1/scans", tags=["ScanSession"])
app.include_router(secret_routes.router, prefix="/api/v1")

@app.get("/health")
async def health():
    return {"status": "ok"}

#* Initialize Rammit connection
@app.on_event("startup")
async def startup_event():
    rabbit_init()
    
if __name__ == "__main__":
    uvicorn.run("app.main:app", host = "0.0.0.0", port = 8000, reload = True)
    
#* Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)