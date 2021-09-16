import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#importar tabla de excel
tabla=pd.read_excel("fiestas_data.xlsx")

#Generar subtablas Monterrey
tablaMonterrey=tabla.groupby('zona_invitado').get_group('Monterrey')
tablaMes_mty = tablaMonterrey['mes']
tablaMes2_mty = []

for i in tablaMes_mty:
    if i == 'Enero':
        tablaMes2_mty.append(1)
    elif i == 'Febrero':
        tablaMes2_mty.append(2)
    elif i == 'Marzo':
        tablaMes2_mty.append(3)
    elif i == 'Abril':
        tablaMes2_mty.append(4)
    elif i == 'Mayo':
        tablaMes2_mty.append(5)
    elif i == 'Junio':
        tablaMes2_mty.append(6)
    elif i == 'Julio':
        tablaMes2_mty.append(7)
    elif i == 'Agosto':
        tablaMes2_mty.append(8)
    elif i == 'Septiembre':
        tablaMes2_mty.append(9)
    elif i == 'Octubre':
        tablaMes2_mty.append(10)
    elif i == 'Noviembre':
        tablaMes2_mty.append(11)
    elif i == 'Diciembre':
        tablaMes2_mty.append(12)

Data={'x':tablaMonterrey['cantidad_invitados'], 'y': tablaMes2_mty}

df = pd.DataFrame(Data, columns = ['x','y'])

print(df)
plt.scatter (df['x'], df['y'])
plt.show()

kmeans = KMeans(n_clusters=7).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(df['x'], df['y'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:,0],centroids[:,1],c="red",s=50)
plt.show()
