from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.routers.intents import router as intents_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Perform any startup tasks here
    print("Starting up the application...")
    yield
    # Perform any shutdown tasks here
    print("Shutting down the application...")


app = FastAPI(
    title= 'Chowder API',
    description='An Autonomous AI That Decides, Pays, and Acts For You.',
    version='0.1.0',
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4173"],  # Allow the frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(intents_router)


@app.get('/')
async def root():
    return {
        "message": "Welcome to the Chowder API!"
    }

if __name__ == "__main__":
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=8000,
    )
