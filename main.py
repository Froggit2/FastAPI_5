from fastapi import FastAPI
from routers import task, user

app = FastAPI()
app.include_router(user.router_user)
app.include_router(task.router_task)


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


# python -m uvicorn main:app