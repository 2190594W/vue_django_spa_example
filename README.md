# vue_django_spa_example

## The project is comprised of two services, the Django backend and the Vue.js SPA frontend. For development, both must be running simultaneously on the default 8000 & 8080 ports, respectively.

### In the root directory, create a virtualenv for Python.
```
python -m venv venv
```

### Activate the newly created venv.
```
. venv/bin/activate
```

### Install required python packages.
```
pip install -r requirements.txt
```

### Start up Django server on default port, 8000.
```
python manage.py runserver
```

## Navigate to the `spoonguru_frontend_v2` directory in a new terminal and proceed with the following commands to get the Vue.js frontend installed and running.

## Project setup
```
npm install
```

### Compiles and hot-reloads for development on default port, 8080.
```
npm run serve
```

Proceed to http://localhost:8080 to use the Vue.js SPA.