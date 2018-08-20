from load2ram import data
class ram(data):  # inherita clase data
    def __init__(self):
        _addresses = []
        # self.opcodes = memory.data._opcodes
        # self.data = memory.data._data4bits
        self.data = data()._datosAMemoria
        self.totalData = ram.n
        for address in range(0, self.totalData, 1):
            _addresses.append(address)
        self.addresses = _addresses
        
    def dataBus(self, ramDir):
        return self.data[ramDir]


if __name__ == '__main__':
    ram = ram()
    for i in range (0,16,1):
        dataBus = ram.dataBus(i)
        print(dataBus)
    ram.data[2] = 15
    dataBus = ram.dataBus(2)
    print(ram.data)