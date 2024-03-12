from fastapi import FastAPI, HTTPException
from modules import Gender, Role, User, updateUserDetails



app = FastAPI()

db:list[User] = [
  User(id=1, full_name="Jeson Roy", gender=Gender.male, roles=[Role.user, Role.admin]),
  User(id=2, full_name="Qurtileen rouge", gender=Gender.female, roles=[Role.student])
]
@app.get("/")
async def root():
  return {"Response":"Hello World"}


@app.get("/api/users")
async def fetch_users():
  return db


@app.post("/api/users")
async def create_user(user:User):
  db.append(user)


@app.delete("/api/users/{id}")
async def delete_user(id:int):
  for user in db:
    if user.id == id:
      db.remove(user)
      return
    raise HTTPException(status_code=404, detail=f"User with id: {id} not found")

@app.put("/api/users/{id}")
async def update_user(updatedUser:updateUserDetails, id:int):
  for usr in db:
    if usr.id == id:
      if updatedUser.full_name is not None:
        usr.full_name = updatedUser.full_name
      if updatedUser.roles is not None:
        usr.roles = updatedUser.roles
      return
    raise HTTPException(status_code=404, detail=f"User with id: {id} not found")