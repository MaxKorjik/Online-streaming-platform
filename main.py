from fastapi import FastAPI

app = FastAPI(debug=True)

@app.get("/")
async def home():
    return {"message" : "Hello"}