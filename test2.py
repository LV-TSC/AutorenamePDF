import pyodbc

server = 'SRVAFL'
database = 'BDSYSTSC'
username = 'RPA'
password = '123qweASD!"#'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'


def buscar_datos(valor):
    try:
        with pyodbc.connect(connection_string) as conn:
            with conn.cursor() as cursor:
                query = '''select codigo_tsc, codigo_trabajador, nombres + ' ' + apellido_materno + ' ' + apellido_materno as 
                    Nombre_Completo, cargo_descripcion, area_descripcion, centro_costos_descripcion, descripcion_sede, activo_cesado from datos_trabajadores_tsc where codigo_trabajador = ?'''
                cursor.execute(query, (valor,))
                rows = cursor.fetchall()
                resultados = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
                return resultados
    except pyodbc.Error as e:
        print("Error al conectar a la base de datos o ejecutar la consulta: ", e)
        return []

valor_busqueda = '21887600'
resultados = buscar_datos(valor_busqueda)

fila_seleccionada = None

for resultado in resultados:
    if resultado.get('activo_cesado') == 'ACTIVO':
        fila_seleccionada = resultado
    else:
        fila_seleccionada = resultados[0]

if fila_seleccionada:
    nombre_completo = fila_seleccionada.get('Nombre_Completo')
    codigo_trabajador = fila_seleccionada.get('codigo_trabajador')
    activo_cesado = fila_seleccionada.get('activo_cesado')
    SEDE = fila_seleccionada.get('descripcion_sede')
    print(f"Nombre Completo: {nombre_completo}, {SEDE.rstrip()}, Código Trabajador: {codigo_trabajador} , {activo_cesado}")
else:
    print("No se encontraron resultados.")