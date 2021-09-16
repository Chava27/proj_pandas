#16-09-2021

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#importar tabla de excel
tabla=pd.read_excel("fiestas_data.xlsx")

#Generar subtablas Monterrey
tablaMonterrey=tabla.groupby('zona_invitado').get_group('Monterrey')
#print(tablaMonterrey)
listaInvitados_mty=


