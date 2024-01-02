from fastapi import FastAPI, Depends, HTTPException
from schema import PostGet
import os
from catboost import CatBoostClassifier
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String
from typing import List
from datetime import datetime
import pandas as pd


SQLALCHEMY_DATABASE_URL = "postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Post(Base):
    __tablename__ = 'post'
    __table_args_ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)

def get_db():
    with SessionLocal() as db:
        return db

def get_model_path(path: str) -> str:
    if os.environ.get("IS_LMS") == "1":  # проверяем где выполняется код в лмс, или локально. Немного магии
        MODEL_PATH = '/workdir/user_input/model'
    else:
        MODEL_PATH = path
    return MODEL_PATH


def load_models():
    model_path = get_model_path("C:\MyJupyterNotebook\KC_ML\lesson_22\catboost_model3")
    model = CatBoostClassifier()
    model.load_model(model_path)  # пример как можно загружать модели

    return model

model = load_models()

app = FastAPI()

posts = pd.read_sql(
    f"""
        SELECT *
        FROM public.i_ildar_23_features_lesson_22_10
    """,
        engine
    ).set_index('index')

@app.get('/post/recommendations/', response_model=List[PostGet])
def recommended_posts(id: int = 200, limit: int = 5, db=Depends(get_db)) -> List[PostGet]:

    user = pd.read_sql(
        f"""
                SELECT * 
                FROM public.user_data
                WHERE user_id = {id}
            """,
        engine
    )
    data = posts.join(user, how='cross')[['age', 'country', 'city', 'exp_group', 'text', 'topic', 'cnt_actions']]
    data['pred'] = model.predict_proba(data)[:, 1] # переводим наши предсказания в вероятности

    data['post_id'] = posts['post_id']
    data = data.sort_values(by='pred', ascending=False).head(limit) # делаем reset_index чтобы добавить post_id, сортируем по предсказаниям и выводим limit постов
    indexes = list(data['post_id'])



    query = db.query(Post).filter(Post.id.in_(indexes)).all() # сделаем запрос по нужным нам индексам
    db.close()

    # query = db.query(Post).filter(Feed.action == 'like') \
    #     .join(Post).group_by(Post.id) \
    #     .order_by(func.count(Post.id).desc()).limit(limit).all()

    return query