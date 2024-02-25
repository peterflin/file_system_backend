from utils.sql_helper import get_session
from utils.jwt_verify import get_password_hash
from models.orm_model import User
from pathlib import Path


class ServiceModel:
    def __init__(self):
        self.session = get_session("service")

    def list_dir(self, path):
        cur_path = Path.cwd() / path
        result = []
        if cur_path.is_dir():
            for x in cur_path.iterdir():
                if x.is_dir():
                    result.append({"name": x.name, "file_type": "dir"})
                else:
                    result.append({"name": x.name, "file_type": "file"})
            return {"dirs": result}
        else:
            return {"dirs": result}

    def __del__(self):
        self.session.close()
