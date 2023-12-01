# Template para Django Rest Framework

Haz tu venv en python e instala las dependencias

```sh
# Venv, Activate, Requirements, Upgrade PIP    en linux
python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && pip install -r requirements.txt
```

```sh
# VENV
python -m venv venv
```

```sh
# ACTIVATE
source venv/bin/activate
```

```sh
# REQUIREMENTS
pip install -r requirements.txt
```

```sh
# UPGRADE PIP
pip install -r requirements.txt
```

## La URL de la API

```www
http://localhost:8000/api/v1/
```

Ya estan generadas las urls basicas GET,PATCH,DELETE,POST

En `Backend/DRF_API/settings.py` el final encontraras el CORS para que puedas agregar la URL del Frontend

```py
# Aqui se define la URL del Frontend para poder hacer peticiones al Backend
CORS_ALLOWED_ORIGINS = [
    "http://localhost:4321", # Astro por defecto.
    "http://localhost:5173", # React, Vue, Svelte. (Vite) por defecto
]
```

Y listo, la templeta ya viene con un modelo definido de Task, pero puedes cambiarlo al que tu desees haciendo sus correspondientes cambios de Django

```sh
python manage.py runserver
```

La API no esta autodocumentada
