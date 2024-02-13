<div align="center">
<h1>
  Recommended System
</h1>
</div>

### О проекте:
<div>
  Задача создать систему, которая способна, на данных о просмотрах и о проставленном пользователем рейтинге для поста, предсказывать какие посты пользователю могут также понравится.
</div>

---

### Технологии:
<div align="center">
  <a href="https://github.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/git-scm-icon.svg" alt="Git" width="40" height="40" /></a>  
  <a href="https://www.postgresql.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/postgresql-original-wordmark.svg" alt="PostgreSQL" width="40" height="40" /></a>  
  <a href="https://www.python.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/python-original.svg" alt="Python" width="40" height="40" /></a>  
  <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> 
  <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a> 
  <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a> 
  <a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="seaborn" width="40" height="40"/> </a>
</div>

---

### Ссылка на соревнование с данными:
<div>
  <a href="https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data" target="_blank">
    <img src=https://img.shields.io/badge/kaggle-%2344BAE8.svg?&style=for-the-badge&logo=kaggle&logoColor=white alt=kaggle style="margin-bottom: 5px;" />
  </a> 
</div>

---

### Метрика: 
<div>
  RMSE=0.12888.
</div>

---

### Проведенная работа:
<div>
  
  -  HouseMarketAPI
  
  Был проведен полный EDA анализ, в ходе которого, были заполнены NaN значения в колонках, проведен анализ метрических фичей и категориальных, с помощью построенных графиков были убраны ненужные независимые переменные. Категориальные колонки были переведены в метрические с помощью advanced-счетчиков(mean-target encoding на валидационной выборке). Для построения модели машинного обучения перебирались различные алгоритмы начиная с линейных, заканчивая полноценными ансамблями с подбором параметров. В ходе подбора модели, лучшей оказался алгоритм catboost. Для создания API на основе алгоритма машинного обучения была создана база данных с удобным размещением таблицы с данными для модели, с помощью FastAPI был написан сервис, SqlAlchemy использовалась для удобной работы с данными из базы данных.

  -  HouseMarketAPP

  Было создано приложение с помощью WindowsForms C++, для которого создана таблица в базе данных для хранения информации о пользователях и объектах для размещения.
</div>

---

### Инструкции по развертыванию(HouseModelAPI):
<div>
  
  -  Загрузка данных для обучения с платформы Kaggle(ссылка выше).
  
  -  Работа над данными описанная в .ipynb файле.
  
  -  Создание базы данных и подключение ее в проекту по специальному пути.
  
  -  Запуск проекта.
</div>


### Инструкции по развертыванию(HouseModelAPP):
<div>
  
  -  Создание и подключение базы данных.
  
  -  Запуск проекта.
</div>

---

### Планы по доработке:
<div>
  - Соединить приложение написанное на C++ с моделью машинного обучения.
</div>
