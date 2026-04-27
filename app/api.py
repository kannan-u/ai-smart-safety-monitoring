from fastapi import FastAPI

app = FastAPI()

@app.get("/alert")
def alert():
    print("🚨 ALERT RECEIVED FROM SYSTEM")
    return {"status": "ok"}