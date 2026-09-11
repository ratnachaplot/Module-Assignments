from fastapi import FastAPI, HTTPException, WebSocket
from pydantic import BaseModel, EmailStr
from database import SessionLocal, engine
from models import Base, User

app = FastAPI()
cache = {}

Base.metadata.create_all(bind=engine)


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int


@app.get("/")
def home():
    return {"message": "Database connected!"}


@app.post("/users")
def create_user(user: UserCreate):
    db = SessionLocal()

    new_user = User(
        name=user.name,
        email=user.email,
        age=user.age
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    cache.pop("users", None)
    db.close()

    return new_user


@app.get("/users")
def get_users():

    if "users" in cache:
        return cache["users"]

    db = SessionLocal()

    users = db.query(User).all()

    db.close()

    cache["users"] = users

    return users


@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate):
    db = SessionLocal()

    existing_user = db.query(User).filter(User.id == user_id).first()

    if existing_user is None:
        db.close()
        raise HTTPException(status_code=404, detail="User not found")

    existing_user.name = user.name
    existing_user.email = user.email
    existing_user.age = user.age

    db.commit()
    db.refresh(existing_user)
    cache.pop("users", None)
    db.close()

    return existing_user


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    db = SessionLocal()

    existing_user = db.query(User).filter(User.id == user_id).first()

    if existing_user is None:
        db.close()
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(existing_user)
    db.commit()
    cache.pop("users", None)
    db.close()

    return {"message": "User deleted successfully"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        message = await websocket.receive_text()

        await websocket.send_text(f"You said: {message}")