import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#importar tabla de excel
tabla=pd.read_excel("fiestas_data.xlsx")

#Generar subtablas Monterrey
tablaMonterrey=tabla.groupby('zona_invitado').get_group('Monterrey')

df = pd.DataFrame(tablaMonterrey, columns = ['cantidad_invitados','mes'])

print(df)
plt.scatter (df['cantidad_invitados'],df['mes'])
plt.show()

kmeans = KMeans(n_cluster=3).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(df['cantidad_invitados'],df['mes'].c=kmeans.labels_.astype(float),s=50,alpha=0.5)
plt.scatter(centroids[:,0],centroids[:,1],c="red",s=50)
plt.show()
