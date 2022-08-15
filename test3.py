import os
import base64
import pandas as pd
import warnings
from tkinter import *
from tkinter import messagebox

folder = os.path.abspath(os.getcwd())
extensions = ('.pdf','.PDF','.docx','.DOCX','.png','.jpg')

from pathlib import Path
home_dir = Path.home()
fileDB = (f'{ home_dir }\\Textile Sourcing Company S.A.C\\Soporte TI - General\\BD\\DB_TI.xlsx')
filemovile = (f'{ home_dir }\\Textile Sourcing Company S.A.C\\Soporte TI - General\\Inventario_Equipos\\Equipos_Moviles\\Inventario_Equipos_Movil.xlsx')
filelaptop = (f'{ home_dir }\\Textile Sourcing Company S.A.C\\Soporte TI - General\\Inventario_Equipos\\Equipos_de_Computo\\Inventario_Equipos_Computo.xlsx')

for x in os.listdir(folder):
    if x.endswith(extensions):
        
        filepath = os.path.splitext(os.path.basename(x))[0]
        print(filepath)

        if len(filepath) < 13:
            warnings.simplefilter(action='ignore', category=UserWarning)
            data = pd.read_excel(filelaptop,skiprows=1, sheet_name="Inventario_General")
            df = pd.DataFrame(data)
            laptopnumber = str(filepath)
            columnas = ['Host', 'DNI', 'Colaborador', 'Área', 'Sede', 'SN']
            
            def buscar():
                info = df[df['Host']==laptopnumber]
                return(info)
            df_seleccionados = buscar()[columnas]

            for index, row in df_seleccionados.iterrows():
                os.rename(folder + '//' + filepath + '.pdf', folder + '//' + str(row['Host'])
                + ' - ' + str(int(row['DNI']))
                + ' - ' + str.upper((row['Colaborador']))
                + ' - ' + str.upper((row['Área']))
                + ' - ' + str.upper((row['Sede']))
                + ' - ' + str.upper((row['SN'])) +'.pdf')
        else:
            continue
