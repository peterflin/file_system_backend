# 我想寫一個具有登入系統的Web API
# 並且可以記錄登入紀錄

from fastapi import FastAPI, Request



app = FastAPI()


@app.post("/login")
def log_in(request: Request, username: str, password: str):
    # 寫入登入紀錄
    pass

