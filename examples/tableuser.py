from database import Base
from sqlalchemy.types import Integer, String
from sqlalchemy import Column


# создаем класс для определения типов таблиц в базе данных для работы через алхимию
class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'public'}

    age = Column(Integer)
    city = Column(String)
    country = Column(String)
    exp_group = Column(Integer)
    gender = Column(Integer)
    id = Column(Integer, primary_key=True)
    os = Column(String)
    source = Column(String)
