from memoria import ram
from registros import registers
from controlUnit import CU
from MemoryAddressRegistry import MemoryAddressRegistry

programa = CU.programa() #ya construi el objeto con las instrucciones de programa
PC = CU.programCounter() # ya construi el objeto PC
 #almacena el PC.value que puede cambiar durante la ejecucion sin alterar el atributo del PC como tal.
RAM = ram() # ya construi el objeto ram con sus respectivos datos 
#PC.update() #si aumenta el PC.value en uno
CIR = CU.InstructionRegister.currentInstructionRegister(programa.instrucciones[PC.value]) #ya tengo el CurrentInstructionRegister con el byte a ejecutar en string
MAR = MemoryAddressRegistry(0) #antes estaba PC.value
A = registers() #cree el registro A 
B = registers()
C = registers()
D = registers()

def fetching():
    print('-----Fetching--------')
    #if len(CIR.FourBitsAddressInfo) == 4: #quiere decir que el addressCode esta en binario, lo voy a convertir a hex para cargar la dir al addressBus
    #    _address2convert= CIR.FourBitsAddressInfo
    #    MAR.addressBus = CIR.convertBinary2DecAddress(_address2convert)
    #elif (CIR.FourBitsAddressInfo).isdigit()==True and len(CIR.FourBitsAddressInfo)<4: #quiere decir que
    #    print("Carajo")
    #else:
    #    MAR.addressBus = int(CIR.FourBitsAddressInfo)
    #dataBus = RAM.dataBus(MAR.addressBus)
    #print("addressBus> %i"%MAR.addressBus)
    #print("dataEnMemoria > %i"%dataBus)
    #A.storedValue = dataBus
    #print("Valor en registro A> %i"%A.storedValue)

    print("CIR> %s"%CIR.current)
    print(CIR.opcode)
    print(CIR.FourBitsAddressInfo)

def decoding():
    print('---- Decoding -------')
    if CIR.decode() == 11 or CIR.decode() == 111 or CIR.decode() == 1001 or CIR.decode() == 1010:
        print("utiliza 2 bits por address")
    else:
        if len(CIR.FourBitsAddressInfo) == 4: #si es = a 4; es una dir de memoria binaria, tengo que convertirlo a dec
            _binaryAddress2convert = CIR.FourBitsAddressInfo
            MAR.addressBus = CIR.convertBinary2DecAddress(_binaryAddress2convert) #el MAR.addressBus ya esta en decimal para ir a buscar a memoria

        if len(CIR.FourBitsAddressInfo) < 4: #quiere decir que el addressInfo ya esta en decimal, 
            MAR.addressBus = int(CIR.FourBitsAddressInfo)
        RAM.dataBusValue = RAM.dataBus(MAR.addressBus)
        print("Opcode> %s"%CIR.opcode)
        print("Instruccion con ese opcode> %s"%CIR.decode())
        print("MAR addressBus> %i" %MAR.addressBus)
        print("RAM dataBus> %i" %RAM.dataBusValue)

def execution():
    print('--- Execution ----')
    print("MAR addressBus value %i" %MAR.addressBus)
    decoded = CIR.decode()
    operate = CU.InstructionRegister().operations()
    if decoded == 0000:
        operate.output()
    if decoded == 1:
        print(MAR.addressBus)
        operate.LD_A()
    print(decoded)
    PC.update()
    


for i in range(0, (programa.n),1) :
    fetching()
    decoding()
    execution()
    if i < programa.n-1:
        CIR = CU.InstructionRegister.currentInstructionRegister(programa.instrucciones[PC.value])
