import os
import base64
import pandas as pd
import warnings
from tkinter import *
from datetime import datetime
from tkinter import messagebox

folder = os.path.abspath(os.getcwd())
extensions = ('.pdf','.PDF','.docx','.DOCX','.png','.jpg')

from pathlib import Path
home_dir = Path.home()
fileDB = (f'{ home_dir }\\Textile Sourcing Company S.A.C\\Soporte TI - General\\BD\\DB_TI.xlsx')
filemovile = (f'{ home_dir }\\Textile Sourcing Company S.A.C\\Soporte TI - General\\Inventario_Equipos\\Equipos_Moviles\\Inventario_Equipos_Movil.xlsx')
filelaptop = (f'{ home_dir }\\Textile Sourcing Company S.A.C\\Soporte TI - General\\Inventario_Equipos\\Equipos_de_Computo\\Inventario_Equipos_Computo.xlsx')
fecha_actual = datetime.now().strftime("%d-%m-%Y")

for x in os.listdir(folder):
    if x.endswith(extensions):
        
        filepath = os.path.splitext(os.path.basename(x))[0]
        print(filepath)

        if len(filepath) < 10:
            warnings.simplefilter(action='ignore', category=UserWarning)
            data = pd.read_excel(filemovile,skiprows=1, sheet_name="TRX_LINEA_TSC")
            df = pd.DataFrame(data)
            movilenumber = int(filepath)
            columnas = ['N° LINEA', 'N° DNI', 'USUARIO', 'AREA', 'GERENCIA', 'SEDE']
            
            def buscar():
                info = df[df['N° LINEA']==movilenumber]
                return(info)
            df_seleccionados = buscar()[columnas]

            for index, row in df_seleccionados.iterrows():
                os.rename(folder + '//' + filepath + '.pdf', folder + '//' + str(int(row['N° LINEA']))
                + ' - ' + str(int(row['N° DNI']))
                + ' - ' + str.upper((row['USUARIO']))
                + ' - ' + str.upper((row['AREA']))
                + ' - ' + str.upper((row['GERENCIA']))
                + ' - ' + str(fecha_actual)
                + ' - ' + str.upper((row['SEDE'].rstrip())) +'.pdf')
        else:
            continue
