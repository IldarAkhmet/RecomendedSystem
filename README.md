<div align="center">
<h1>
  Recommended System
</h1>
</div>

### Задача проекта:
<div>
  Создать систему, которая способна, на данных о просмотрах и о проставленном пользователем рейтинге для поста, предсказывать какие посты пользователю могут также понравится.
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

### Метрика: 
<div>
  HitRate@5=0.523
</div>

---

### Проведенная работа:
<div>
  Был проведен полный EDA анализ над данными, в ходе которого выявилось каким образом разные независимые переменные влияют на таргет. Признак с текстом поста был проведен через ряд различных преобразований, на основе уже известных фичей были созданы новые, такие как: количество лайков на посту, длина текста. Все категориальные колонки были проведены через преобразования для перехода в метрическое пространство. Перебирались различные алгоритмы машинного обучения для получения лучше модели, перебирались разные параметры внутри этих алгоритмов. Был выбран алгоритм - catboost. С помощью FastAPI создан сервис, с помощью PostgreSQL создана база данных с таблицей из преобразованных данных для алгоритма.
</div>

---

### Планы по доработке:
<div>
  
  - Использовать методы глубокого обучения для более четкой обработки текстовой колонки и получения более хорошего значения по метрике.
 
</div>
