from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import uvicorn
from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import List


class User(BaseModel):
    uid: str
    first_name: str
    last_name: str
    gender: str
    permission: str


db: List[User] = [
    User(uid=str(uuid4()),first_name="jacob",last_name="kolkhi", gender="male", permission="admin"),
    User(uid=str(uuid4()),first_name="dimi",last_name="kolkhi", gender="male", permission="user")
]


usermanager_app = FastAPI()


@usermanager_app.get("/", status_code=200)
async def root():
    # file = open("helloworld.html", "r")
    html_start = "<html><body>"
    html_end = "</body></html>"
    html_body = "welcome to my first containered usermanager app(fastapi framework)"
    return HTMLResponse(html_start + html_body + html_end, status_code=200)


@usermanager_app.get("/api/v1/users")
async def get_users():
    html_start = "<html><body>"
    html_end = "</body></html>"
    html_body = str(db)
    return HTMLResponse(html_start + html_body + html_end, status_code=200)


@usermanager_app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"new uid": user.uid}


@usermanager_app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: str):
    for user in db:
        if user.uid == user_id:
            db.remove(user)
            return {"deleted uid": user.uid}
    raise HTTPException(
        status_code=404,
        detail=f"user with uid: {user_id} doesnot exists"
        )


@usermanager_app.put("/api/v1/users/{user_id}")
async def update_user(updated_user: User, user_id: str):
    for user in db:
        if user.uid == user_id:
            user.first_name = updated_user.first_name
            user.last_name = updated_user.last_name
            user.gender = updated_user.gender
            user.permission = updated_user.permission
            return {"updated uid": user.uid}
    raise HTTPException(
        status_code=404,
        detail=f"user with uid: {user_id} doesnot exists"
        )


if __name__ == "__main__":
  uvicorn.run("main:usermanager_app", host='0.0.0.0', port=6002, reload=True)







