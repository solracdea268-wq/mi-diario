# git add .
# git commit -m "LO Q SE HIZO EXPLICACION"
# git push
from datetime import datetime
import os
import json
#import matplotlib.pyplot as plt
class Menu:
    def __init__(self, archivo_json):
        self.datos = leer_archivo(archivo_json)
        self.arch_json = archivo_json
    def escribir(self):
        print("Escribe un tema del dia:")
        diccionario = {}
        diccionario['titulo'] = input("Ingrese el titulo:\n     > > >   ")
        diccionario['contenido'] = input("Ingrese el contenido:\n            > > > ")
        dia = fecha().day
        mes = fecha().month
        gestion = fecha().year
        hora = fecha().hour
        minuto = fecha().minute
        segundos = fecha().second
        diccionario["nombre del dia"] = fecha().strftime("%A")
        diccionario['fecha'] = f"{dia}/{mes}/{gestion}" 
        diccionario['hora'] = f"{hora}:{minuto}:{segundos}"  # SE PUDO AHORRAR LINEAS DE CODIGO
        opcion = int(input("Ingrese en quee parte va la nota:\n1. Estudios\n2.Social\n3. Ambos\n                    > > >   "))
        if opcion == 2:
            diccionario['1 al 10 social'] = float(input("Ingrese como le fue del 1 al 10 socialmente:\n             >  > >   "))
            diccionario['etiqueta'] = "Estudios"
            puntaje = diccionario["1 al 10 social"]
            if puntaje >= 9:
                diccionario["estado del dia"] = "Excelente"
            elif puntaje >= 6:
                diccionario["estado del dia"] = "Bien"
            elif puntaje >= 4:
                diccionario["estado del dia"] = "Regular"
            else:
                diccionario["estado del dia"] = "Muy mal"
        elif opcion == 1:
            diccionario['1 al 10 estudios'] = float(input("Ingrese como le fue del 1 al 10 en los estudios:\n             >  > >   "))
            diccionario['etiqueta'] = "Social"
            puntaje = diccionario["1 al 10 estudios"]
            if puntaje >= 9:
                diccionario["estado del dia"] = "Excelente"
            elif puntaje >= 6:
                diccionario["estado del dia"] = "Bien"
            elif puntaje >= 4:
                diccionario["estado del dia"] = "Regular"
            else:
                diccionario["estado del dia"] = "Muy mal"
        elif opcion == 3:
            diccionario["1 al 10 estudios y social"] = float(input("Ingrese como le fue del 1 al 10:\n                > > >  "))
            diccionario['etiqueta'] = "Social","Estudios"
            puntaje = diccionario["1 al 10 estudios y social"]
            if puntaje >= 9:
                diccionario["estado del dia"] = "Excelente"
            elif puntaje >= 6:
                diccionario["estado del dia"] = "Bien"
            elif puntaje >= 4:
                diccionario["estado del dia"] = "Regular"
            else:
                diccionario["estado del dia"] = "Muy mal"
        opcion_imp = int(input("Ingrese que tan importante fue el evento:\n1. Demsiado Importante\n2. Muy Importante\n3. Algo Importante\n4. Poco Importante\n5. Nada importante:\n           > > >   "))
        if opcion_imp == 1: diccionario['importancia'] = "Demasiado Importante"
        elif opcion_imp == 1: diccionario['importancia'] = "Muy Importante"
        elif opcion_imp == 1: diccionario['importancia'] = "Algo Importante"
        elif opcion_imp == 1: diccionario['importancia'] = "Poco Importante"
        elif opcion_imp == 1: diccionario['importancia'] = "Nada Importante"
        diccionario['notas extras']= input("Ingrese notas extras:\n               > > >   ")
        self.datos.append(diccionario)
        escribir_arch(self.arch_json, self.datos)
        print("Se guuardo correctamente...")
    def ver_contenido_general(self):
        if combrobar_arch(self.arch_json) <= 10:
            print("No hay datos...")
            return False
        else:
            print(f"==== MIS NOTAS ====")
            for i, dicc in enumerate(self.datos, start=1):
                print(f"{i}. {dicc['fecha']}    |   {dicc['titulo']}")
            return True
    def ver_contenido_detallado(self):
        if self.ver_contenido_general() == False:
            print("No se puede ver contenido porq no hay....")
        else:
            opcion = int(input("Ingrese el indice del cual quiere ver el titulo:\n         > > >  "))
            for indice, dicc in enumerate(self.datos, start=1):
                if opcion == indice:
                    print(f"===== DETALLES {dicc['fecha']} '{dicc['titulo']}' =====\nTitulo:         {dicc['titulo']}\nContenido:      {dicc['contenido']}\nFecha:          {dicc['fecha']}\nHora:           {dicc['hora']}\nNombre del dia: {dicc['nombre del dia']}\nEtiqueta:       {dicc['etiqueta']}\nImportancia:    {dicc['importancia']}\nNotas Extras:   {dicc['notas extras']}\nEstado del dia: {dicc['estado del dia']}")
    #def ver_grafica(self):
    def eliminar_exto(self):
        indice_dado = int(input("Ingrese el indice a eliminar:\n          > > >  "))
        for indice, dicc in enumerate(self.datos, start=1):
            if indice == indice_dado:
                del self.datos[indice-1]
                print("SE ELIMINO CORRECTAMENTE...")
                escribir_arch(self.arch_json, self.datos)
def leer_archivo(ruta):
    with open(ruta, "r") as r:
        datos = json.load(r)
    return datos
def fecha():
    fecha = datetime.now()
    return fecha
def combrobar_arch(ruta):
    return os.path.getsize(ruta)
def escribir_arch(ruta, cont):
    with open(ruta,"w")as w:
        return json.dump(cont, w,indent=4)
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
ruta = "diario/diario.json"
main1 = Menu(ruta)
while True:
    print("===== MENU =====")
    opcion_elegida = int(input("1. Ver contenido General\n2. Ver Contenido Detallado\n3. Escribir Contenido\n4. Eiminar Texto\n5. Salir\n            > > >  "))
    if opcion_elegida ==1:
        main1.ver_contenido_general()
    elif opcion_elegida == 2:
        main1.ver_contenido_general()
        main1.ver_contenido_detallado()
    elif opcion_elegida == 3:
        main1.escribir()
    elif opcion_elegida == 4:
        main1.ver_contenido_general()
        main1.eliminar_exto()
    elif opcion_elegida == 5:
        break
    else: print("Ingrese solo numeros del 1 al 4...")
# PRUEBA SI SAE EN GITHUUB   HOLAAAAAAAAAAA