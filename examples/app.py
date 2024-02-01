from fastapi import FastAPI, Depends, HTTPException
from schema import PostGet
import os
from model import load_models
from database import Base, engine, SessionLocal
from catboost import CatBoostClassifier
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String
from typing import List
from tablepost import Post
from datetime import datetime
import pandas as pd
import datetime


def get_db():
    with SessionLocal() as db:
        return db


model = load_models()

app = FastAPI()

posts = pd.read_sql(
    f"""
        SELECT *
        FROM public.i_ildar_23_features_lesson_22_10
    """,
        engine
    ).set_index('index')

### пока в разработке
# posts = pd.read_sql(
#     f"""
#         SELECT *
#         FROM public.posts_info_features_dl
#     """,
#     engine
# ).set_index('index')

@app.get('/post/recommendations/{id}', response_model=List[PostGet])
def recommended_posts(id: int = 200, limit: int = 5, db=Depends(get_db)) -> List[PostGet]:
    # now = datetime.datetime.now()
    user = pd.read_sql(
        f"""
                SELECT * 
                FROM public.user_data
                WHERE user_id = {id}
            """,
        engine
    )

    ### пока в разработке
    # user['hour'] = now.hour
    # user['month'] = now.month

    data = posts.join(user, how='cross')[['age', 'country', 'city', 'exp_group', 'text', 'topic', 'cnt_actions']]

    ### пока в разработке
    # data = posts.join(user, how='cross')[['hour', 'month', 'gender', 'age', 'country', 'city', 'exp_group', 'os',
    #    'source', 'topic', 'TextCluster', 'DistanceToCluster_0',
    #    'DistanceToCluster_1', 'DistanceToCluster_2', 'DistanceToCluster_3',
    #    'DistanceToCluster_4', 'DistanceToCluster_5', 'DistanceToCluster_6',
    #    'DistanceToCluster_7', 'DistanceToCluster_8', 'DistanceToCluster_9',
    #    'DistanceToCluster_10', 'DistanceToCluster_11', 'DistanceToCluster_12',
    #    'DistanceToCluster_13', 'DistanceToCluster_14']]

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