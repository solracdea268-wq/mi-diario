import json
from datetime import datetime
import os
#import pandas as pd
#import matplotlib.pyplot as plt
class Menu:
    def __init__(self, ruta):
        self.ruta = ruta #Leer el archivo .json para las funciones
        self.datos = leer_archivo(ruta)  # funciones .py
    def ver_gastos(self):
        if os.path.getsize(self.ruta) > 2:
            indice = 0
            print("=========== G A S T O S ===========")
            print("   EN QUE | FECHA | FECHA REGISTRADA | GASTADO POR | GASTO")
            for indice ,dicc in enumerate(self.datos):
                indice += 1
                print(f"{indice}. {dicc['en que']} | {dicc['fecha dia']}/{dicc['fecha mes']}/26 | {dicc['fecha registrada']} | {dicc['gastado por']} | {dicc['gasto']} bs")
            print("====================================")
    def agregar_gasto(self):
        diccionario = {}
        en_que = input("Ingrese en que se uso el gasto:\n      > > > ").capitalize()
        fecha_dia = int(input("Ingrese la fecha del dia del gasto:\n      > > > "))
        fecha_mes = int(input("Ingrese la fecha del mes del gasto:\n      > > > "))
        gastado_por = input("Ingrese el nombre de la persona que hizo el gasto:\n      > > > ").capitalize()
        monto  = int(input("Ingrese el monto del gasto:\n      > > > "))
        tiempo = datetime.now()
        fecha_de_subida = tiempo.strftime("%A, %d de %B")
        diccionario['en que'] = en_que
        diccionario['fecha dia'] = fecha_dia
        diccionario['fecha mes'] = fecha_mes
        diccionario['fecha registrada'] = fecha_de_subida
        diccionario['gastado por'] = gastado_por
        diccionario['gasto'] = monto
        self.datos.append(diccionario)
        print(f"Gasto : {diccionario['en que']} agregado con exito!! \n")
        guarda_archivo(self.ruta, self.datos)
    def ver_reportes(self):
        gasto_total = 0
        for dicc in self.datos:
            gasto_total += dicc['gasto']
        print(f"========= GASTOS TOTOALES: {gasto_total} Bs ============")
        mayor_item = max(self.datos, key=lambda x: x['gasto'])
        print(f"El gasto mayor es {mayor_item['en que']} con {mayor_item['gasto']} Bs")
    def filtrar_gasto_mes(self):
        mes_dado = input("Ingrese el numero de mes que desea filtrar:\n      > > > ")
        lista_mes = []
        encontrado = False
        for dicc in self.datos:
            if dicc['fecha mes'] == mes_dado:
                lista_mes.append(dicc)
                encontrado = True
        if encontrado:
            print(f"=========== G A S T O S del mes: {mes_dado} ===========")
            print("   EN QUE | FECHA | FECHA REGISTRADA | GASTADO POR | GASTO")
            gasto_total = 0
            for i, dicc in enumerate(lista_mes):
                i += 1
                gasto_total += dicc['gasto']
                print(f"{i}. {dicc['en que']} | {dicc['fecha dia']}/{dicc['fecha mes']}/26 | {dicc['fecha registrada']} | {dicc['gastado por']} | {dicc['gasto']} bs")
            print(f"========= GASTOS TOTALES del mes: {gasto_total} Bs ============\n")
        else: print("No se encontro el mes o no hay gastos...")
    def filtrar_gasto_dia(self):
        dia_dado = input("Ingrese el numero de dia que desea filtrar:\n      > > > ")
        lista_dia = []
        encontrado = False
        for dicc in self.datos:
            if dicc['fecha dia'] == dia_dado:
                lista_dia.append(dicc)
                encontrado = True
        if encontrado:
            print(f"=========== G A S T O S del dia: {dia_dado} ===========")
            print("   EN QUE | FECHA | FECHA REGISTRADA | GASTADO POR | GASTO")
            gasto_total = 0
            for i, dicc in enumerate(lista_dia):
                i += 1
                gasto_total += dicc['gasto']
                print(f"{i}. {dicc['en que']} | {dicc['fecha dia']}/{dicc['fecha mes']}/26 | {dicc['fecha registrada']} | {dicc['gastado por']} | {dicc['gasto']} bs")
            print(f"========= GASTOS TOTALES del mes: {gasto_total} Bs ============\n")
        else: print("No se encontro el dia o no hay gastos...")
    def editar_gasto(self):
        indice_dado = int(input("Ingrese el indice del gasto que desea modificar:\n    > > > "))
        encontrado = False
        for indice, dicc in enumerate(self.datos,start=1):
            if indice == indice_dado:
                encontrado = True
        if encontrado:
            nuevo_gasto = int(input("Ingrese el nuevo monto:\n          > > > "))
            self.datos[indice_dado-1]['gasto'] = nuevo_gasto
            self.datos[indice_dado-1]['fecha registrada'] = fecha()
            guarda_archivo(self.ruta, self.datos)
            print(f"Gasto: {nuevo_gasto} a {self.datos[indice_dado-1]['en que']} editado con exito")
        else: print("No se encontro el gasto...")
    def ver_grafica(self):
        if not self.datos:
            print("NO hay datos para graaficar...")
        else:
            lista_gasto = []
            lista_fecha = []
            for gasto in self.datos:
                lista_gasto.append(gasto['gasto'])
                # Combinamos fecha y concepto para el eje X
                fecha = f"{gasto['fecha dia']}/{gasto['fecha mes']}/26\n{gasto['en que']}"
                lista_fecha.append(fecha)

            # 2. Configuración de la figura (Fondo claro y tamaño)
            plt.figure(figsize=(12, 6), facecolor='#FDFDFD')
            ax = plt.axes()
            ax.set_facecolor('#FDFDFD')

            # 3. Crear barras con un color azul acero moderno
            barras = ax.bar(lista_fecha, lista_gasto, color='#5DADE2', width=0.6)

            # 4. Añadir etiquetas de valor sobre cada barra
            for barra in barras:
                yval = barra.get_height()
                ax.text(barra.get_x() + barra.get_width()/2, yval + 0.5, 
                        f'Bs. {yval}', ha='center', va='bottom', 
                        fontsize=10, fontweight='bold', color='#2E4053')

            # 5. Títulos y etiquetas estéticas
            plt.title('Reporte de Gastos Detallado', fontsize=16, fontweight='bold', 
                      pad=20, loc='left', color='#283747')
            plt.ylabel('Monto gastado', fontsize=11, color='#566573')

            # 6. Limpieza de bordes (Spines)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_color('#D5DBDB')
            ax.spines['bottom'].set_color('#D5DBDB')

            # 7. Cuadrícula horizontal sutil
            ax.yaxis.grid(True, linestyle='--', alpha=0.5, color='#BDC3C7')
            ax.set_axisbelow(True)
            # Ajuste automático y guardado
            plt.tight_layout()
            plt.savefig('gastitos.png', dpi=300) # dpi=300 para mayor resolución
            plt.close() # Es buena práctica cerrar la figura después de guardar
            print("Imagen guardada con éxito (gastitos.png).")
    def buscar_gastos(self):
        if not self.datos:
            print("NO hay dastos que buscar...")
            return
        else:
            en_que = input("Ingrese en que se hizo el gasto: \n                 > > > ")
            lista_encontrada = []
            encontrado = False
            for dicc in self.datos:
                if dicc['en que'].lower() == en_que.lower():
                    lista_encontrada.append(dicc)
                    encontrado = True
            if encontrado:
                for i, dicc in enumerate(lista_encontrada, start=1):
                    print(f"{i}. {dicc['en que']} | {dicc['fecha dia']}/{dicc['fecha mes']}/26 | {dicc['fecha registrada']} | {dicc['gastado por']} | {dicc['gasto']} bs")
            else: print("No se encontro el objeto...")
def leer_archivo(ruta):
    if not os.path.exists(ruta):
        with open(ruta, 'w') as f:
            json.dump([], f)
    with open(ruta, "r") as archivo:
        return json.load(archivo)
def guarda_archivo(ruta, datos):
    with open(ruta, "w") as f:
        json.dump(datos,f,indent=4, ensure_ascii=False)
def fecha():
        tiempo = datetime.now()
        fecha_de_subida = tiempo.strftime("%A, %d de %B")
        return fecha_de_subida
#def guardar_datos_excel(ruta_del_excel):
 #   datos = leer_archivo(ruta1)
  #  df = pd.DataFrame(datos)
   # resumen_de_persona = df.groupby("gastado por")['gasto'].sum()
    #resumen_de_persona.to_excel(ruta_del_excel)
    #print("Guarado")
ruta1 = "Control_de_Gastos/control_de_gastos.json"
main1 = Menu(ruta1)
ruta_execel = "Control_de_gastos.xlsx"
try:
    while True:
        print("======= M E N U ======")
        opcion = int(input("1. Ver Gastos\n2. Agregar Gastos\n3. Reportes\n4. Filtrar Por Mes\n5. Filtrar por dia\n6. Editar Gastos\n7. Ver Grafica de Gastos\n8. Buscar Gastos\n9. Abrir Excel\n       > > > "))
        if opcion ==1 :
            main1.ver_gastos()
            main1.ver_reportes()
        elif opcion == 2:
            main1.agregar_gasto()
        elif opcion ==3:
            main1.ver_reportes()
        elif opcion == 4:
            main1.filtrar_gasto_mes()
        elif opcion == 5:
            main1.filtrar_gasto_dia()
        elif opcion == 6:
            main1.ver_gastos()
            main1.editar_gasto()
        elif opcion == 7:
             main1.ver_grafica()
        elif opcion == 8:
            main1.buscar_gastos()
        elif opcion == 9:
            guardar_datos_excel(ruta_execel)
        else: break
except (ValueError, IndentationError): print("ERROR Ingrese lo valores adecuadamente...")