from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# engine會使用postgressql+psycopg2來進行登入

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')


# 建立session
def get_session():
    session = sessionmaker(bind=engine)
    session = session()
    return session
