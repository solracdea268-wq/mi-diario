import json
import os
from datetime import datetime
class Menu:
    def __init__(self, ruta_arch):
        self.datos = leer_archivo(ruta_arch)
        self.ruta_arch = ruta_arch
    def 
def leer_archivo(ruta):
    if comprobar_tamanioarch(ruta) <=10:
        with open(ruta, "w") as w:
            json.dump([], w)
        with open(ruta, "r") as r:
            return json.load(r)
    else:
        with open(ruta, "r") as r:
            return json.load(r)
def comprobar_tamanioarch(ruta):
    return os.path.getsize(ruta)
ruta_json = "libro/libros.json"
leer_archivo(ruta_json)