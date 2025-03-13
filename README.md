# backend

## Project setup
Activate virtual enviroment
```
python3 -m venv venv
```
```
source venv/bin/activate 
```

Instalar paquetes:
```
pip install -r requirements.txt
```

### Run server development
```
python manage.py runserver
```




# frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

El front debe ir en el puerto :8080 si no cambiar en el settings de django y poner CORS_ORIGIN_ALLOW_ALL = True