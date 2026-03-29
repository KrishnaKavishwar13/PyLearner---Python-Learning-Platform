from fastapi import FastAPI

# Database
from app.database import Base, engine

# Models (IMPORTANT: import all models here)
from app.models import user, question, result

# Routes
from app.routes import auth, quiz


# Create FastAPI app
app = FastAPI(
    title="AI Python Learning Platform API",
    version="1.0.0"
)

# Create tables in DB
Base.metadata.create_all(bind=engine)


# Root route (health check)
@app.get("/")
def home():
    return {"message": "API is running 🚀"}


# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

app.include_router(quiz.router, prefix="/quiz", tags=["Quiz"])