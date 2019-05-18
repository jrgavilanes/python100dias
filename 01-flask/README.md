# APP Flask Básica

## Crear entorno virtual

python3 -m venv venv

    si no funciona: apt-get install python3-venv

## Activar entorno virtual e instalar Flask

source venv/bin/activate

(venv)$ pip3 install flask

(venv)$ pip3 list

## Estructura APP

```bash
├── demo.py
├── program
│   ├── __init__.py
│   └── routes.py
└── venv
```

```python
# __init__.py
from flask import Flask

app = Flask(__name__)

from program import routes
```

```python
# routes.py
from program import app

@app.route('/')
@app.route('/index')
def index():
    return 'hola notas!'
```

```python
# demo.py
from program import app
```

## Ejecutar APP

(venv)$ export FLASK_APP=demo.py && flask run

## Examinar variables entorno

(venv)$ env | grep FLASK_APP en Linux

## Leer variables entorno desde archivo ( para facilitar desarrollo.)

```bash
(venv)$ pip3 install python-dotenv
(venv)$ echo "FLASK_APP=demo.py" > .flaskenv
(venv)$ flask run
```

## Plantillas HTML

```bash
├── demo.py
├── program
│   ├── __init__.py
│   ├── routes.py
│   └── templates
│       └── index.html
```

```python
# routes.py
from program import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
```

```html
# index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Plantilla</title>
</head>
<body>
    <p>Plantilla html</p>
</body>
</html>
```

## Con plantilla Base

```bash
├── demo.py
├── program
│   ├── __init__.py
│   ├── routes.py
│   └── templates
│       ├── base.html
│       └── index.html
```

```html
# base.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Plantilla</title>
</head>
<body>
    {% block content %} {% endblock %}  
</body>
</html>
```

```html
# index.html
{% extends "base.html" %}

{% block content %}

    <h1>Hola nano esto está heredado</h1>

{% endblock %}
```
