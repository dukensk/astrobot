# Часто используемые команды

### Обновить пакеты из requirements.txt (выполнять из вирт. окружения)
```sh
pip install --upgrade -r requirements.txt
```

### Создание приложения

```sh
python manage.py startapp app_name
```

_app_name_ – название приложения

## Миграции

### Создать миграции для приложения `app_name`

```sh
python manage.py makemigrations app_name
```

### Применить миграции

```sh
python manage.py migrate
```

### Отменить миграции приложения  `app_name`

```sh
python manage.py migrate app_name zero
```