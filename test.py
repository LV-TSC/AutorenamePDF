import os
import glob
import pyodbc
import time
from datetime import date
from datetime import timedelta
import subprocess
from pathlib import Path
from sys import exit

def crearconexion():
    global conexion
    direccion_servidor = 'SRVAFL'
    nombre_bd = 'BDSYSTSC'
    nombre_usuario = 'sa'
    password = 'scr20.$ab'
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    except Exception as e:
        print("Ocurrió un error al conectar a SQL Server: ", e)

dnib = 75922175

try:
    crearconexion()
    try:
        with conexion.cursor() as cursor:
            consulta = '''select codigo_tsc, codigo_trabajador, nombres + ' ' + apellido_materno + ' ' + apellido_materno as Nombre_Completo, 
                cargo_descripcion, area_descripcion, centro_costos_descripcion, descripcion_sede, activo_cesado from datos_trabajadores_tsc where codigo_trabajador = ?'''
            cursor.execute(consulta, dnib)
            resultado = conexion.commit()
            print(resultado)
            print("HECHO")
    except Exception as e:
        print(e)

except Exception as e:
    print(e)

finally:
    conexion.close()
    exit()
        