from memoria import ram
from registros import registers
from controlUnit import CU
from MemoryAddressRegistry import MAR

programa = CU.programa() #ya construi el objeto con las instrucciones de programa
PC = CU.programCounter() # ya construi el objeto PC
RAM = ram() # ya construi el objeto ram con sus respectivos datos 
PC.update() #si aumenta el PC.value en uno
CIR = CU.InstructionRegister.currentInstructionRegister(programa.instrucciones[PC.value]) #ya tengo el CurrentInstructionRegister con el byte a ejecutar en string
MAR = MAR(PC.value) #almacena el PC.value que puede cambiar durante la ejecucion sin alterar el atributo del PC como tal.
dataBus = RAM.dataBus(MAR.addressBus)
print(RAM.data)
print(RAM.dataBus(5))
print(MAR.addressBus)
print(dataBus)
PC.update()
MAR.addressBus = 6 #cambio 
print(MAR.addressBus)
print(dataBus)
print(CIR.current)
print(CIR.FourBitsAddressInfo)
def comentario():
    print('aqui voy a integrar todos los modulos creados.')