class memory:
    class data:
        _readMe = open("test.code", 'r').read()
        _predata = _readMe.split('\n')  # asigna a cada linea del archivo, una posicion en el arreglo privado _data
        _data = []
        for byte in _predata:
            byte = int(byte)
            _data.append(byte)
        n = len(_data)
        def __init__(self):
                self.instructions = memory.data._data #crea el atributo de instrucciones al objeto data para luego cargarlo a ram

    class ram(data): #inherita clase data
        def __init__(self):
            _addresses = []
            self.data = memory.data().instructions #cargo el atributo instrucciones de la clase data a un atributo arreglo de ram para poder indexar los valores
            self.totalData = memory.ram.n
            for address in range (0,self.totalData,1):
                _addresses.append(address)
            self.addresses = _addresses
    #Memory Address Registry --> MAR
    class MAR: #MAR recibe el PC del CU para ir a buscar esa data al address en ram que envio el PC, tambien almacena la siguiente linea a ejecutar para que lo use el CU
        def __init__(self, PC=0): #en PC pasas el atributo que tiene el PC de tu CU, PC.Counter o algo asi
            self.instruction2exec = PC
            self.nextInstruction2exec = PC +1
    class addressBus(MAR): #inherita MAR, con el fin de retornar solo la direccion de ram para esa instruccion 
        def ramDir(self): #va a retornar la direccion de memoria (que contiene la data) que solcito el PC. Este valor lo va a usar la funcion de ram que devuelve la data en esa dirRam al CU
            self.dir = self.instruction2exec #utiliza el atributo (.instruction2exec) de MAR para retornar solo la dir de memoria de la data para ejecutar la instruccion del PC
            return self.dir
    
    class registers:
        inUse = 0
        def __init__(self, n=0):
            if n == 0:
                self.storedValue = n
            else:
                self.storedValue = n
                memory.registers.inUse += 1
        def clearRegistry(self):
            self.storedValue = 0
            memory.registers.inUse -= 1

        def withValue(self):
            if self.storedValue >0:
                return 1
            else:
                return 0

if __name__ == '__main__':

    instrucciones = memory.data()
    print(instrucciones.instructions)
    ram = memory.ram()
    
    for n in range (0, memory.data.n, 1):
        print(ram.addresses[n], ram.data[n], ram.totalData, ram._data, ram.addresses)
    
    for i in range(0, ram.totalData, 1):
        MAR = memory.MAR(i) # i es el program counter PC
        print(MAR.instruction2exec, " - %i" %MAR.nextInstruction2exec)
        print("Ir a buscar esta direccion en memoria> %i" %memory.addressBus.ramDir(MAR)) #MAR es el objeto definido dentro de este for y retorna la direccion de ram para obtener la data.
    print(MAR.instruction2exec)
    #addressBus = memory.addressBus
    direccionRam = memory.addressBus.ramDir(MAR)
    print("Buscar en RAM la direccion %i" % direccionRam)
    regA = memory.registers(direccionRam)
    regC = memory.registers(direccionRam)
    regB = memory.registers()
    print("Valor del Registro A  %i" %regA.storedValue)
    print(regB.storedValue)
    print("Registros en uso>> %i" %memory.registers.inUse)
    regC.clearRegistry()
    print("Registros en uso>> %i" % memory.registers.inUse)
    print(regC.storedValue)
    print(regA.withValue())