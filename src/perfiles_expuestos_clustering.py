# %%
# scaler = StandardScaler()
scaler = joblib.load(f'{work_dir}/outputs/models/standard_scaler_expuestos.pkl')

df_cols = pd.read_csv(f'{work_dir}/configs/orden_columnas_scaler_expuestos.csv',header=0)
columnas_nombres = list(df_cols['variables'].values)

df_scaled1 = scaler.transform(df_tmp1[columnas_nombres])

print('lectura y transformacion de expuestos OK')

# %%
# kpca = KernelPCA(n_components=2, kernel='cosine', gamma=0.1,random_state=0)
# X_kpca = kpca.fit_transform(df_scaled1)

# plt.figure(figsize=(8, 6))
# plt.scatter(X_kpca[:, 0], X_kpca[:, 1])
# plt.title("Kernel PCA with Cosine Kernel")
# plt.xlabel('1st component')
# plt.ylabel('2nd component')
# plt.show()

# %%
# pca = PCA(n_components=2,random_state=0)
# df_pca = pca.fit_transform(df_scaled1)
# df_pca = pd.DataFrame(data=df_pca, columns=['PC1', 'PC2'])

# plt.figure(figsize=(8, 6))
# sns.scatterplot(x='PC1', y='PC2', data=df_pca)
# # plt.title('PCA scatter plot')
# plt.xlabel('1st component', fontsize=16)
# plt.ylabel('2nd component', fontsize=16)
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)
# plt.show()

# %%
# pca = PCA(random_state=0)
# pca.fit(df_scaled1)

# plt.figure(figsize=(10,8))
# plt.plot(np.cumsum(pca.explained_variance_ratio_))
# plt.xlabel('Número de Componentes')
# plt.ylabel('Varianza Explicada Acumulada')
# plt.grid(True)
# plt.show()

# %%
# kpca = KernelPCA(n_components=100, kernel='cosine', gamma=0.1,random_state=0)
kpca = joblib.load(f'{work_dir}/outputs/models/kernelpca_expuestos.pkl')

df_pca = kpca.transform(df_scaled1)

# %%
from sklearn.mixture import GaussianMixture

# %%
# gmm = GaussianMixture(random_state=0,n_components=3)
gmm = joblib.load(f'{work_dir}/outputs/models/gmm_model_expuestos.pkl')

cluster_labels = gmm.predict(df_pca)
plt.scatter(df_pca[:, 0], df_pca[:, 1], c=cluster_labels, cmap='plasma')
plt.show()

print('importacion de algoritos de kpca y gmm successfull')

# %% [markdown]
# # Calculando clusters

# %%
# n_components = np.arange(1, 11)

# # %%
# aic_values = []
# bic_values = []

# # Ajustar el modelo y calcular AIC/BIC para cada número de clústeres
# for n in n_components:
#     gmm = GaussianMixture(n_components=n, random_state=42)
#     gmm.fit(df_pca)
#     aic_values.append(gmm.aic(df_pca))
#     bic_values.append(gmm.bic(df_pca))

# # %%
# plt.figure(figsize=(8, 4))
# plt.plot(n_components, aic_values, label='AIC', marker='o')
# plt.plot(n_components, bic_values, label='BIC', marker='o')
# plt.xlabel('Número de Clústeres')
# plt.ylabel('Puntaje')
# plt.legend()
# plt.title('AIC y BIC para determinar el número óptimo de clústeres')
# plt.show()

# # %%
# log_likelihoods = []

# # Calcular log-likelihood para cada número de clústeres
# for n in n_components:
#     gmm = GaussianMixture(n_components=n, random_state=42)
#     gmm.fit(df_pca)
#     log_likelihoods.append(gmm.score(df_pca))  # Promedio de log-likelihood

# # Graficar la log-likelihood
# plt.figure(figsize=(8, 4))
# plt.plot(n_components, log_likelihoods, marker='o')
# plt.xlabel('Número de Clústeres')
# plt.ylabel('Log-Likelihood')
# plt.title('Curva de Log-Likelihood para determinar el número óptimo de clústeres')
# plt.show()

# %%
df_rev1 = dfper[dfper['target'].isin([1,2])].copy()

# %%
df_rev1['segmento'] = cluster_labels

# print('Dataframe con segmentos de perfiles expuestos')
# print(df_rev1.head())

df_rev1.to_csv(f'{work_dir}/data/processed/segmentos_expuestos.csv')

# %%
# df_rev1['segmento'].value_counts()

# %%
plt.pie(df_rev1['segmento'].value_counts().values,labels=df_rev1['segmento'].value_counts().index)
plt.show()
# %% [markdown]
# # Graficando resultados

# %%
