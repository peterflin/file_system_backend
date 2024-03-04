from utils.sql_helper import get_session
from utils.jwt_verify import get_password_hash
from models.orm_model import User
from pathlib import Path


class FileSystemModel:

    def list_dir(self, path):
        cur_path = Path.cwd() / path
        print(Path.cwd(), cur_path)
        result = {}
        if cur_path.is_dir():
            for x in cur_path.iterdir():
                if x.is_dir():
                    result[x.name] = {"name": x.name, "file_type": "dir"}
                else:
                    result[x.name] = {"name": x.name, "file_type": "file"}
            return result
        else:
            return result
