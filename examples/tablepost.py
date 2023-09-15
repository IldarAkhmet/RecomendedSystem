from database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String

class Post(Base):
    __tablename__ = 'post'
    __table_args_ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)