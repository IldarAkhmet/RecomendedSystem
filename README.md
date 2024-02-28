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
<div>
  Python(pandas, seaborn, numpy, matplotlib, scikit-learn, sqlalchemy, fastapi), SQL(postgresql)
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
