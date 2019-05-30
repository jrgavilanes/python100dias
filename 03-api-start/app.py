import json
from typing import List

from apistar import App, Route, types, validators
from apistar.http import JSONResponse

# Helpers

def _carga_datos():
    with open('data.json') as f:
        colegas = json.loads(f.read())
        return {colega["id"]: colega for colega in colegas}

colegas = _carga_datos()

VALID_COMPANIES = set(colega["company"] for colega in colegas.values())
CAR_NOT_FOUND = 'Colega no encontrado'

# import pdb; pdb.set_trace()