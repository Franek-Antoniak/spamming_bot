import requests

# Spam 2000 request-POST
for x in range(2000):
    requests.post('http://localhost:8080/api/task/new', json={"description": "You are being hacked!"})

# Spam 100 request-GET wywołujący WARNING w Javie
for x in range(1000):
    requests.get('http://localhost:8080/api/task/get/task', json={"uniqueId": "You are being hacked!"})

# Spam 300 request-PATCH - odznaczanie i zaznaczanie zadania
# Aby zobaczyć wystarczy szybko klikać F5
# Aby zdobyć UUID wystarczy wysłać posta o nowy Task i odczytać return value od serwera
# for x in range(1000):
#     requests.patch('http://localhost:8080/api/task/update', json={"uniqueId": "TRZEBA PODMIENIC NA ISTNIEJACE UUID",
#                                                                   "done": ("true", "false")[x % 2]})

# Kodowanie requestów
r = requests.get('http://localhost:8080/api/task/get/task', json={"uniqueId": "You are being hacked!"})
print("Kodowanie: " + r.encoding)

# Wynik z request-POST
r = requests.post('http://localhost:8080/api/task/new', json={"description": "You are being hacked!"})
print("Otrzymaliśmy JSON\'a: " + r.text)

# Status code
x = requests.post('http://localhost:8080/api/task/ERROR', json={"descrsafadsn": "You are being hacked!"})
print("Status code posta wywołującego błąd: " + str(x.status_code))
print("Status code posta bez błędu: " + str(r.status_code))

# Exception -> x.raise_for_status()

# Response Headers
print(r.headers)
print(r.headers.get('content-type'))
print(x.headers.get('content-type'))
