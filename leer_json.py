import json

def leer_json(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        datos_json = json.load(archivo)
        
    #Convertir los datos del formato JSON a lista

    return [(dato["fecha_inicio"], dato["fecha_final"], dato["pais"], dato["contagios"], dato["muertes"], dato["pruebas"]) for dato in datos_json]