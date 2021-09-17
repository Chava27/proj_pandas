import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#importar tabla de excel
tabla=pd.read_excel("fiestas_data.xlsx")

#Generar subtablas Monterrey
tablaMonterrey=tabla.groupby('zona_invitado').get_group('Monterrey')

#kmeans Brandy
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

ax=plt.subplot(221)

Data={'x':tablaMes2_mty, 'y': tablaMonterrey['cantidad_invitados']}

df = pd.DataFrame(Data, columns = ['x','y'])

#print(df)

plt.xlabel("MES")
plt.ylabel("INVITADOS")
plt.title("INVITADOS VS MES")

plt.scatter (df['x'], df['y'])

kmeans = KMeans(n_clusters=4).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

ax=plt.subplot(222)

plt.xlabel("MES")
plt.ylabel("INVITADOS")
plt.title("INVITADOS VS MES")

plt.scatter(df['x'], df['y'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:,0],centroids[:,1],c="red",s=50)

#Kmeans Chavy
ax=plt.subplot(223)

Data2={'x':tabla['cantidad_invitados'],'y': tabla['total_comida']}
df2=pd.DataFrame(Data2,columns=['x','y'])

plt.xlabel("INVITADOS")
plt.ylabel("COMIDA")
plt.title("INVITADOS VS COMIDA")

plt.scatter(df2['x'],df2['y'])

kmeans=KMeans(n_clusters=3).fit(df2)
centroids=kmeans.cluster_centers_
print(centroids)

ax=plt.subplot(224)

plt.xlabel("INVITADOS")
plt.ylabel("COMIDA")
plt.title("INVITADOS VS COMIDA")

plt.scatter(df2['x'],df2['y'],c=kmeans.labels_.astype(float), s=50,alpha=0.5)
plt.scatter(centroids[:,0],centroids[:,1],c='red',s=50)

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
plt.show()

#Kmeans Royi

#se genera un data frame con el costo total de la fiesta 
df3 = pd.DataFrame(tablaMonterrey, columns = ['cantidad_invitados','total_fiesta'])

#genera 4 clusters acorde a los valores de df para definir los centroides
kmeans = KMeans(n_clusters=4).fit(df3)
centroids = kmeans.cluster_centers_
print(centroids)

plt.xlabel("INVITADOS")
plt.ylabel("PRECIO TOTAL")
plt.title("PRECIO TOTAL DE LA FIESTA")

#dibuja la gràfica con los puntos del nùmero de invitados contra el costo total
plt.scatter(df3['cantidad_invitados'], df3['total_fiesta'],c=kmeans.labels_.astype(float),s=50,alpha=0.5)
plt.scatter(centroids[:,0],centroids[:,1],c="red",s=50)

plt.show()


