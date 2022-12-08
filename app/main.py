from fastapi import FastAPI
import pandas as pd
from collections import Counter
from operator import itemgetter

df_Films = pd.read_csv('Datasets_creados/Films.csv')
app = FastAPI()

#este es un mensaje de bienvenida a la API
@app.get('/')
def mensaje():
    mensaje = 'Bienvenido a la API creada por Marín Eluney Gómez Piñeiro. donde se podran hacer consultas a un dataframe que contiene datos sobre las series  y peliculas publicadas en las plataformas Disney Plus, Amazon Prime, Netflix y Hulu'
    return mensaje

@app.get('/get_max_duration/')
async def Max_tiemp_x_film_y_año (año:int, plataforma:str, tipo:str):

    #filtro en duracion por los que contienen 'min'
    df_max_temp = df_Films[df_Films.duration.str.contains(tipo)]

    #filtro por plataforma
    df_max_temp = df_max_temp[df_max_temp['Plataform'] == plataforma]

    #filtro por año
    df_max_temp = df_max_temp[df_max_temp['release_year'] == año]

    #quito min de la columna duration
    df_max_temp['duration'] = df_max_temp['duration'].apply(lambda cant_film: cant_film.replace("min",""))
    df_max_temp['duration'] = df_max_temp['duration'].str.strip()

    #cambio el tipo de valores de la columna de obcant_x_platafet a int
    df_max_temp['duration'] = df_max_temp['duration'].astype(str).astype(int)

    #reordeno el dataframe
    df_max_temp = df_max_temp.sort_values('duration',ascending=False)
    df_max_temp = pd.DataFrame(df_max_temp)
    df_max_temp = df_max_temp.drop(['Id','director','cast','country','date_added','release_year','rating','duration','listed_in','description','Plataform',	'Unnamed: 0', 'type'], axis = 1)
    
    #filtrom la promera fila
    return df_max_temp.head(1)
    

@app.get('/get_count_plataform/')
def cantidad_film (plataforma:str):
    #Filramos ppr plataforma
    x = df_Films[df_Films['Plataform'] == plataforma]

    #filtramos por tipo de film y creamos un dataframe para cada tipo 
    x_Movie = x[x['type']=='Movie']
    x_show = x[x['type']=='TV Show']
    
    #contamos las columnas
    Movie = x_Movie.shape[0]
    TVShow = x_show.shape[0]

    #Creamos un nuevo Dataframe
    cant_x_plataf = pd.DataFrame()
    cant_x_plataf['Plataform'] = None
    cant_x_plataf['Movie'] = None
    cant_x_plataf['TV Show'] = None
    
    #insertamos en las filas el numero de columnas del Dataframe de cada tipo de film 
    nueva_fila = pd.Series([plataforma, Movie, TVShow], index=cant_x_plataf.columns)
    cant_x_plataf = cant_x_plataf.append(nueva_fila, ignore_index=True)
    
    return cant_x_plataf

@app.get ('/get_listedin')
def top_genero (genero:str):
    #Filtro por las filas de 'listed_in' que contengan el genero ingresado
    top_genero = df_Films[df_Films.listed_in.str.contains(genero)]

    #creo un dataframe para cada plataforma filtrada
    top_genero_Amazon = top_genero[top_genero['Plataform'] == 'Amazon Prime']
    top_genero_Disney = top_genero[top_genero['Plataform'] == 'Disney Plus']
    top_genero_Netflix = top_genero[top_genero['Plataform'] == 'Netflix']
    top_genero_Hulu = top_genero[top_genero['Plataform'] == 'Hulu']

    #cuento las columnas de todos los dataframes
    genero_Amazon = top_genero_Amazon.shape[0]
    genero_Disney = top_genero_Disney.shape[0]
    genero_Hulu = top_genero_Hulu.shape[0]
    genero_Netflix = top_genero_Netflix.shape[0]

    #creo un nuevo dataframe
    df_genero = pd.DataFrame()
    df_genero['Plataform'] = None
    df_genero['Cantidad'] = None

    #inserto en las filas el numero de columnas de cada dataframe
    nueva_fila = pd.Series(['Amazon', genero_Amazon], index=df_genero.columns)
    nueva_fila2 = pd.Series(['Disney', genero_Disney], index=df_genero.columns)
    nueva_fila3 = pd.Series(['Netflix', genero_Netflix], index=df_genero.columns)
    nueva_fila4 = pd.Series(['Hulu', genero_Hulu], index=df_genero.columns)

    df_genero =df_genero.append(nueva_fila, ignore_index=True)
    df_genero =df_genero.append(nueva_fila2, ignore_index=True)
    df_genero =df_genero.append(nueva_fila3, ignore_index=True)
    df_genero =df_genero.append(nueva_fila4, ignore_index=True)
    
    #reordeno de forma descendente el dataframe
    df_genero = df_genero.sort_values('Cantidad', ascending=False)
    
    #solicito que me retornen solo la primera fila, que corresponde al valor mas alto
    return df_genero.head(1)

@app.get('/get_actor')
def actor_mas_actuo (plataforma:str, año:int):
    #filtramos pro plataforma y por año
    actor = df_Films[df_Films['Plataform'] == plataforma]
    actor = actor[actor['release_year'] == año]

    #eliminamos columnas que no necesitamos
    df_prov = actor.drop(['Id','title','director', 'country','date_added', 'rating','duration','description','type', 'Unnamed: 0'], axis = 1)

    #Filtramos la columna cast, para que sea desigual a 'no info'
    df_prov = df_prov[df_prov['cast'] != 'No info']

     #creamos una lista provicional, donde metemos los actores en la columna cast separados por coma
    df_prov = df_prov['cast'].str.split(', ').to_list()

    #creamos una lista para eliminar la lista de listas
    lista_actores = []
    for item in df_prov:

        lista_actores += item

    #Ahora contamos las veces en que aparece un actor y lo metemos en 'contador'
    contador = Counter(lista_actores)

    #ordenamos 'contador' de forma descendente
    contador = sorted(contador.items(), key = itemgetter(1), reverse = True)

    mas_actuo = contador[0]
    #convertimos mas_actuo a una lista
    mas_actuo = list(mas_actuo)
    
    #creamos un nuevo dataframe con los valores solicitados
    df_actor = pd.DataFrame()

    #Cramos variables para luego insertarlas en las filas
    actores = mas_actuo[0]
    cantidad = mas_actuo[1]

    #Creamos las comlumnas
    df_actor['plataform'] = None
    df_actor['actores'] = None
    df_actor['cantidad'] = None
    
    #insertamos las variables en las filas
    nueva_fila = pd.Series([plataforma, actores, cantidad], index=df_actor.columns) 
    df_actor = df_actor.append(nueva_fila, ignore_index=True)


    return df_actor
