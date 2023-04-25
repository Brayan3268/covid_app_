from graficar_tercero import GraficarTercero
from leer_json import leer_json

datos = leer_json("covid_app\json.json")
print(type(datos))

graficador_tercero = GraficarTercero(datos)

graficador_tercero.generar_grafico()