from fastapi import APIRouter


router = APIRouter()


# 我想透過帶入username與password來登入
# 帳號認證是到PostgreSQL資料庫來進行認證
# 如果成功就回傳token
# token是使用jwt token來進行認證
@router.get("/api/login")
def login(username: str, password: str):
    if username == "admin" and password == "admin":
        return {"token": "123"}
    else:
        return {"error": "username or password is wrong"}
    