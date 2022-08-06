import os
import base64
import pandas as pd
from tkinter import *
from tkinter import messagebox
import warnings

folder = ("C:\TSC\Escaner")
extensions = ('.pdf', '.PDF','.docx', '.jpg')

from pathlib import Path
home_dir = Path.home()
fileDB = (f'{ home_dir }\\Textile Sourcing Company S.A.C\\Soporte TI - General\\BD\\DB_TI.xlsx')
filemovile = ('C:\\TSC\\BD\\Inventario_Equipos_Movil.xlsx')
filelaptop = ('C:\\TSC\\BD\\Inventario_Equipos_Computo.xlsx')

try:
    for x in os.listdir(folder):
        if x.endswith(extensions):
            
            filepath = os.path.splitext(os.path.basename(x))[0]

            if len(filepath) < 15:
                print("INICIO")
                warnings.simplefilter(action='ignore', category=UserWarning)
                data = pd.read_excel(filelaptop,skiprows=1, sheet_name="Inventario - Laptop")
                df = pd.DataFrame(data)
                laptopnumber = str(filepath)
                columnas = ['Host', 'DNI', 'Personal', 'Área', 'Sede', 'SN']
                
                print("BUSCAR")
                def buscar():
                    info = df[df['Host']==laptopnumber]
                    return(info)

                df_seleccionados = buscar()[columnas]

                print("RENOMBRAR")
                for index, row in df_seleccionados.iterrows():
                    os.rename(folder + '//' + filepath + '.pdf', folder + '//' + str(row['Host'])
                    + ' - ' + str(int(row['DNI']))
                    + ' - ' + str.upper((row['Personal']))
                    + ' - ' + str.upper((row['Área']))
                    + ' - ' + str.upper((row['Sede']))
                    + ' - ' + str.upper((row['SN'])) +'.pdf')
            else:
                continue

    messagebox.showinfo("Aviso","Se termino de renombrar los archivos")

except Exception as e:
    messagebox.showerror("Error","No se encuentra DNI")