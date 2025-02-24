import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
import seaborn as sns
import textwrap
import missingno as msno
from sklearn.decomposition import PCA,KernelPCA
from sklearn.manifold import MDS,TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
# import prince
# from yellowbrick.cluster import KElbowVisualizer
from pathlib import Path

work_dir = Path.cwd() 

os.chdir(f"{work_dir}/data/raw")

dforg = pd.read_csv('Encuesta_organizacional_2023.csv')
dfper = pd.read_csv('Encuesta_personas_2023.csv')

per = pd.read_excel('Diccionario_datos.xlsx','Preguntas - EP',usecols=['Enunciado Pregunta','Categoria','Serial Code'])
org = pd.read_excel('Diccionario_datos.xlsx','Preguntas - EO',usecols=['Enunciado Pregunta','Categoria','Serial Code'])
org = org.iloc[0:136]

per.columns = ['pregunta','categoria','code']
org.columns = ['pregunta','categoria','code']

per['code'] = per['code'].str.lower()
org['code'] = org['code'].str.lower()

dfper = dfper[dfper['ip_002'].notnull()].reset_index(drop=True).copy()

acoso_tecnico = [col for col in dfper.columns if 'at_' in col]
dfper['Acoso_Tecnico'] = dfper[acoso_tecnico].apply(lambda row: 1 if any(row == 'Sí, me ha pasado.') else 0, axis=1)

testigos_tecnicos = [col for col in dfper.columns if 'tt_' in col]
dfper['Testigo_Tecnico'] = dfper[testigos_tecnicos].apply(lambda row: 1 if any(row == 'Sí, he sido testigo.') else 0, axis=1)

dfper['Acoso_Declarado'] = dfper[['ad_001','ad_014']].apply(lambda row: 1 if any(row == 'Sí, me ha pasado.') else 0, axis=1)

dfper['Testigo_Declarado'] = dfper[['td_001']].apply(lambda row: 1 if any(row == 'Sí, he sido testigo de hostigamiento o acoso sexual.') else 0, axis=1)

acoso_total = [col for col in dfper.columns if 'Acoso' in col]
dfper['Acoso_Total'] = dfper[acoso_total].apply(lambda row: 1 if any(row == 1) else 0, axis=1)

testigo_total = [col for col in dfper.columns if 'Testigo' in col]
dfper['Testigo_Total'] = dfper[testigo_total].apply(lambda row: 1 if any(row == 1) else 0, axis=1)

dfper['target'] = dfper['Acoso_Total']+dfper['Testigo_Total']

exec(open(f"{work_dir}/src/perfiles_expuestos_pipeline.py").read())

exec(open(f"{work_dir}/src/perfiles_no_expuestos_pipeline.py").read())
