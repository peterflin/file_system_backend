from pydantic import BaseModel
from utils.sql_helper import get_session
from utils.jwt_verify import verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, get_password_hash
from utils.verify_model import Token
from datetime import timedelta
from models.orm_model import User


class UserModel:
    def __init__(self):
        self.session = get_session("user")
        # self.username = username
        # self.password = password
        # self.privileges = privileges

    def login(self, username, password):
        user_row = self.session.query(User.password).filter(User.username == username).first()
        user = verify_password(password, user_row.password)
        if not user:
            return None
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": username}, expires_delta=access_token_expires
        )
        return Token(access_token=access_token, token_type="bearer")
    
    def register(self, username, password, privilege=1):
        user = User(username=username, password=get_password_hash(password), privilege=privilege)
        self.session.add(user)
        self.session.commit()
        return user

    def __del__(self):
        self.session.close()
