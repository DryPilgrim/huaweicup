# coding:gbk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('./data/mushrooms.csv')
print(df.head())

X = df.drop('class', axis=1)
y = df['class']
y = y.map({'p': 'Posionous', 'e': 'Edible'})

cat_cols= X.select_dtypes(include='object').columns.tolist()
print('X.columns.values.tolist():\n',X.columns.values.tolist())
for col in cat_cols:
    print(f" col name : {col}, N Unique : {X[col].nunique()}")

for col in cat_cols:
    X[col]=X[col].astype("category")
    X[col]=X[col].cat.codes
print(X.head())


#----------------------PCA降维可视化------------------------ 

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

X_std = StandardScaler().fit_transform(X)
X_pca = PCA(n_components=2).fit_transform(X_std)
X_pca = np.vstack((X_pca.T, y)).T

df_pca = pd.DataFrame(X_pca, columns=['1st_Component','2nd_Component', 'class'])
print(df_pca.head())

plt.figure(figsize=(8, 8))
sns.scatterplot(data=df_pca, hue='class', x='1st_Component', y='2nd_Component')
plt.show()

#----------------------t-SNE降维可视化------------------------  

from sklearn.manifold import TSNE

tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X_std)
X_tsne_data = np.vstack((X_tsne.T, y)).T
df_tsne = pd.DataFrame(X_tsne_data, columns=['Dim1', 'Dim2', 'class'])
print(df_tsne.head())

plt.figure(figsize=(8, 8))
sns.scatterplot(data=df_tsne, hue='class', x='Dim1', y='Dim2')
plt.show()