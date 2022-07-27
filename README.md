# Simple ElasticSearch integration in Django

Небольшой учебный проект демонстрирующий интеграцию DJANGO и ElasticSearch, на основе статьи django.fun:

### Функционал

- Автоматическое заполнение тестовыми данными базы данных.
- Индексирование базы данных с помощью ElasticSearch.
- Возможность добавления и редактирования данных о пользователе через админку.
- Поиск с помощью ElasticSearch.

### Интересное

- Кастомная команда заполнения базы данных.
- Поиск с помощью ElasticSearch
- Возможность развернуть сервис с помощью Docker-Compose


**Ссылки**:
- [Django.fun](https://django.fun/tutorials/django-rest-framework-i-elasticsearch/)


### Инструменты

- Python >= 3.10
- Django >= 4.0
- Django Rest Framework >= 3.13.1
- ElasticSearch = 7.17.5
- Docker


## Старт

#### 1) Переименовать "!.env copy" на ".env" и прописать свои настройки

    SECRET_KEY=django_key
    ALLOWED_HOSTS=localhost 127.0.0.1
    DEBUG_OPTIONS=1
    
    ES_NAME=имя_твоего_контейнера_ElasticSearch
    ES_HOSTS=<имя_твоего_контейнера_ElasticSearch>:9200



#### 2) Создать образ и запустить контейнер

    docker-compose up --build

##### 3) Создать супер юзера

    docker exec -it dc-esdjango bash
    cd core/
    python manage.py createsuperuser

##### 3.1) В случае необходимости заполнить базу данных
    
    python manage.py populate_db

##### 4) Заполнение и сопоставление индекса ElasticSearch

    python manage.py search_index --rebuild

##### 0) Для тестирования работы поиска доступны следующие конечные точки:
    
    - http://127.0.0.1:8001/search/user/jess_/
    - http://127.0.0.1:8001/search/category/seo/
    - http://127.0.0.1:8000/search/article/linux/
