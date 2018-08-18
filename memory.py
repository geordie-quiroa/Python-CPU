class memory:
    class data:
        _readMe = open("test.code", 'r').read()
        _data = _readMe.split('\n')  # asigna a cada linea del archivo, una posicion en el arreglo privado _data
        n = len(_data)
        def __init__(self):
                self.instructions = memory.data._data #crea el atributo de instrucciones al objeto data para luego cargarlo a ram

    class ram(data): #inherita clase data
        def __init__(self):
            address = []
            self.data = memory.data._data
            self.totalData = memory.ram.n
            for i in range (0,self.totalData,1):
                address.append(i)
            self.address = address
    class MAR: #MAR recibe el PC del CU para ir a buscar esa data al address en ram que envio el PC, tambien almacena la siguiente linea a ejecutar para que lo use el CU
        def __init__(self, PC=0):
            self.instruction2exec = PC
            self.nextInstruction2exec = PC +1

    class addressBus:
        def __init__(self):
            self.address = "hello"
if __name__ == '__main__':

    instrucciones = memory.data()
    print(instrucciones.instructions)
    ram = memory.ram()
    
    for n in range (0, memory.data.n, 1):
        print(ram.address[n], ram.data[n], ram.totalData, ram._data, ram.address)
    MAR = memory.MAR()
    for i in range(0, memory.data.n, 1):
        MAR.instruction2exec = i
        MAR.nextInstruction2exec = i+1
        print(MAR.instruction2exec, " - %i" %MAR.nextInstruction2exec)
