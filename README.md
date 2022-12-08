# DataScients_PI01
Este es un proyecto hecho por Martín Eluney Gómez Piñeiro, para el curso de Data Scients de Henry en la cohorte 5.
En este proyecto se me dieron las siguientes pautas a seguir:

## **Propuesta de trabajo**

El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente aplicar las transformaciones que consideren pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API deberán construirla en un entorno virtual dockerizado.

Los datos serán provistos en archivos de diferentes extensiones, como *csv* o *json*. Se espera que realicen un EDA para cada dataset y corrijan los tipos de datos, valores nulos y duplicados, entre otras tareas. Posteriormente, tendrán que relacionar los datasets así pueden acceder a su información por medio de consultas a la API.

Las consultas a realizar son:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año:
    El request debe ser: get_max_duration(año, plataforma, [min o season]).

+ Cantidad de películas y series (separado) por plataforma
    El request debe ser: get_count_plataform(plataforma).  
  
+ Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
    El request debe ser: get_listedin('genero').
    Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.

+ Actor que más se repite según plataforma y año.
  El request debe ser: get_actor(plataforma, año).

## **Pasos del proyecto**

1. Ingesta y normalización de datos.

2. Relacionar el conjunto de datos y crear la tabla necesaria para realizar consultas. Aquí se recomienda corroborar qué datos necesitarán en base a las consultas a realizar y concatenar las 4 tablas.

3. Leer documentación en links provistos e indagar sobre Uvicorn, FastAPI y Docker.

5. Crear la API en un entorno Docker → leer documentación en links provistos.

5. Realizar consultas solicitadas.

6. Realizar un video demostrativo.

7. **PLUS**: realizar un deployment en Mogenius .
  
  ## **Realizacion del Proyecto**
 **Limpieza de Datos**
 
 +  Primero lei los cuatro archivos suministrados con ayuda de Pandas y cree un dataframe para cada uno.
 
 +  Elimine los posibles duplicados de cada uno.
 
 +  Cree una columna para cada dataframe que dijese la plataforma a la que pertenecia cada pelicula o serie.
 
 +  Concatene los dataframes en uno solo.
 
 +  cree una nueva columna id.
  
 +  Elimine la columna id_show ya que tenia ids repetidas, por que originalmente pertenecio a 4 archivos diferentes.
  
 +  Contabilice los nulos y rastrie en que columnas se hallaban.
  
 +  Visualice los valores de cada columna mas repetidos, en busca de valores sin sentido.
  
 +  Reemplace los valores sin sentido por 'No info'.
  
 +  Reemplace los nulos poir 'No Info'.
   
 +  Exporte el dataframe como un nuevo csv.
 
 **Creacion de la API**
 
 +  Cree un archivo main.py donde importe la libreria de python FastAPI que me permitio crear la API.

 +  Cree 5 Querys (1 mensaje de bienvenida y 4 funciones).
 
 +  Corri la API.
 
 +  Comprobe el buen funcionamiento de la API.
 
 +  
 **Deployd en Docker**
 
 + Cree un archivos requirements.txt donde puse todas las librerias necesarias a instalar para el correcto funcionamiento de la API.
 
 + Cree una imagen de docker siguiendo el paso a paso puesto en el github https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
 
 + cree un container para la imagen siguiendo el mismo tutorial.
 
 + probe en correcto funcionamiento de la API en el container.





 
