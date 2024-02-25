from fastapi import APIRouter, Request, HTTPException, Depends, status, Form, Body
from fastapi.security import OAuth2PasswordRequestForm
from utils.jwt_verify import get_current_active_user
from datetime import timedelta
from utils.verify_model import Token, User, Directory
from utils.jwt_verify import get_password_hash
from models.service_model import ServiceModel


service_router = APIRouter()


@service_router.get("/service/list_dir", response_model=Directory, tags=["Service"])
def service_list_dir(request: Request, current_user: User = Depends(get_current_active_user)):
    result = ServiceModel().list_dir(request.query_params.get("path"))
    return result
