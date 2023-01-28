import os
import sqlalchemy
import psycopg2
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=60), unique=True)
    def __str__(self):
        return f'id: {self.id}, name: {self.name}'

class favorite(Base):
    __tablename__ = 'favorite'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    id_user = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(user.id), nullable=False)

    def __str__(self):
        return f'id: {self.id}, name: {self.id_user}'





def create_tables(engine):
    Base.metadata.create_all(engine)


def drop_tables(engine):
    Base.metadata.drop_all(engine)


db_type = 'postgresql'
db_login = 'postgres'
# БД нужно предварительно создать, например для терминала 'createdb -U postgres VKinder_DB'
db_name = 'VKinder_DB'
db_host = 'localhost:5432'
# предварительно прописываем в Environment Variables переменную с именем PAS в значение пароль от БД
db_pass = os.getenv('PAS')
DSN = f"{db_type}://{db_login}:{db_pass}@{db_host}/{db_name}"

if __name__ == '__main__':
    # создаем движок
    engine = sqlalchemy.create_engine(DSN)
    # создаем таблицы
    create_tables(engine)

    # создаем сессию
    # Session = sessionmaker(bind=engine)
    # session = Session()
