from sqlalchemy.types import Integer, String, TIMESTAMP
from sqlalchemy import Column, ForeignKey
from database import Base
from tablepost import Post
from tableuser import User
from sqlalchemy.orm import relationship

class Feed(Base):
    __tablename__ = 'feed_action'
    __table_args__ = {'schema': 'public'}

    user = relationship(User)
    post = relationship(Post)
    action = Column(String)
    time = Column(TIMESTAMP)
    post_id = Column(Integer,
                     ForeignKey(Post.id), primary_key=True)
    user_id = Column(Integer,
                     ForeignKey(User.id), primary_key=True)