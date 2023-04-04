#getTable(start: int, end: int): int[][] -> obtener matriz que representa la tabla principal
#deleteRecord(orden: int): void -> eliminar registro
#addRecord(aquí irán las columnas que decidan que van a conformar la tabla principal): void -> Agregar registro
#Pendiente: 3.	Imprimir la información de un dato específico solicitado por el usuario (con la información relacionada de las listas)

#Recomiendo haber creado ya la tabla con las nuevas columnas, etc, etc, antes de comenzar a crear las funciones
import pandas as pd
import numpy as np
import eel
df=pd.read_csv('https://www.datos.gov.co/api/views/7cci-nqqb/rows.csv?accessType=DOWNLOAD')
#Variables independientes
Peaton= df['PEATON'].to_list()
Automovil=df['AUTOMOVIL'].to_list()
Campaero=df['CAMPAERO'].to_list()
Camioneta=df['CAMIONETA'].to_list()
Micro=df['MICRO'].to_list()
Buseta=df['BUSETA'].to_list()
Bus=df['BUS'].to_list()
Camion=df['CAMION'].to_list()
Volqueta=df['VOLQUETA'].to_list()
Moto=df['MOTO'].to_list()
Bicicleta=df['BICICLETA'].to_list()
Diurnio_Nocturno=df['DIURNIO/NOCTURNO'].to_list()
#Variables dependientes
Gravedad=df['GRAVEDAD'].to_list()

#Función que crea matriz que representa la tabla principal
@eel.expose
def gettable(peaton, automovil, campaero, camioneta, micro, buseta, bus, camion, volqueta, moto, bicicleta, diurnio_nocturno, gravedad):
    table=np.array(list(zip(peaton, automovil, campaero, camioneta, micro, buseta,bus, camion,volqueta, moto,bicicleta, diurnio_nocturno,gravedad)))
    return table

#tabla= gettable(Peaton,Automovil, Campaero,Camioneta,Micro,Buseta,Bus,Camion,Volqueta,Moto,Bicicleta,Diurnio_Nocturno,Gravedad)
#print(tabla)
#Eliminar registro
@eel.expose
def deleteRecord(datos, f):
    newtable=np.delete(datos,f, axis=0)
    return newtable


#eliminar=deleteRecord(tabla,0)

#Añadir registro
@eel.expose
def addRecord(datos, newrecord):
    newtable=np.vstack((datos,newrecord))
    return newtable 

#new=addRecord(tabla,[1,1,1,1,1,1,1,1,1,1,1,'Diurno','Con Heridos'])
#print(new)
