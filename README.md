Инструкция для запуска:  
```
docker-compose build
docker-compose up
```

`http://127.0.0.1:8000/api/` - сделать POST request/ добавить URL  
`http://127.0.0.1:8000/shortener/` - список и статистика переходов по всем URL в таблице  





Если команда docker-compose up выдает ошибку типа `django.db.utils.OperationalError: connection to server at "pgdatabase" (172.25.0.3), port 5432 failed: FATAL:  no pg_hba.conf entry for host "172.25.0.4"` - нужно в docker-compose увеличить параметр sleep для запуска app
