from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

projects = [
    {
        "id": 1,
        "name": "Project One",
        "description": "First mock project description.",
        "skills": ["Vue", "Node", "Docker"],
        "repo": "https://github.com/example/project-one",
    },
    {
        "id": 2,
        "name": "Project Two",
        "description": "Second mock project description.",
        "skills": ["Python", "Flask"],
        "repo": "https://github.com/example/project-two",
    },
]

@app.get("/api/projects")
async def get_projects():
    return projects
