# coding: utf-8
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ObjectTable(Base):
    __tablename__ = 'object_table'

    object_id = Column(Integer, primary_key=True)
    object_name = Column(String(150), server_default=text("''::character varying"))
    object_type = Column(Integer)


class PrivilegeTable(Base):
    __tablename__ = 'privilege_table'

    parent_id = Column(Integer, primary_key=True, nullable=False)
    child_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, primary_key=True, nullable=False)
    privilege = Column(Integer, primary_key=True, nullable=False)


class ProjectGroup(Base):
    __tablename__ = 'project_group'

    project_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, primary_key=True, nullable=False)
    privilege = Column(Integer, primary_key=True, nullable=False)


class User(Base):
    __tablename__ = 'users'

    username = Column(String(20), primary_key=True)
    password = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False, server_default=text("nextval('users_user_id_seq'::regclass)"))
