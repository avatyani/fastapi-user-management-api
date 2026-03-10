from fastapi import FastAPI

app = FastAPI(
    title="User Management API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "User Management API is running"}