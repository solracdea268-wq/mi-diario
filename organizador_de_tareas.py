import os
import json
class MenuDeTareas:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.lista_tareas = leer_archivo_json(nombre_archivo)
        self.tareas_no_completadas = []
        for tarea in self.lista_tareas:
            if tarea['completado'] == False:
                self.tareas_no_completadas.append(tarea)
        self.tareas_completadas= []
        for tarea in self.lista_tareas:
            if tarea['completado'] == True:
                    self.tareas_completadas.append(tarea)
    def ver_tareas(self):
        print("============== TAREAS ==========")
        print("   NOMBRE   |    IMPORTANCIA    |   FECHA DE PLAZO")
        for indice, tarea in enumerate(self.tareas_no_completadas, start=1):
            print(f"{indice}. {tarea['nombre']} | {tarea['nivel de importancia']}%   |  {tarea['dia de plazo']}/{tarea['mes del plazo']}/{gestion}   |     ")
        print('===================================')
    def agregar_tarea(self):
        print(os.path.abspath(self.nombre_archivo))
        nombre_tarea = input("Ingrese el nombre de la tarea:\n          > > >  ")
        importancia_de_tarea = int(input("Ingrese la importancia de la tarea del 1 al 100: \n         > > > "))
        dia_del_plazo = int(input("Ingrese el dia del plazo de la tarea:\n         > > > "))
        mes_del_plazo = int(input("Ingrese el mes del plazo de la tarea:\n         > > > "))
        diccionario = {}
        diccionario['nombre'] = nombre_tarea
        diccionario['nivel de importancia'] = importancia_de_tarea
        diccionario['dia de plazo'] = dia_del_plazo
        diccionario['mes del plazo'] = mes_del_plazo
        diccionario['completado'] = False
        self.lista_tareas.append(diccionario)
        escribir_algo(self.nombre_archivo, self.lista_tareas)
        print("Tarea Agregada con exitooo")
    def marcar_tarea_como_completada(self):
        indice = 0
        indice_elegido = int(input("Ingrese el indce q desea marcar: \n                  > > > "))
        for tarea in self.tareas_no_completadas:
            if indice_elegido == self.tareas_no_completadas[indice]:
                tarea['completado'] = True
                print(f"Se marco la tarea: {tarea['nombre']} como completada   ")
            indice += 1
def leer_archivo_json(ruta):
    if not os.path.exists(ruta):
        with open(ruta, 'w') as w:
          json.dump([], w)
          return []
    else:
        if os.path.getsize(ruta) <= 2: 
            with open(ruta, 'w') as w:
                json.dump([], w)
        with open(ruta, 'r') as r:
            datos = json.load(r)
            return datos
def escribir_algo(ruta, lista):
    with open(ruta,"w") as w:
        json.dump(lista, w, indent=4)
    return
gestion = 26
main1 = MenuDeTareas("organizador_de_tareas.json")
while True:
    opcion_eleegia = int(input("1. Ver Tareas\n2. Agregar Tarea\n3. Marcar Tarea como Completada\n                    > > > "))
    if opcion_eleegia == 1:
        main1.ver_tareas()
    elif opcion_eleegia == 2:
        main1.agregar_tarea()
    elif opcion_eleegia == 3:
        main1.ver_tareas()
        main1.marcar_tarea_como_completada()
    else: break