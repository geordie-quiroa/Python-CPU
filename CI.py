from memoria import ram
from registros import registers
from controlUnit import CU
from MemoryAddressRegistry import MemoryAddressRegistry
from datetime import datetime
programa = CU.programa()  # ya construi el objeto con las instrucciones de programa
PC = CU.programCounter()  # ya construi el objeto PC
# almacena el PC.value que puede cambiar durante la ejecucion sin alterar el atributo del PC como tal.
RAM = ram()  # ya construi el objeto ram con sus respectivos datos
# PC.update() #si aumenta el PC.value en uno
CIR = CU.InstructionRegister.currentInstructionRegister(programa.instrucciones[PC.value])  # ya tengo el CurrentInstructionRegister con el byte a ejecutar en string
MAR = MemoryAddressRegistry(0)  # antes estaba PC.value
A = registers()  # cree el registro A
B = registers()
C = registers()
D = registers()  # este va a ser el Output
do = CU.Interruptions()


def fetching():
    print('-----Fetching--------')
    print("CIR> %s" % CIR.current)
    print("OPCODE> %s" % CIR.opcode)
    print("OPERAND> %s" % CIR.FourBitsAddressInfo)


def decoding():
    print('---- Decoding -------')
    if CIR.decode() == 11 or CIR.decode() == 111 or CIR.decode() == 1001 or CIR.decode() == 1010:
        print("utiliza 2 bits por address")
    else:
        if len(
                CIR.FourBitsAddressInfo) == 4:  # si es = a 4; es una dir de memoria binaria, tengo aqui la convierto a decimales para poder indexar en memoria
            _binaryAddress2convert = CIR.FourBitsAddressInfo
            MAR.addressBus = CIR.convertBinary2DecAddress(
                _binaryAddress2convert)  # el MAR.addressBus ya esta en decimal para ir a buscar a memoria

        if len(CIR.FourBitsAddressInfo) < 4:  # quiere decir que el addressInfo ya esta en decimal,
            if CIR.FourBitsAddressInfo != 'HLT' and (CIR.FourBitsAddressInfo).isdigit():
                MAR.addressBus = int(CIR.FourBitsAddressInfo)
            else:
                MAR.addressBus = 0000
        RAM.dataBusValue = RAM.dataBus(MAR.addressBus)
        print("Opcode> %s" % CIR.opcode)
        if CIR.decode() != 1111:
            print("Instruccion con ese opcode> %s" % CIR.decode())
            print("MAR addressBus> %i" % MAR.addressBus)
            print("RAM dataBus> %i" % RAM.dataBusValue)


def execution():
    print('--- Execution ----')
    # print("MAR addressBus value %i" %MAR.addressBus)
    decoded = CIR.decode()
    operate = CU.InstructionRegister().operations()
    ALU = CU.InstructionRegister.ArithmeticLogicUnit()
    if decoded == 11 or decoded == 111 or decoded == 1001 or decoded == 1010:
        if decoded == 11:
            ALU.AND()
        if decoded == 111:
            operate.OR()
        if decoded == 1001:
            if (CIR.First2bits == "A") and (CIR.Last2bits == "B"):
                ALU.ADD(A, B, D)
                print("Resultado Suma> %i" % D.storedValue)
        if decoded == 1010:
            operate.SUB()
    if decoded == 0000:
        print(operate.output(B))
    if decoded == 1:
        print("MAR addresBus Value> %i" % MAR.addressBus)
        print("Data Bus Value> %i" % RAM.dataBusValue)
        operate.LD_A(A, RAM.dataBusValue)
        print("Registro A> %i" % A.storedValue)
    if decoded == 10:
        print(MAR.addressBus)
        operate.LD_B(B, RAM.dataBusValue)
        print("Data Bus Value> %i" % RAM.dataBusValue)
        print("Registro B> %i" % B.storedValue)
    if decoded == 100:
        operate.ILD_A(A, MAR.addressBus)
        print("addressBus Value> %i" % MAR.addressBus)
        print("Registro A> %i" % A.storedValue)
    if decoded == 1000:
        operate.ILD_B(B, MAR.addressBus)
        print("Registro B > %i" % B.storedValue)
    if decoded == 101:
        operate.STR_A(RAM, MAR.addressBus, A)
        print("Se guardo registro A en posicion RAM> %i" % MAR.addressBus)
    if decoded == 110:
        operate.STR_B(RAM, MAR.addressBus, B)
    if decoded == 1011:
        line2jump = MAR.addressBus
        operate.JMP2instruction(PC, line2jump)
    if decoded == 1111:
        operate.HALT(do)
        print("Terminate")
    PC.update()
    # do.interrupt = 1

startTime = datetime.now()
clock = CU.clock()
for i in range(0, (programa.n), 1):
    if PC.value <= programa.n and do.interrupt != 1:
        fetching()
        decoding()
        if PC.value <= programa.n:
            execution() 
            clock.updateInstructionsExec()
        if PC.value <= programa.n - 1:
            CIR = CU.InstructionRegister.currentInstructionRegister(programa.instrucciones[PC.value])
        print('\n')