from pydantic import Basemodel
from utils.sqlhelper import get_session
from utils.util_func import hash_password


class UserLogin(Basemodel):
    username: str
    password: str
    privileges: int


class UserModel:
    def __init__(self, username, password, privileges):
        self.session = get_session()
        # self.username = username
        # self.password = password
        # self.privileges = privileges

    def login(self, username, password):
        password = self.session.query(UserLogin.password).filter(UserLogin.username == username).first()
        hashed_password = hash_password(password)['password']
        if hashed_password == password:
            return hashed_password

    def __repr__(self):
        return f"UserModel(username={self.username}, password={self.password}, privileges={self.privileges})"

    def __str__(self):
        return f"UserModel(username={self.username}, password={self.password}, privileges={self.privileges})"
