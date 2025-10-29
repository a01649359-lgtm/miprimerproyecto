import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='whitegrid')

#Cargar el archivo spotify en pandas
file_path="C:\VALENTINA\ICT\Codigo_semanatec2_analisisdatos/spotify.csv"
df = pd.read_csv(file_path, encoding='latin1')

#Leer el archivo
#Imprime las informacion importante a cada operación 
print(f"Info del DataFrame")
print(df.info())
print("\n ")

#Imprime solo las primeras 5 filas
print("Primeras filas del DataFrame")
print(df.head())
print("\n ")

# Valores nulos por columna
print("Valores nulos por columna:")
valores_nulos = df.isnull().sum()
print(valores_nulos)
print("\n ")

#Estadísticas descriptivas de todas las columnas numéricas
print(f"DF describe: medidas estádisticas del DataFrame")
print(df.describe())
print("\n ")

#Columnas disponibles
print(f"Filas y columnas del DataFrame")
print(df.shape)
print("\n ")


#Funciones para recolectar algunas informaciónes
def top_artists(df, n=10 ):
    return df['artists'].value_counts().head(n)


def most_popular_songs(df, n=10):
    return df[['track_name','artists','popularity']].sort_values(by='popularity',ascending=False).head(n)

def longest_songs(df,n=5):
    canciones_largas=df.sort_values(by='duration_ms', ascending=False)
    return canciones_largas[['track_name','artists','duration_ms']].head(n)

def most_popular_genre (df):
    conteo_generos=df['track_genre'].value_counts()
    genero_mas_popular=conteo_generos.idxmax()
    cantidad_canciones_genero=conteo_generos.max()
    print(f"El más popular es: {genero_mas_popular} con {cantidad_canciones_genero} canciones.")
    return conteo_generos.head(5)

#Impresion de las funciones
#Top 10 artistas
print("El top 10 artistas más escuchados en Spotify es: ")
print(top_artists(df))
print("\n ")
 
#Top 10 canciones más escuchadas
print("El top 10 canciones más escuchadas en Spotify es:")
print(most_popular_songs(df))
print("\n ")

#Las 5 canciones más largas
print("Las 5 canciones más largas en Spotify son:")
print(longest_songs(df))
print("\n ")

#Los generos más escuchados 
print("Los generos más escuchados en Spotify son:")
print(most_popular_genre(df))
print("\n ")


#Calculo media, mediana y desvicación estándar de c/variable solo numericas
print("Media de cada variable:")
print(df.mean(numeric_only=True))
print("\n ")

print("Mediana de cada variable:")
print(df.median(numeric_only=True))
print("\n ")

print("Desviación estándar de cada variable:")
print(df.std(numeric_only=True))
print("\n ")




