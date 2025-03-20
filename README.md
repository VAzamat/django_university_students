# Django проект работы со "студентами"

Ключевые слова:
- django
- skypro_python41.0
- студенты

### Эволюция проекта
- [x] Классная работа "20.1 Работа с ORM (Object-Relational Mapping) в Django"
- [x] Классная работа "20.2 Работа с шаблонами, статическими файлами, шаблоном bootstrap"

### Шаг за шагом

#### 20.1 Работа с ORM (Object-Relational Mapping) в Django

 - Настройка работы с базой данных  СУБД PostgreSQL
 - Создаем модель в Django для класса студент (class Student)
 - Создаем миграцию и применяем миграцию с номером 0001
 - Настраиваем пути в urls.py, MEDIA_URL и MEDIA_ROOT
 - Создаем контроллер index в views.py и страницу templates/students/index.html
 - Настраиваем админку, python manage.py createsuperuser
 - Заполнение базы данных python manage.py dumpdata и loaddata

#### 20.2  Шаблонизация в Django

 - Настройка статических файлов
 - Шаблоны на основе Bootstrap
 - Подшаблоны и базовые шаблоны
 - Новые шаблонные теги и фильтры в templatetags/path_tag_filter.py
 - Ссылки на рисунки и меню