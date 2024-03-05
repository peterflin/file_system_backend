from pydantic import BaseModel
from typing import Union


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    username: str
    password: str


class DirectoryInput(BaseModel):
    path: str
    object_id: int


class File(BaseModel):
    name: str
    file_type: str


class Directory(BaseModel):
    dirs: list[File]
