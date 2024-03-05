from fastapi import APIRouter, Request, HTTPException, Depends, status, Form, Body
from fastapi.security import OAuth2PasswordRequestForm
from utils.jwt_verify import get_current_active_user
from datetime import timedelta
from utils.verify_model import Token, User
from utils.jwt_verify import get_password_hash
from models.user_model import UserModel


user_router = APIRouter()


@user_router.post("/user/token", tags=["User"])
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Token:
    token = UserModel().login(form_data.username, form_data.password)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token


@user_router.post("/user/register", tags=["User"])
async def register_user(user: User):
    return UserModel().register(user.username, user.password)
