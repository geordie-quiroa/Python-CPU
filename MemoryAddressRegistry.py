#Memory Address Registry --> MAR
class MAR: #MAR recibe el PC del CU para ir a buscar esa data al address en ram que envio el PC, tambien almacena la siguiente linea a ejecutar para que lo use el CU
    def __init__(self, PC=0): #en PC pasas el atributo que tiene el PC de tu CU, PC.Counter o algo asi
        self.dataAddress2fetch = PC
        self.nextDataAddress2fetch = PC+1

class addressBus(MAR): #inherita MAR, con el fin de retornar solo la direccion de ram para esa instruccion, que puede ser cambiada por el CU sin afectar MAR como tal
    def ramDir(self): #va a retornar la direccion de memoria (que contiene la data) que solcito el PC. Este valor lo va a usar la funcion de ram que devuelve la data en esa dirRam al CU
        self.dir = self.dataAddress2fetch #utiliza el atributo (.dataAddress2fetch) de MAR para retornar solo la dir de memoria de la data para ejecutar la instruccion del PC
        return self.dir #da el parametro para usar como indice en el arreglo de ram


if __name__=='__main__':
    PC = 2
    MAR = MAR() # puede ir vacio, lo tomaria como PC = 0
    MAR.dataAddress2fetch = PC
    MAR.dataAddress2fetch = 8
    print(addressBus().ramDir())
    ramDir = addressBus.ramDir(MAR)
    print(MAR.dataAddress2fetch)
    print(ramDir)