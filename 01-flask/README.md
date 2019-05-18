# APP Flask Básica

## Crear entorno virtual

python3 -m venv venv

    si no funciona: apt-get install python3-venv

## Activar entorno virtual e instalar Flask

source venv/bin/activate

(venv)$ pip3 install flask

(venv)$ pip3 list

## Estrucutura APP

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