# coding: utf-8
from sqlalchemy import BigInteger, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    username = Column(String(20), primary_key=True)
    password = Column(String, nullable=False)
    privilege = Column(BigInteger)
