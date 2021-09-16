import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#importar tabla de excel
tabla=pd.read_excel("fiestas_data.xlsx")
tablaMonterrey=tabla.groupby('zona_invitado').get_group('Monterrey')
Data={'x':tabla['cantidad_invitados'],'y': tabla['total_comida']}
df=pd.DataFrame(Data,columns=['x','y'])
plt.scatter(df['x'],df['y'])
plt.show()

kmeans=KMeans(n_clusters=3).fit(df)
centroids=kmeans.cluster_centers_
print(centroids)

plt.scatter(df['x'],df['y'],c=kmeans.labels_.astype(float), s=50,alpha=0.5)
plt.scatter(centroids[:,0],centroids[:,1],c='red',s=50)
plt.show()