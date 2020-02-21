from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"id": user_id, "emai": "kek@lol.com"}
