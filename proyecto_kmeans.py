#16-09-2021

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Hola
tabla=pd.read_excel("fiestas_data.xlsx")

#generar subtablas Monterrey
tablaMonterrey=tabla.groupby('zona_invitado').get_group('Monterrey')

df = pd.DataFrame(tablaMonterrey, columns = ['total_fiesta','cantidad_invitados'])

print (df)
plt.scatter (df['cantidad_invitados'],df['total_fiesta'])
plt.show()

kmeans = KMeans(n_clusters=4).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(df['cantidad_invitados'], df['total_fiesta'],c=kmeans.labels_.astype(float),s=50,alpha=0.5)
plt.scatter(centroids[:,0],centroids[:,1],c="red",s=50)
plt.show()
