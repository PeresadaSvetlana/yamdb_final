![example workflow](https://github.com/PeresadaSvetlana/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### **YaMDb** - База с отзывами и оценками пользователей на музыкальные произведения, книги и фильмы. 
Проект сделан в учебных целях на основе ранее созданного проекта api_yamdb мы создали и запустили Docker-контейнеры, научились обрабатывать Docker файлы, разместили свой первый образ на DockerHub.
Автор проекта студентка курса Яндекс.Практикум.

## **Технологии**

Python 3.7 Django 2.2.16
Docker

## **Как запустить проект:**

Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:PeresadaSvetlana/infra_sp2.git
```

```
cd infra_sp2/infra/
```

Собрать контейнеры и перезапустить их:

```
docker-compose up -d --build 

```

Выполнить миграции, создать суперпользователя и собрать статику:

```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input 
```



## **Некоторые примеры запросов к API.**

http://84.201.178.53/api/v1/auth/signup/

http://84.201.178.53/api/v1/genres/

http://84.201.178.53/api/v1/titles/{titles_id}/

http://84.201.178.53/api/v1/users/{username}/