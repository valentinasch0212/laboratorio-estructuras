import eel

#Debería de recibir de qué dato a que dato quiere retornar
#ejemplo, del registro 30 al 100
#y debería retornar una matriz que contenga la tabla
@eel.expose
def getOriginalTable():
    return

if __name__ == '__main__':
    eel.init('web')
    eel.start('main.html', size=(600, 600), port=3000, mode='chrome')