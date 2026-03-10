from fastapi import FastAPI
from app.api.v1 import users

app = FastAPI(
    title="User Management API",
    version="1.0.0"
)

app.include_router(users.router, prefix="/v1")

@app.get("/")
def root():
    return {"message": "User Management API is running"}

