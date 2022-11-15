# 💬 YaMDb - приложение для сбора отзывов
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django) ![Django](https://img.shields.io/badge/Django-2.2.19-green) ![DRF](https://img.shields.io/badge/DRF-3.12.4-green) ![API](https://img.shields.io/badge/API-v.1-red)

Приложение для сбора отзывов пользователей о фильмах, книгах, музыке. Каждое произведение может быть объединено администратором в категории и назначены жанры. Посредством REST API пользователи могут регистрироваться в приложении, авторизироваться, добавлять обзоры, оставлять оценки и комментарии к произведениям.

## Содержание

- [Описание](#Описание)
- [Описание API](#Описание-API)
- [Установка и запуск](#Установка-и-запуск)
- [Использованные технологии](#Использованные-технологии)
- [Лицензия](#Лицензия)
- [Авторы](#Авторы)

## Описание

Приложение представляет собой REST API, пользователи которого могут:
- регистрироваться в приложении, получая код подтверждения на свой e-mail
- получать токен для полноценного доступа к API, работа с токенами реализована с помощью библиотеки `SimpleJWT`
- авторизованные пользователи могут изменять свои учетные данные через специальный адрес `/users/me`
- администраторы могут создавать новых пользователей, изменять их учетные данные других пользователей
- пользователи могут запрашивать категории произведений, жанры, произведения, отзывы, комментарии к отзывам
- оставлять отзывы и рейтинг на произведения, комментировать другие отзывы, редактировать и удалять свои отзывыв и комментарии

## Описание API

Методы API имеют разграниченный доступ. Пользователи делятся на:
- пользователей
- модераторов
- администраторов

📖 Подробное интерактивное описание всех доступных методов эндпоинта расположено по адресу:
```http
  http://127.0.0.1:8000/swagger/
```
```http
  http://127.0.0.1:8000/redoc/
```
## Установка и запуск

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/spaut33/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Для наполнения базы данных тестовыми данными можно использовать команду:

```
python3 manage.py import_csv
```

## Использованные технологии

- [Python 3.7](https://www.python.org/)
- [Django 2.2](https://www.djangoproject.com/)
- [Django Rest Framework 3.12](https://www.django-rest-framework.org/)
- [djangorestframework-simplejwt](https://github.com/jazzband/djangorestframework-simplejwt)
- [django-filter](https://github.com/carltongibson/django-filter/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [drf-yasg](https://github.com/axnsan12/drf-yasg)
- [pytest](https://docs.pytest.org/)
    
## Лицензия

[MIT](https://choosealicense.com/licenses/mit/)


## Авторы

- [Александр Ежов](https://www.github.com/Niea-under-7)
- [Егор Житников](https://www.github.com/egor-zhit)
- [Роман Петраков](https://www.github.com/spaut33)



- [Сергей Ивакин]() - Наставник
- [Андрей Квичанский](https://www.github.com/kvichans) - Ревьюер