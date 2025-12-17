# Домашнее задание "Работа с ORM"

Импорт каталога телефонов из CSV с сохранением в БД и онлайн-библиотека с фильтрацией по датам.

---

## 1) Каталог телефонов из CSV - БД - Сайт
- Есть `phones.csv`.
- Данные импортируются в базу данных в модель `Phone`
- На сайте:
  - `/catalog/` показывает список всех телефонов
  - `/catalog/<slug>/` показывает страницу конкретного телефона
  - в каталоге есть сортировка: по имени, по цене по возрастанию, по цене по убыванию 

### Запуск:
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py import_phones
python manage.py runserver
```

## 1) Онлайн-библиотека книг
### Страницы:
- `/books/` — список всех книг
- `/books/YYYY-MM-DD/` — книги, опубликованные в конкретную дату
- На странице `/books/YYYY-MM-DD/` есть ссылки на предыдущую и следующую дату публикации (если такие даты есть в базе).

### Запуск:
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/books.json
python manage.py runserver
```
