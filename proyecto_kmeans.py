import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#importar tabla de excel
tabla=pd.read_excel("fiestas_data.xlsx")

#Generar subtablas Monterrey
tablaMonterrey=tabla.groupby('zona_invitado').get_group('Monterrey')
#print(tablaMonterrey)
listaInvitados_mty = tablaMonterrey["nombre_festejado"]
listaMes_mty = tablaMonterrey["mes"]

#print(listaInvitados_mty)
#print(listaMes_mty)

Data = ['x': listaInvitados,
        'y': listaMes_mty]


