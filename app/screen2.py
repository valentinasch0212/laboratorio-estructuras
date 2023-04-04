#datos estadísticos, los que ustedes quieran....
#en general son bastante fáciles de hacer, solo es seguir ciertas fórmulas

#mediana, media, desviación estandar, etc...
#hagan varias funciones sobre eso.

#-------------------------------------------
#las gráficas si me toca a mi del lado del cliente porque ahí es donde se grafica xd


#Moda, media, mediana y valores máximos y mínimos de las listas usadas
import statistics
import eel
import screen1 

@eel.expose
def moda(lista):
    mode=statistics.mode(lista)
    return mode
@eel.expose
def mediana(lista):
    median=statistics.median(lista)
    return median
@eel.expose
def media(lista):
    mean=statistics.mean(lista)
    return mean
@eel.expose
def maximo(lista):
    maximum=max(lista)
    return maximum
@eel.expose
def minimo(lista):
    minimum=min(lista)
    return minimum




