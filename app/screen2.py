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


modapeaton=moda(screen1.Peaton)
medianapeaton=mediana(screen1.Peaton)
mediapeaton=media(screen1.Peaton)
maxpeaton=maximo(screen1.Peaton)
minpeaton=minimo(screen1.Peaton)

modaautomovil=moda(screen1.Automovil)
medianaautomovil=mediana(screen1.Automovil)
mediaautomovil=media(screen1.Automovil)
maxautomovil=maximo(screen1.Automovil)
minautomovil=minimo(screen1.Automovil)


modacampaero=moda(screen1.Campaero)
medianacampaero=mediana(screen1.Campaero)
mediacampaero=media(screen1.Campaero)
maxcampaero=maximo(screen1.Campaero)
mincampaero=minimo(screen1.Campaero)

modacamioneta=moda(screen1.Camioneta)
medianacamioneta=mediana(screen1.Camioneta)
mediacamioneta=media(screen1.Camioneta)
maxcamioneta=maximo(screen1.Camioneta)
mincamioneta=minimo(screen1.Camioneta)

modamicro=moda(screen1.Micro)
medianamicro=mediana(screen1.Micro)
mediamicro=media(screen1.Micro)
maxmicro=maximo(screen1.Micro)
minmicro=minimo(screen1.Micro)

modabuseta=moda(screen1.Buseta)
medianabuseta=mediana(screen1.Buseta)
mediabuseta=media(screen1.Buseta)
maxbuseta=maximo(screen1.Buseta)
minabuseta=minimo(screen1.Buseta)

modabus=moda(screen1.Bus)
medianbus=mediana(screen1.Bus)
mediabus=media(screen1.Bus)
maxbus=maximo(screen1.Bus)
minbus=minimo(screen1.Bus)

modacamion=moda(screen1.Camion)
medianacamion=mediana(screen1.Camion)
mediacamion=media(screen1.Camion)
maxcamion=maximo(screen1.Camion)
mincamion=minimo(screen1.Camion)

modavolqueta=moda(screen1.Volqueta)
medianvolqueta=mediana(screen1.Volqueta)
mediavolqueta=media(screen1.Volqueta)
maxvolqueta=maximo(screen1.Volqueta)
minvolqueta=minimo(screen1.Volqueta)

modamoto=moda(screen1.Moto)
medianamoto=mediana(screen1.Moto)
mediamoto=media(screen1.Moto)
maxmoto=maximo(screen1.Moto)
minmoto=minimo(screen1.Moto)

modabicicleta=moda(screen1.Bicicleta)
medianabicicleta=mediana(screen1.Bicicleta)
mediabicicleta=media(screen1.Bicicleta)
maxbicicleta=maximo(screen1.Bicicleta)
minabicicleta=minimo(screen1.Bicicleta)

modadiurnio_nocturno=moda(screen1.Diurnio_Nocturno)
modagravedad=moda(screen1.Gravedad)

#BTW solo se calcula la moda de las listas de Diurnio/Nocturno y gravedad porque son listas que no contienen
#datos númericos para hacer los otros cálculos como media, mediana, etc.

