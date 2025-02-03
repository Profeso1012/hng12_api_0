from fastapi import FastAPI
from app.routes import router
from fastapi.middleware.cors import CORSMiddleware

# Create a FastAPI instance
app = FastAPI(title="HNG12 Public API", version="1.0")

# CORS Handling (Allows requests from anywhere)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)
