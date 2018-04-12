# Probe

## Что и зачем
* Возвращает любые http-статусы

* Возвращает ответ с произвольной задержкой

Для тестирования всяческих программных окружений.

## Запуск

```
docker build -t probe . && docker run -ti -p 8000:8000 probe python app.py
```

## Ручки

* Cтатусы

```
~ > curl -i http://localhost:8000/status/599
HTTP/1.1 599 UNKNOWN RESPONSE
Connection: keep-alive
Keep-Alive: 5
Content-Length: 29
Content-Type: text/plain; charset=utf-8

Network connect timeout error%

~ > curl -i http://localhost:8000/status/402
HTTP/1.1 402 Payment Required
Connection: keep-alive
Keep-Alive: 5
Content-Length: 16
Content-Type: text/plain; charset=utf-8

Payment Required%

```

* Задержка

```
~ > curl -i http://localhost:8000/delay/10
<тут проходит 10 секунд>
HTTP/1.1 200 OK
Connection: keep-alive
Keep-Alive: 5
Content-Length: 26
Content-Type: application/json

{"status":"ok","delay":10}%
```


