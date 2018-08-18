class memory:
    class data:
        opcodes = []
        memory_address = []
        _readMe = open("data.code", 'r').read()
        #print(_readMe)
        _splitMe = _readMe.split('\n')  # crea un array
        #print(_splitMe)

        def __init__(self, _splitMe):
                self.instructions = _splitMe
        for byte in _splitMe:
            #print(byte[4:8])
            opcodes.append(byte[0:4])
            memory_address.append(byte[4:10])

    class ram(data):
        def __init__(self):
            self.opcodes = memory.ram.opcodes
            self.memory_address = memory.ram.memory_address
