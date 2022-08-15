import os
import base64
import pandas as pd
import warnings
from tkinter import *
from tkinter import messagebox
icon = \
"""
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
"""

icondata= base64.b64decode(icon)
tempFile= "icon.ico"
iconfile= open(tempFile,"wb")
iconfile.write(icondata)
iconfile.close()

root=Tk()
root.title("RenamePDF")
root.geometry("400x80")
root.resizable(False,False)

root.wm_iconbitmap(tempFile)
os.remove(tempFile)

miFrame=Frame(root)
miFrame.pack()

folder = os.path.abspath(os.getcwd())
extensions = ('.pdf','.PDF','.docx','.DOCX','.png','.jpg')

from pathlib import Path
home_dir = Path.home()
fileDB = (f'{ home_dir }\\Textile Sourcing Company S.A.C\\Soporte TI - General\\BD\\DB_TI.xlsx')
filemovile = (f'{ home_dir }\\Textile Sourcing Company S.A.C\\Soporte TI - General\\Inventario_Equipos\\Equipos_Moviles\\Inventario_Equipos_Movil.xlsx')
filelaptop = (f'{ home_dir }\\Textile Sourcing Company S.A.C\\Soporte TI - General\\Inventario_Equipos\\Equipos_de_Computo\\Inventario_Equipos_Computo.xlsx')

#Aplicacion
def autonameDNI():
    try:
        for x in os.listdir(folder):
            if x.endswith(extensions):
                
                filepath = os.path.splitext(os.path.basename(x))[0]
                print(filepath)

                if len(filepath) < 10:
                    data = pd.read_excel(fileDB, sheet_name="TB_EMPLEADO")
                    df = pd.DataFrame(data)
                    dnib = int(filepath)
                    columnas = ['DNI', 'DESC_USUARIO', 'AREA_GDH', 'GERENCIA', 'SEDE']
                    def buscar():
                        info = df[df['DNI']==dnib]
                        return(info)

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

def autonameMOVILE():
    try:
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
                        + ' - ' + str.upper((row['SEDE'])) +'.pdf')
                else:
                    continue

        messagebox.showinfo("Aviso","Se renombraron los archivos por Número de Teléfono")

    except Exception as e:
        messagebox.showerror("Error","No se encuentra el Número de Telefono")

def autonameLAPTOP():
    try:
        for x in os.listdir(folder):
            if x.endswith(extensions):
                
                filepath = os.path.splitext(os.path.basename(x))[0]
                print(filepath)

                if len(filepath) < 14:
                    warnings.simplefilter(action='ignore', category=UserWarning)
                    data = pd.read_excel(filelaptop,skiprows=1, sheet_name="Inventario - Laptop")
                    df = pd.DataFrame(data)
                    laptopnumber = str(filepath)
                    columnas = ['Host', 'DNI', 'Personal', 'Área', 'Sede', 'SN']
                    
                    def buscar():
                        info = df[df['Host']==laptopnumber]
                        return(info)
                    df_seleccionados = buscar()[columnas]

                    for index, row in df_seleccionados.iterrows():
                        os.rename(folder + '//' + filepath + '.pdf', folder + '//' + str(row['Host'])
                        + ' - ' + str(int(row['DNI']))
                        + ' - ' + str.upper((row['Personal']))
                        + ' - ' + str.upper((row['Área']))
                        + ' - ' + str.upper((row['Sede']))
                        + ' - ' + str.upper((row['SN'])) +'.pdf')
                else:
                    continue

        messagebox.showinfo("Aviso","Se renombraron los archivos por Número de Laptop")

    except Exception as e:
        messagebox.showerror("Error","No se encuentra el Número de Laptop")


def autonameNUEVOLAPTOP():
    try:
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

        messagebox.showinfo("Aviso","Se renombraron los archivos por Nuevo Número de Laptop")

    except Exception as e:
        messagebox.showerror("Error","No se encuentra el Número de Laptop")

#------------LABELS-----------#
mesagelabel=Label(miFrame, text="¿COMO DESEA BUSCAR LOS ARCHIVOS?")
mesagelabel.grid(row=0, column=1, padx=5, pady=5, sticky="nswe", columnspan=3)

#---------BOTONES----------#
miFrame2=Frame(root)
miFrame2.pack()

searchbutton=Button(miFrame2, width=11, text="N° DNI",command=autonameDNI)
searchbutton.grid(row=0,column=0, sticky="e", padx=5, pady=5)

createbutton=Button(miFrame2, width=11, text="N° CELULAR", command=autonameMOVILE)
createbutton.grid(row=0,column=1, sticky="e", padx=5, pady=5)

createbutton=Button(miFrame2, width=11, text="N° LAPTOP(A)", command=autonameLAPTOP)
createbutton.grid(row=0,column=2, sticky="e", padx=5, pady=5)

createbutton=Button(miFrame2, width=11, text="N° LAPTOP(N)", command=autonameNUEVOLAPTOP)
createbutton.grid(row=0,column=3, sticky="e", padx=5, pady=5)

root.mainloop()