from fastapi import FastAPI

process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0"

app = FastAPI()

@app.get("/")
def instant():
    return "Live from production!"