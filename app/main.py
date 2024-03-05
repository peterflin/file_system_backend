# 我想寫一個具有登入系統的Web API
# 並且可以記錄登入紀錄

from fastapi import FastAPI
from routers.user_controller import user_router
from routers.service_controller import service_router


app = FastAPI()

app.include_router(user_router)
app.include_router(service_router)
