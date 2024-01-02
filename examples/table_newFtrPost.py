from database import Base
from sqlalchemy.types import Integer, String, Float
from sqlalchemy import Column


class Features(Base):
    __tablename__ = 'i_ildar_23_features_lesson_22'


    post_id = Column(Integer, primaty_key=True)
    text = Column(String)
    topic = Column(String)
    max_tfidf = Column(Float)
    cnt_actions = Column(Integer)

