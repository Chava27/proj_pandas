#Actividad Excel
#16-sep-2021
#IMPORTAR LIBRERIA PANDAS
import pandas as pd
#IMPORTAR LIBRERIA MATPLOIT
import matplotlib.pyplot as plt
#IMPORTAR NUMPY
import numpy as np
#IMPORTAR XLRD
import xlrd
import dataframe
import sklearn

#importar tabla de excel
tabla=pd.read_excel("fiestas_data.xlsx")

#generar subtablas Monterrey
tablaMonterrey=tabla.groupby('zona_invitado').get_group('Monterrey')
lista_salones_mty=tablaMonterrey['salon']
print("El salon mas utlizado en Monterrey es:",lista_salones_mty.max(),"\n")
lista_cuotas_mty=tablaMonterrey['couta_salon']
print("La media de rangos de cuotas en Monterrey es de",np.mean(lista_cuotas_mty),"\n")
print("La desviación estándar de cuotas en Monterrey es de",np.std(lista_cuotas_mty),"\n")

#graficar
ax=plt.subplot(111)
x=lista_salones_mty
y=lista_cuotas_mty
plt.xlabel("SALONES")
plt.ylabel("Cuotas")
plt.title("Precio de Salones MTY")
#definir valores
plt.bar(x,y,color='tab:blue')
labels=ax.get_xticklabels()
plt.setp(labels,rotation=45,horizontalalignment='right')
plt.show()
