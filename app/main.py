from fastapi import FastAPI
from app.database import engine, Base
from app.routes import user

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Register Routes
app.include_router(user.router, prefix="/api", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}
