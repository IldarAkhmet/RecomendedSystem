import os
from catboost import CatBoostClassifier


# функция для загрузки модели
def load_models():
    model_path = r"model\catboost_model3"
    model = CatBoostClassifier()
    model.load_model(model_path)  # пример как можно загружать модели

    return model
