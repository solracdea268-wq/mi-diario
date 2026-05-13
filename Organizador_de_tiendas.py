import os
import json
from datetime import datetime
class Usuario:
    def __init__(self, archivo):
        self.archivo = archivo
        self.usuarios = cargar_datos(archivo)
    def ingreso_al_sistema(self):
        encontrado = False
        contra = False
        usuario_ingresado = input("Ingrese su nombre de usuario:\n    > > >  ")
        for diccionario in self.usuarios:
            if diccionario["usuario"] == usuario_ingresado:
                encontrado = True
                contra_dada = input("Ingrese su contraseña:\n       > > > ")
                if contra_dada == diccionario['clave']:
                        print("Se logro ingresar al sistema, Bienvenido...")
                        contra = True
        if encontrado and contra:
            print(f"BIENVENIDO: {usuario_ingresado}")
            return True
        elif encontrado and not contra:
            print("Contrasena incorrecta...")
            return False
        else:
            print("Usuario incorrecto...")
            return False
    def crear_usario(self):
        diccionario = {}
        diccionario['usuario'] = input("Ingrese el nombre de usuario:\n       > > >  ")
        diccionario['clave'] = input("Ingrese su nueva contrasenia:\n       > > >  ")
        self.usuarios.append(diccionario)
        escribir(self.archivo, self.usuarios)
class MenuProductos:
    def __init__(self, archivo):
        self.archivo = archivo
        self.lista = cargar_datos(self.archivo)
    def agregar_producto(self):
        diccionario = {}
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = float(input("Ingrese el precio del producto: "))
        stock_producto = int(input("Ingrese la cantidad de stock del producto: "))
        diccionario["nombre"] = nombre_producto
        diccionario["precio"] = precio_producto
        diccionario["stock"] = stock_producto
        self.lista.append(diccionario)
        print(f"El producto: {diccionario['nombre']} fue agregado con exito!! ")
        with open(self.archivo, "w") as arch:
            json.dump(self.lista, arch, indent=4,ensure_ascii=False)
    def ver_productos(self):
        if os.path.exists(self.archivo) and os.path.getsize(self.archivo) > 2:
            print("NOMBRE | PRECIO | STOCK")
            for indice, diccionario in enumerate(self.lista, start=1):
                print(f"{indice}. {diccionario['nombre']} | {diccionario['precio']} | {diccionario['stock']}")
        else: print("No hay productos disponibles...")
    def editar_precio(self):
        
        indice_elegido = int(input("Ingrese el indice del producto que desea cambiar el precio: "))
        encontrado = False
        if 0 < indice_elegido <= len(self.lista):
            for indice, dic in enumerate(self.lista):
                if indice == indice_elegido-1:
                    precio_nuevo = float(input("Ingrese el nuevo precio del producto:"))
                    self.lista[indice]["precio"] = precio_nuevo
                    encontrado = True
                    print(f"Precio del producto {self.lista[indice]['nombre']} cambiado con exito a {self.lista[indice]['precio']}")
        else: print("Indice invalido...")
        if encontrado:
            escribir(self.archivo, self.lista)
        if not encontrado:
            print("No se encontro el indice del producto...")
    def eliminar_producto(self):
        indice_elegido = int(input("Ingrese el indice del producto que quiere eliminar: "))
        encontrado = False
        for indice, dic in enumerate(self.lista):
            if indice == indice_elegido-1:
                print(f"Producto: {self.lista[indice]['nombre']} eliminado con exito!!")
                del self.lista[indice]
                encontrado = True
        if encontrado:
            with open(self.archivo, "w" ) as arch:
                json.dump(self.lista,arch,indent=4, ensure_ascii=False)
        if not encontrado:
            print("No se encontro el indice del producto...")
class MenuVentas:
    def __init__(self, archivo, archivo_producto):
        self.archivo = archivo
        self.archivo_producto = archivo_producto
        self.lista_ventas = cargar_datos(self.archivo)
        self.lista_productos = cargar_datos(self.archivo_producto)

    def vender_producto(self):
        indice_producto = int(input("Ingrese el indice del producto que desea vender: "))
        encontrado = False
      #  if 0 < indice_producto <= len(self.lista_productos):
        for indice, dic in enumerate(self.lista_productos):
            if indice == indice_producto-1:
                cant_vender = int(input("Ingrese la cantidad de ventas: "))
                if cant_vender <= self.lista_productos[indice]['stock']:
                    precio = float(self.lista_productos[indice]['precio'] * cant_vender)
                    producto_nombre = self.lista_productos[indice]['nombre']
                    self.lista_productos[indice]['stock'] -= cant_vender
                    encontrado = True
                    print(f"-----VENDIDO-----\nProducto: {self.lista_productos[indice]['nombre']}\nCantidad: {cant_vender}\nPrecio total: {precio} ")
                else:
                    print("Stock insuficiente...")
     #   else: print("Indice invalido...")
        if encontrado:               
             tiempo = datetime.now()
             dia = tiempo.day
             mes = tiempo.month
             diccionario = {}
             diccionario["producto"] = producto_nombre
             diccionario["cantidad"] = cant_vender
             diccionario["total"] = precio
             diccionario["tiempo"] = f"{dia}/{mes}/{gestion}"
             diccionario['hora'] = f"{tiempo.hour}:{tiempo.minute}:{tiempo.second}"
             self.lista_ventas.append(diccionario)
             escribir(self.archivo, self.lista_ventas)
             escribir(self.archivo_producto, self.lista_productos)
    def reportes(self):
        if os.path.exists(self.archivo) and os.path.getsize(self.archivo) > 2:
            print("-------REPORTES------")
            print("Producto | Cantidad | Precio total | Dia\n")
            precio_total = 0
            for indice, venta in enumerate(self.lista_ventas, start=1):
                print(f"{indice}. {venta['producto']} | {venta['cantidad']} unidades | {venta['total']} bs | dia: {venta['tiempo']}   | Hora: {venta['hora']}")    
                precio_total += venta['total']
            print(f"------------------\nPrecio total ganado: {precio_total}\n------------------")
            mayor_item = max(cargar_datos(ruta_vent), key=lambda x: x['cantidad'])
            print(f"El producto mas vendido es {mayor_item['producto']}")
        else: print("No hay ventas registradas")
def cargar_datos(ruta):
    if not os.path.exists(ruta):
        with open(ruta, "w") as f:
            json.dump([], f)
    with open(ruta, "r") as f:
        return json.load(f)
def escribir(ruta, que_escribir):
    with open(ruta, "w") as w:
        return json.dump(que_escribir, w, indent=4)
ruta_prod =  "organizador_de_tiendas_produtos.json"
ruta_vent =  "organizador_de_tiendas_ventas.json"
ruta_user = "organizador_de_tiendas_usuarios.json"
def tiempo():
    hoy = datetime.now()
    return hoy
gestion = 26
main_productos = MenuProductos(ruta_prod)
main_ventas = MenuVentas(ruta_vent, ruta_prod)
usuario1 = Usuario(ruta_user)
try:
    usuario1.crear_usario()
    print("BIENVENIDO!\nTiene 3 intentos para ingresar su usuario")
    intentos = 3
    entrada = False
    while intentos > 0:
        entrada = usuario1.ingreso_al_sistema()
        intentos -= 1
        if entrada:
            break
        else:
            print(f"Le quedan: {intentos} intentos...")
    while entrada:
        opcion_elegida = int(input("------MENU------\n1. Productos\n2. Vender\n3. Ver Reportes\n4. Salir\n  > > > "))
        if opcion_elegida == 1:
            opcion_producto = int(input("-----PRODUCTOS----\n1. Agregar Producto\n2. Ver Productos\n3. Editar Precio\n4. Eliminar Producto\n   > > > "))
            if opcion_producto == 1:
                main_productos.agregar_producto()
            elif opcion_producto == 2:
                main_productos.ver_productos()
            elif opcion_producto == 3:
                main_productos.ver_productos()
                main_productos.editar_precio()
            elif opcion_producto == 4 :
                main_productos.ver_productos()
                main_productos.eliminar_producto()
        if opcion_elegida == 2:
            main_productos.ver_productos()
            main_ventas.vender_producto()
        if opcion_elegida == 3:
            main_ventas.reportes()
        elif opcion_elegida == 4:
            break
except (ValueError,IndexError): print("Error, ingrese los datos correctamente...")