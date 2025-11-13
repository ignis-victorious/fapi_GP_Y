#
#  Import LIBRARIES
from fastapi import FastAPI

from .utils import delete_user, get_user, patch_user, post_user, put_user

#  Import FILES
# from .data.contact_data import users

#   ___

app = FastAPI()


@app.get(path="/")
#  Import FILES LIBRARIES
def main() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get(path="/status")
async def get_app() -> dict[str, bool | str]:
    return {"success": True, "message": "You just created your first FastAPI endpoint"}


@app.get(path="/get_user")
async def get_user_from_id(user_id: int) -> dict[str, bool | dict[str, str]]:
    try:
        user_data: dict[str, str] | None = get_user(user_id=user_id)
        # print(f"user_id: {user_id}")
        # print(f"--get_user(user_id=user_id): {get_user(user_id=user_id)}")
        # print(f"User_data = {user_data}")
        return {"success": True, "data": user_data}
    except Exception as e:
        raise e


@app.post(path="/add_user")
async def add_new_user(user_id: int, name: str, email: str, phone: str) -> dict[str, bool | dict[int, dict[str, str]]]:
    try:
        user_data: dict[int, dict[str, str]] = post_user(user_id=user_id, name=name, email=email, phone=phone)
        return {"success": True, "data": user_data}
    except Exception as e:
        raise e


@app.patch(path="/update_user")
async def update_user(
    user_id: int, name: str | None = None, email: str | None = None, phone: str | None = None
) -> dict[str, bool | dict[int, dict[str, str]]]:
    try:
        user_data: dict[int, dict[str, str]] = patch_user(user_id=user_id, name=name, email=email, phone=phone)
        return {"success": True, "data": user_data}

    except Exception as e:
        raise e


@app.delete(path="/delete_user")
async def delete_user_by_id(user_id: int) -> dict[str, bool | dict[int, dict[str, str]]]:
    try:
        user_data: dict[int, dict[str, str]] = delete_user(user_id=user_id)
        return {"success": True, "data": user_data}

    except Exception as e:
        raise e


@app.put("/put_user")
async def update_user_details(
    user_id: int, name: str, email: str, phone: str
) -> dict[str, bool | dict[int, dict[str, str]]]:
    try:
        user_data: dict[int, dict[str, str]] = put_user(user_id=user_id, name=name, email=email, phone=phone)
        return {"success": True, "data": user_data}
    except Exception as e:
        raise e
