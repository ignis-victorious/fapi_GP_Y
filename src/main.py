#
#  Import LIBRARIES
#  Import FILES
#   ___
from fastapi import FastAPI

app = FastAPI()


@app.get(path="/")
#  Import FILES LIBRARIES
def main() -> dict[str, str]:
    return {"message": "Hello World"}


# @app.get(path="/status")
# async def get_app() -> dict[str, bool | str]:
#     return {"success": True, "message": "You just created your first FastAPI endpoint"}
