from load2ram import data

class ram(data):  # inherita clase data
    def __init__(self):
        _addresses = []
        self.data = data()._datosAMemoria
        self.totalData = ram.n
        for address in range(0, self.totalData, 1):
            _addresses.append(address)
        self.addresses = _addresses
        
    def dataBus(self, ramDir):
        return self.data[ramDir]

if __name__ == '__main__':
    RAM = ram()
    for i in range (0,16,1):
        print(RAM.dataBus(i))
    RAM.data[2] = 15
    dataBus = RAM.dataBus(2)
    print(RAM.data)