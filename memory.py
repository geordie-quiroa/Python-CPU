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
    #Memory Address Registry --> MAR
    class MAR: #MAR recibe el PC del CU para ir a buscar esa data al address en ram que envio el PC, tambien almacena la siguiente linea a ejecutar para que lo use el CU
        def __init__(self, PC=0): #en PC pasas el atributo que tiene el PC de tu CU, PC.Counter o algo asi
            self._instruction2exec = PC
            self._nextInstruction2exec = PC +1
    class addressBus(MAR): #inherita atributos privados de MAR 
        def ramDir(self): #va a retornar la direccion de memoria (que contiene la data) que solcito el PC. Este valor lo va a usar la funcion de ram que devuelve la data en esa dirRam al CU
            self.dir = self._instruction2exec #utiliza el atributo privado (._instruction2exec) de MAR para retornar solo la dir de memoria de la data para ejecutar la instruccion del PC
            return self.dir

if __name__ == '__main__':

    instrucciones = memory.data()
    print(instrucciones.instructions)
    ram = memory.ram()
    
    for n in range (0, memory.data.n, 1):
        print(ram.address[n], ram.data[n], ram.totalData, ram._data, ram.address)
    
    for i in range(0, ram.totalData, 1):
        MAR = memory.MAR(i) # i es el program counter PC
        print(MAR._instruction2exec, " - %i" %MAR._nextInstruction2exec)
        print("Ir a buscar esta direccion en memoria> %i" %memory.addressBus.ramDir(MAR)) #MAR es el objeto definido dentro de este for.
    