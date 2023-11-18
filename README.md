![pipeline](https://gitlab.crja72.ru/django_2023/students/44991-and12062005-yandex.ru-47231/badges/main/pipeline.svg)

python3 -m venv venv

source venv\bin\activate
# Запускаем виртуальное окружение

pip3 install -r requirements/prod.txt
# Устанавливаем необходимые зависимости

pip3 install -r requirements/dev.txt
# Добавляем необходимые для разработки зависимости

pip3 install -r requirements/test.txt
# Устанавливаем необходимые зависимости для запуска тестов

django-admin startproject lyceum
# Создаем проект джанги

cd lyceum
# Переходим в созданный каталог


python manage.py startapp catalog
# Запускаем приложение каталог

python manage.py startapp homepage
# Запускаем приложение домашняя страница

python manage.py startapp about
# Запускаем приложение о нас

cp config.env .env
# Настройка перменных окружения



# Идем на https://app.quickdatabasediagrams.com
<!-- catalog_tag
-
id PK int FK >- catalog_item_tags.tag_id
name varchar(150)
is_published bool
slug varchar(200)

catalog_item
-
id PK integer FK >- catalog_item_tags.item_id
name varchar(150)
is_published bool
text text
category_id integer

catalog_item_tags
-
item_id integer 
tag_id integer 

catalog_category
-
id PK integer FK >- catalog_item.category_id
name varchar(150)
is_published bool
slug varchar(200)
weight integer -->
# Скачиваем диаграмму и переименовываем в ER.jpg

django-admin compilemessages
# Создаем файл с переводами

python manage.py runserver
# Запускаем сервер