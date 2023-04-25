from graficar import Graficar
import csv

class GraficarTercero(Graficar):
    def __init__(self, datos):
        super().__init__(datos)
    
    def generar_grafico(self):
        #Convertir los datos al formato requerido por la librería de terceros
        datos_csv = self.convertir_a_csv()
        
        #Utilizar la librería de terceros para generar el grafico
        Graficar.generar_grafico1(datos_csv)
        
    def convertir_a_csv(self):
        with open("covid_app\datos.csv", 'w', newline='') as f:
            writer = csv.writer(f)

            #La primera linea del archivo son los headers de los datos
            writer.writerow(['fecha_inicio', 'fecha_final', 'pais', 'contagios', 'muertes', 'pruebas'])

            #Se escriben los datos en el archivo
            for obj in self.datos:
                writer.writerow([obj[0], obj[1], obj[2], obj[3], obj[4], obj[5]])
        
        f.close()
        return "covid_app\datos.csv"