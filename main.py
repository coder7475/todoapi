from fastapi import FastAPI

api = FastAPI()


all_todos = [
    {
        "todo_id": 1,
        "todo_name": "Exercise",
        "todo_description": "Exercise every morning for 30 minutes",
    },
    {"todo_id": 2, "todo_name": "Read", "todo_description": "Read 20 pages of a book"},
    {
        "todo_id": 3,
        "todo_name": "Work on Project",
        "todo_description": "Spend 2 hours on personal project",
    },
    {
        "todo_id": 4,
        "todo_name": "Learn",
        "todo_description": "Watch one tutorial on Docker",
    },
    {
        "todo_id": 5,
        "todo_name": "Plan Next Day",
        "todo_description": "Write down tasks for tomorrow",
    },
]


@api.get("/")
async def index():
    return {"message": "Hello World"}
