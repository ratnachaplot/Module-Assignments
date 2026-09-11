#Build a FastAPI service with CRUD endpoints, request validation, error handling, and automated docs.
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    name: str
    email: str
    age: int

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

@app.post("/users")
def create_user(user: User):
    users.append(user)

    return user

@app.get("/users")
def get_users():
    return users

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):

    if user_id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")

    users[user_id] = user

    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    if user_id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")

    deleted_user = users.pop(user_id)

    return deleted_user