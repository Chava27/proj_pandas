#Actividad Excel
#16-sep-2021
#IMPORTAR LIBRERIA PANDAS
import pandas as pd
#IMPORTAR LIBRERIA MATPLOIT
import matplotlib.pyplot as plt
#IMPORTAR NUMPY
import numpy as np

#importar tabla de excel
tabla=pd.read_excel("fiestas_data.xlsx")

#generar subtablas Monterrey
tablaMonterrey=tabla.groupby('zona_invitado').get_group('Monterrey')
lista_salones_mty=tablaMonterrey['salon']
lista_cuotas_mty=tablaMonterrey['couta_salon']
lista_mes_mty = tablaMonterrey["mes"]
lista_invitados_mty = tablaMonterrey["cantidad_invitados"]
lista_atendientes_mty = tablaMonterrey["num_atendientes"]
lista_platillo_mty = tablaMonterrey["platillo"]
lista_precioPlatillo_mty = tablaMonterrey["precio_platillo"]
lista_show_mty = tablaMonterrey["show"]
lista_precioShow_mty = tablaMonterrey["precio_show"]

#Imprimiendo valores estadisticos
print("El salon mas utlizado en Monterrey es:",lista_salones_mty.max(),"\n")
print("La media de rangos de cuotas en Monterrey es de",np.mean(lista_cuotas_mty),"\n")
print("La desviación estándar de cuotas en Monterrey es de",np.std(lista_cuotas_mty),"\n")

#grafica de cuotas
ax=plt.subplot(222)
x=lista_salones_mty
y=lista_cuotas_mty
plt.xlabel("SALONES")
plt.ylabel("Cuotas")
plt.title("Precio de Salones MTY")
#definir valores
plt.bar(x,y,color='tab:blue')
labels=ax.get_xticklabels()
plt.setp(labels,rotation=45,horizontalalignment='right')

#Grafica de invitados
ax2 = plt.subplot(221)
x2 = lista_mes_mty
y2 = lista_invitados_mty

plt.xlabel("MESES")
plt.ylabel("INVITADOS")
plt.title("INVITADOS VS MESES")

plt.bar(x2,y2, color="blue")
labels= ax2.get_xticklabels()
plt.setp(labels,rotation=45, horizontalalignment="right")

#Grafica de platillos
ax3 = plt.subplot(223)
x3 = lista_platillo_mty
y3 = lista_precioPlatillo_mty

plt.xlabel("PLATILLOS")
plt.ylabel("PRECIO")
plt.title("PRECIO POR PLATILLO")

plt.bar(x3,y3, color="y")
labels= ax3.get_xticklabels()
plt.setp(labels,rotation=45, horizontalalignment="right")

#Grafica de shows
ax4 = plt.subplot(224)
x4 = lista_show_mty
y4 = lista_precioShow_mty

plt.xlabel("SHOW")
plt.ylabel("PRECIO")
plt.title("PRECIO POR SHOW")

plt.bar(x4,y4, color="green")
labels= ax4.get_xticklabels()
plt.setp(labels,rotation=45, horizontalalignment="right")

plt.show()
