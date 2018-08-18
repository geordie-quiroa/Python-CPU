class memory:
    class data:
        #_opcodes = [] # variables privadas, por convencion se usa el guion bajo para este tipo de variables.
        #_data4bits = []
        _readMe = open("data.code", 'r').read()
        #print(_readMe)
        _data = _readMe.split('\n')  # crea un array
        #_data = [] #cambie _parseData por _data
        #print(_splitMe)
        n = len(_data)
        def __init__(self):
                self.instructions = memory.data._data
        #for byte in _parseData:  # inhabilite esta funcion porque ahora _parseData es _data
            #print(byte[4:8])
            #_data.append(byte)
            #_opcodes.append(byte[0:4])
            #_data4bits.append(byte[4:8])

    class ram(data): #inherits class data
        def __init__(self):
            address = []
            #self.opcodes = memory.data._opcodes
            #self.data = memory.data._data4bits
            self.data = memory.data._data
            self.totalData = memory.ram.n
            for i in range (0,self.totalData,1):
                address.append(i)
            self.address = address
    class MAR:
        def __init__(self, PC=0):
            self.instruction2exec = PC
            self.nextInstruction2exec = PC +1


    class addressBus:
        def __init__(self):
            self.address = "hello"
if __name__ == '__main__':
    #ram=memory.ram(memory.ram)
    #memory.ram(memory.ram._splitMe)

    instrucciones = memory.data()
    print(instrucciones.instructions)
    ram = memory.ram()
    #ram.opcodes
    for n in range (0, memory.data.n, 1):
        print(ram.address[n], ram.data[n], ram.totalData, ram._data, ram.address)
    #print(ram.opcode, ram.memory_address)
    #for byte in memory.ram._splitMe:
        #print(byte)
    #    print(byte[0:4], byte[0:4])
    MAR = memory.MAR()
    for i in range(0, 5, 1):
        MAR.instruction2exec = i
        MAR.nextInstruction2exec = i+1
        print(MAR.instruction2exec, " - %i" %MAR.nextInstruction2exec)
