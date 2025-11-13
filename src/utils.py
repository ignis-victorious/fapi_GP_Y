#
#  Import LIBRARIES
from fastapi import HTTPException

#  Import FILES
from .data.contact_data import users

#   ___


def get_user(user_id: int) -> dict[str, str]:
    data: dict[str, str] | None = users.get(user_id)
    print(f"Inside get_user - Data = {data}")
    if not data:
        raise HTTPException(status_code=404, detail="No user with such id")
    return data


def post_user(user_id: int, name: str, email: str, phone: str) -> dict[int, dict[str, str]]:
    if user_id in users:
        raise HTTPException(status_code=400, detail=f"User with id {user_id} already exists")
    users[user_id] = {"name": name, "email": email, "phone": phone}
    return users


def patch_user(
    user_id: int, name: str | None = None, email: str | None = None, phone: str | None = None
) -> dict[int, dict[str, str]]:
    if user_id not in users:
        raise HTTPException(status_code=400, detail="No user with such id.")

    # return ("error": "User not found"}
    if name:
        users[user_id]["name"] = name
    if email:
        users[user_id]["email"] = email
    if phone:
        users[user_id]["phone"] = phone

    return users


def delete_user(user_id: int) -> dict[int, dict[str, str]]:
    if user_id not in users:
        raise HTTPException(status_code=400, detail=f"User with id {user_id} does not exist")
    print(f"Del users: {users[user_id]}")
    del users[user_id]
    return users


def put_user(user_id: int, name: str, email: str, phone: str) -> dict[int, dict[str, str]]:
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    # Replace entire user record

    users[user_id] = {"name": name, "email": email, "phone": phone}
    return users
    # return {"message": f"User with id {user_id} updated successfully"}
