from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "System Running"}

@app.get("/alert")
def alert():
    return {"message": "Human detected in restricted zone CATION!!!"}