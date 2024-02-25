from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# engine會使用postgressql+psycopg2來進行登入


db_engine = {
    "user": create_engine('postgresql+psycopg2://file_reader:reader_pwd@localhost:5432/file_system'),
    "service": create_engine("postgresql+psycopg2://service_user:service@localhost:5432/file_system"),
}


# 建立session
def get_session(role):
    if role not in db_engine:
        raise ValueError("Invalid role")
    session = sessionmaker(bind=db_engine[role])
    session = session()
    return session
