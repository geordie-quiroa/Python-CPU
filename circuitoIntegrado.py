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
A = registers() #cree el registro A 

def fetching():
    print('-----Fetching--------')
    MAR = MemoryAddressRegistry(PC.value)
    dataBus = RAM.dataBus(MAR.addressBus)
    print("addressBus> %i"%MAR.addressBus)
    print("CIR> %s"%CIR.current)
    print("dataEnMemoria > %i"%dataBus)
    A.storedValue = dataBus
    print("Valor en registro A> %i"%A.storedValue)
    

def decoding():
    print('---- Decoding -------')
    print(CIR.opcode)
    print(CIR.decode())

def execution():
    print('--- Execution ----')
    PC.update()


for i in range(0, (programa.n),1) :
    fetching()
    decoding()
    if i < programa.n-1:
        execution()
    CIR = CU.InstructionRegister.currentInstructionRegister(programa.instrucciones[PC.value])