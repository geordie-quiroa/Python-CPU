class memory:
    class data:
        _opcodes = [] # variables privadas, por convencion se usa el guion bajo para este tipo de variables.
        _memory_address = []
        _readMe = open("test.code", 'r').read()
        #print(_readMe)
        _parseData = _readMe.split('\n')  # crea un array para cada linea del .code
        #print(_splitMe)
        n = len(_parseData)
        def __init__(self):
                self.instructions = memory.data._parseData
        for byte in _parseData:
            #print(byte[4:8])
            _opcodes.append(byte[0:4])
            _memory_address.append(byte[4:10])

    class ram(data): #inherita la clase data 
        def __init__(self):
            self.opcodes = memory.data._opcodes
            self.memory_address = memory.data._memory_address

#ram = memory.ram()
#for byte in range (0, memory.data.n, 1):
    #return (ram.opcodes[0:4], ram.memory_address[4:8])
