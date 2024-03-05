from utils.sql_helper import get_session
from models.orm_model import PrivilegeTable, ObjectTable
from sqlalchemy import and_


class ServiceModel:
    def __init__(self):
        self.session = get_session("service")

    def get_object_id(self, path_name):
        return self.session.query(ObjectTable.object_id).filter(ObjectTable.object_name == path_name).first()

    def get_user_id(self, username):
        return self.session.query(UserTable.user_id).filter(UserTable.username == username).first()

    def get_privileges(self, current_path, current_user):
        sub_q1 = self.session.query(PrivilegeTable.child_id, PrivilegeTable.privilege).filter(PrivilegeTable.parent_id == current_path).filter(
            PrivilegeTable.user_id == current_user
        ).subquery()
        # print([row._mapping for row in sub_q1])
        # sub_q = self.session.query(PrivilegeTable.child_id, PrivilegeTable.privilege).filter(PrivilegeTable.user_id == current_user).subquery()
        result = self.session.query(ObjectTable.object_name, ObjectTable.object_type).join(sub_q1, sub_q1.c.child_id == ObjectTable.object_id).all()
        return [row._mapping for row in result]

    def __del__(self):
        self.session.close()
