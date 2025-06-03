💡 Проект: “Платформа бронирования курсов/мероприятий”
Описание: Пользователь может регистрироваться, просматривать список курсов/ивентов,
бронировать участие, а администратор — добавлять и редактировать мероприятия.

Приложения:

1. users – регистрация, логин, профиль.
2. courses – курсы/мероприятия: CRUD, отображение, категории.
3. bookings – бронирование курсов/мероприятий, отображение личных бронирований.
4. (опционально) adminpanel – отдельный интерфейс для модерации (можно просто
   через admin, но можешь сделать views).

Фичи:
• Разделение прав доступа (обычный пользователь / админ).
• Авторизация/регистрация.
• Список мероприятий с фильтрацией.
• Детали мероприятия.
• Бронирование и отображение бронирований.

🧩 Приложения:

1. users
   • Регистрация / логин (JWT)
   • Профиль
2. events
   • CRUD мероприятий
   • Список, поиск, фильтрация
3. bookings
   • Пользователь может бронировать участие в мероприятии
   • Посмотреть свои бронирования

---

1. Структура проекта

   event_booking/
   ├── manage.py
   ├── event_booking/
   │ └── settings.py
   ├── users/
   │ └── models.py, views.py, urls.py
   ├── events/
   │ └── models.py, views.py, urls.py
   ├── bookings/
   │ └── models.py, views.py, urls.py

2. Установка django
   pip install django djangorestframework psycopg2-binary djangorestframework-simplejwt

3. Добавление изменений в файлы
   users/models.py
   events/models.py
   bookings/models.py
В settings.py:
```python
DATABASES = {
   'default': {
      'ENGINE': 'django.db.backends.postgresql',
      'NAME': 'event_booking',
      'USER': 'postgres',
      'PASSWORD': 'yourpassword',
      'HOST': 'localhost',
      'PORT': '5432',
   }
}

INSTALLED_APPS = [
   'rest_framework',
   'rest_framework_simplejwt',
   'users',
   'events',
   'bookings',
]

AUTH_USER_MODEL = 'users.User'
```

В settings.py:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
```

В users/urls.py:
В users/views.py:
В users/serializers.py:

events/serializers.py
events/views.py
events/urls.py

bookings/serializers.py
bookings/views.py
bookings/urls.py

bookings/serializers.py (добавим второй сериализатор)
bookings/views.py (добавим создание бронирования)
bookings/urls.py (добавим в маршруты)