import subprocess
import time

def ejecutar_comando(comando):
    """Ejecuta un comando del sistema y devuelve el resultado."""
    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        print(f"Ejecutando: {comando}")
        print(f"Salida:\n{resultado.stdout}")
        if resultado.stderr:
            print(f"Error:\n{resultado.stderr}")
        return resultado.stdout
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el comando {comando}: {e}")
        return None

def obtener_nombre_adaptador():
    """Obtiene el nombre del adaptador WiFi."""
    salida = ejecutar_comando("netsh interface show interface")
    if salida:
        lineas = salida.splitlines()
        for linea in lineas:
            if "Wi-Fi" in linea or "Wireless" in linea:
                partes = linea.split()
                nombre_adaptador = partes[-1]
                print(f"Nombre del adaptador encontrado: {nombre_adaptador}")
                return nombre_adaptador
    print("No se encontró un adaptador WiFi.")
    return None

def desactivar_wifi(nombre_adaptador):
    """Desactiva el adaptador WiFi."""
    if nombre_adaptador:
        ejecutar_comando(f"netsh interface set interface \"{nombre_adaptador}\" admin=disable")
        print("WiFi desactivado.")
        time.sleep(5)  # Espera 5 segundos antes de reactivar

def activar_wifi(nombre_adaptador):
    """Activa el adaptador WiFi."""
    if nombre_adaptador:
        ejecutar_comando(f"netsh interface set interface \"{nombre_adaptador}\" admin=enable")
        print("WiFi activado.")
        time.sleep(5)  # Espera 5 segundos para asegurar que se haya activado correctamente

def resolver_problemas():
    """Ejecuta comandos de resolución de problemas."""
    ejecutar_comando("ipconfig /release")
    time.sleep(5)  # Espera 5 segundos entre comandos
    ejecutar_comando("ipconfig /renew")
    time.sleep(5)
    ejecutar_comando("ipconfig /flushdns")
    print("Comandos de resolución de problemas ejecutados.")

def main():
    print("Inicio del proceso de resolución de problemas de WiFi.")
    nombre_adaptador = obtener_nombre_adaptador()
    if nombre_adaptador:
        desactivar_wifi(nombre_adaptador)
        activar_wifi(nombre_adaptador)
        #resolver_problemas()
        print("Proceso completado. Verifica tu conexión a Internet.")
    else:
        print("No se pudo encontrar el adaptador WiFi. Verifica manualmente el nombre del adaptador.")

if __name__ == "__main__":
    main()