from fastapi import FastAPI

app = FastAPI(
    title="ProcureTrack",
    description="Procurement order tracking for Everluxe",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}