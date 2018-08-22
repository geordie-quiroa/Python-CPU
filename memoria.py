from load2ram import data

class ram(data):  # inherita clase data
    def __init__(self):
        _addresses = [] #utilizo el gion bajo como una convencion de desarrollo POO en python para definir metodos y variables privadas para una clase.
        self.data = data()._datosAMemoria #cargo el atributo privado _datosAMemoria del modulo load2ram  a un atributo arreglo publico de ram para poder indexar los valores
        self.totalData = ram.n
        for address in range(0, self.totalData, 1):
            _addresses.append(address) 
        self.addresses = _addresses
        self.dataBusValue = 0
        
    def dataBus(self, ramDir):
        return self.data[ramDir]

if __name__ == '__main__':
    RAM = ram() #RAM es el objeto, ram() es el constructor
    for i in range (0,16,1):
        print(RAM.dataBus(i))
    RAM.data[2] = 15
    dataBus = RAM.dataBus(2)
    print(RAM.data)