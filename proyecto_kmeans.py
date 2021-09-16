#16-09-2021
#Parte de Roy

#imports de librerias
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Lectura de la tabla
tabla=pd.read_excel("fiestas_data.xlsx")

#generar subtabla con datos de Monterrey
tablaMonterrey=tabla.groupby('zona_invitado').get_group('Monterrey')

#se genera un data frame con el costo total de la fiesta 
df = pd.DataFrame(tablaMonterrey, columns = ['total_fiesta','cantidad_invitados'])

#genera 4 clusters acorde a los valores de df para definir los centroides
kmeans = KMeans(n_clusters=4).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

#dibuja la gràfica con los puntos del nùmero de invitados contra el costo total
plt.scatter(df['cantidad_invitados'], df['total_fiesta'],c=kmeans.labels_.astype(float),s=50,alpha=0.5)
plt.scatter(centroids[:,0],centroids[:,1],c="red",s=50)
plt.show()
