import os
import base64
import pandas as pd
import warnings
from tkinter import *
from tkinter import messagebox

folder = "C:\\TSC\\Data\\Escaner"
print(folder)
extensions = ('.pdf','.PDF','.docx','.DOCX','.png','.jpg')

from pathlib import Path
home_dir = Path.home()
print(home_dir)
#fileDB = (f'{ home_dir }\\Textile Sourcing Company S.A.C\\Soporte TI - General\\BD\\DB_TI.xlsx')
filemovile = (f'{ home_dir }\\Textile Sourcing Company S.A.C\\Soporte TI - General\\Inventario_Equipos\\Equipos_Moviles\\Inventario_Equipos_Movil.xlsx')
filelaptop = (f'{ home_dir }\\Textile Sourcing Company S.A.C\\Soporte TI - General\\Inventario_Equipos\\Equipos_de_Computo\\Inventario_Equipos_Computo.xlsx')

fileDB = """C:\\Users\\lvivanco\\Textile Sourcing Company S.A.C\\Soporte TI - General\\BD\\DB_TI.xlsx"""
try:
    for x in os.listdir(folder):
        if x.endswith(extensions):
            
            filepath = os.path.splitext(os.path.basename(x))[0]
            print(filepath)
            if len(filepath) < 10:
                print("INICIO DNI")
                data = pd.read_excel(fileDB, sheet_name="TB_EMPLEADO")
                print(data)
                df = pd.DataFrame(data)
                dnib = int(filepath)
                print(df)
                columnas = ['DNI', 'DESC_USUARIO', 'AREA_GDH', 'GERENCIA', 'SEDE']
                print("Paso 2") 
                def buscar():
                    info = df[df['DNI']==dnib]
                    return(info)
                print("paso 3")
                df_seleccionados = buscar()[columnas]
                
                for index, row in df_seleccionados.iterrows():
                    os.rename(folder + '//' + filepath + '.pdf', folder + '//' + str(row['DNI'])
                    + ' - ' + str.upper((row['DESC_USUARIO']))
                    + ' - ' + str.upper((row['AREA_GDH']))
                    + ' - ' + str.upper((row['GERENCIA']))
                    + ' - ' + str.upper((row['SEDE'])) +'.pdf')
            else:
                continue

        messagebox.showinfo("Aviso","Se renombraron los archivos por DNI")

except Exception as e:
    messagebox.showerror("Error","No se encuentra el DNI")
