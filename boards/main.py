from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, boards, tasks
from authenticator import authenticator
import os

app = FastAPI()
app.include_router(users.router)
app.include_router(boards.router)
app.include_router(authenticator.router)
app.include_router(tasks.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get("CORS_HOST", "https://404-waffle.gitlab.io"),
        os.environ.get("CORS_HOST", "https://boards-service.nov-pt-2.mod3projects.com"),
        os.environ.get("CORS_HOST", "http://localhost:3000"),
        os.environ.get("CORS_HOST", "http://localhost:8080"),
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/launch-details")
def launch_details():
    return {
        "launch_details": {
            "year": 2023,
            "month": 3,
            "day": "10",
            "hour": 19,
            "min": 0,
            "tz:": "PST",
        }
    }

#         os.environ.get("CORS_HOST"),
#         "http://localhost:3000",
#         "http://localhost:8080",
#         os.environ.get("CORS_HOST", "http://localhost:3000"),
#         os.environ.get("CORS_HOST", "http://localhost:8080"),
