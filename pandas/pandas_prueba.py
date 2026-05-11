import pandas as pd
nombres = ["Lunes", "Martes", "Miercoles","Jueves", "Viernes", "Sabado", "Domingo"]
datos = [1,2,3,4,5,6,7]
dt = pd.DataFrame(nombres,datos)
print(dt)