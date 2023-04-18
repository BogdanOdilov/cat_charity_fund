# QRKot

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Git](https://img.shields.io/badge/-Git-464646?style=flat&logo=Git&logoColor=ffffff&color=043A6B)](https://www.git-scm.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-464646?style=flat&logo=FastAPI&logoColor=ffffff&color=043A6B)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)

Проект QRKot — приложение для Благотворительного фонда поддержки котиков. Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

## Технологии
- Python 3.10
- Git
- SQLAlchemy 1.4

## Использование
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/BogdanOdilov/cat_charity_fund.git
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас Windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать файл .env:

```
APP_TITLE=Благотворительный фонд котиков
DESCRIPTION=Сбор пожертвований на нужды хвостатых
DATABASE_URL=your_database
SECRET=your_secret
FIRST_SUPERUSER_EMAIL=your_email
FIRST_SUPERUSER_PASSWORD=your_password
```

Автогенерация миграций:

```
alembic revision --autogenerate -m "First migration"
```

Применение миграций:

```
alembic upgrade head
```

Запуск проекта:

```
uvicorn app.main:app --reload
```

Документация API:

```
http://127.0.0.1:8000/docs
```

Автор: [Богдан Одилов](https://github.com/BogdanOdilov)
