from alu import ALU
from datetime import datetime
class CU:
    class clock:
        _cyclesExecuted = 0
        def __init__(self):
            self.cycles = self._cyclesExecuted
        def calculateSpeed(self, timeStarted):
            return (self.cycles/(datetime.now()-timeStarted))
        def updateInstructionsExec(self):
            self._cyclesExecuted +=1
    class Interruptions:
        _value = 0
        def __init__(self):
            self.interrupt = self._value
    class programa:
        # Cada funcion debe estar "autocontenida" para poder hacer pruebas autmatizadas.
        _readMe = open("program2.code", 'r').read()
        _readProgram = _readMe.split('\n')  # crea un array
        _programInstructions = [] # cambie _parseData por _data
        for instruction in _readProgram:
            byte = instruction.upper()
            #byte = prebyte.replace(' ', '')
            _programInstructions.append(byte)
        n = len(_programInstructions)

        def __init__(self):
            self.instrucciones = self._programInstructions

    class programCounter:
        _value = 0

        def __init__(self):
            self.value = self._value

        def update(self, jmp=1):
            self.value += jmp
            
    class InstructionRegister:
        class currentInstructionRegister:
            def __init__(self, instructionAtPC): #tiene que recibir el string del programa.code at PC. Sin procesar ni nada, porque adentro lo procesa.
                self.current = instructionAtPC
                _index = instructionAtPC.find(' ')
                _instructionLength = len(instructionAtPC)
                if _index >0:
                    self.opcode = instructionAtPC[0:_index]
                    self.FourBitsAddressInfo = instructionAtPC[_index+1:_instructionLength]
                    #_stringAddressInfo = self.FourBitsAddressInfo
                    #_addressIndex = _stringAddressInfo.find(' ')
                    #if _addressIndex >0:
                        #print("separar los 4 bits en 2 de 2")
                    self.First2bits = instructionAtPC[_index+1:_index+2]
                    self.Last2bits = instructionAtPC[_instructionLength-1:_instructionLength]
                else:
                    self.opcode = instructionAtPC # ver cual es la direccion de halt aqui va a ir
                    self.FourBitsAddressInfo = instructionAtPC #ver cual es la direccion de HALT, aqui va a ir
            def convertBinary2DecAddress(self, BinaryAddress_string):
                _binaryAddress = ['0000', '0001', '0010', '0111', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
                binaryAddress2int = _binaryAddress.index(BinaryAddress_string)
                return binaryAddress2int
            def decode(self):
                opcode = self.opcode
                if opcode == 'OUTPUT' or opcode == '0000':
                    return  0 #('Fuciono output')
                if opcode == 'LD_A' or opcode == '0001':
                    return 1 #('Funciono LD_A')
                    ## DO OUTPUT
                if opcode == 'LD_B' or opcode == '0010':
                    return 10 #('Funciono LD_B')
                    ## DO LD_A
                if opcode == 'AND' or opcode == '0011':
                    return  11 #('Funciono AND')
                    ## DO LD_B
                if opcode == 'ILD_A' or opcode == '0100':
                    return 100 #('Funciono ILD_A')
                    ## DO AND
                if opcode == 'ILD_B' or opcode == '1000':
                    return 1000 #('Funciono ILD_B')
                if opcode == 'STR_A' or opcode == '0101':
                    return 101 #('Funciono STR_A')
                    ## DO ILD_A
                if opcode == 'STR_B' or opcode == '0110':
                    return 110 #('Funciono STR_B')
                    ## DO STR_A
                if opcode == 'STR_C' or opcode == '0111':
                    return 111 #('Funciono STR_C')
                    ## DO STR_B
                if opcode == 'ADD' or opcode == '1001':
                    return 1001 #('Funciono ADD')
                if opcode == 'SUB' or opcode == '1010':
                    return 1010 #('Funciono SUB')
                    ## DO ADD
                if opcode == 'JMP' or opcode == '1011':
                    return 1011 #('Funciono JMP')
                    ## DO SUB
                if opcode == 'JMP_N' or opcode == '1100':
                    return 1100 #('Funciono JMP_N')
                    ## DO SUB
                if opcode == 'ROR?' or opcode == '1101':
                    ## DO JMP
                    return 1101 #("Funciono ROR?")
                if opcode == 'ROL?' or opcode == '1110':
                    return 1110 #('Funciono ROL?')
                if opcode == 'HLT' or opcode == '1111':
                    return 1111 #('Funciono HALT')
        class ArithmeticLogicUnit:
            def ADD(self, register1, register2):
                register1.storedValue = register1.storedValue + register2.storedValue
                return register1

            def AND(self, register1, register2):
                register1.storedValue = register1.storedValue & register2.storedValue
                return register1

            def OR(self, register1, register2):
                register1.storedValue = register1.storedValue | register2.storedValue
                return register1

            def SUB(self, register1, register2):
                register1.storedValue = register1.storedValue - register2.storedValue
                return register1
            
            def SHR(self, register):
                register = register >> 1
                return register                

            def SHL(self, register):
                register = register << 1
                return register
        class operations:            
            def output(self, B):
                return B.storedValue
            def LD_A(self, registerA, dataBusVal): #en IC le paso el objeto "A" y ese es el param de registerA, luego en dataBusVal le paso el valor del atributo de RAM "dataBusValue"
                registerA.storedValue = dataBusVal
                print('Loaded A')
            def LD_B(self, registerB, dataBusVal):
                registerB.storedValue = dataBusVal
                print("Loaded B")
            def ILD_A(self, registerA, store2registerA):
                registerA.storedValue = store2registerA
            def ILD_B(self, registerB, store2registerB):
                registerB.storedValue = store2registerB
            def STR_A(self, ram, dirAtRam2write, registerA):
                ram.data[dirAtRam2write] = registerA.storedValue
            def STR_B(self, ram, dirAtRam2write, registerB):
                ram.data[dirAtRam2write] = registerB.storedValue
            def JMP2instruction(self, PCobject, jump2instruction):
                PCobject.update(jump2instruction)
            def HALT(self, doI):
                doI.interrupt = 1
if __name__ == '__main__': 
    def prueba1():
        PC = CU.programCounter()
        programa = CU.programa()
        ProgInstrucciones = programa.instrucciones
        
        for i in range(0, programa.n-1,1):
            print(PC.value)
            CIR = CU.InstructionRegister.currentInstructionRegister(ProgInstrucciones[PC.value])
            print(CIR.current, "opcode> %s" %CIR.opcode, "address Info> %s" %CIR.FourBitsAddressInfo)
            print(CIR.decode())
            PC.update()
            print(programa.instrucciones[i])
        i = 2
        index = ProgInstrucciones[i].find(' ')
        CIR = CU.InstructionRegister.currentInstructionRegister(ProgInstrucciones[PC.value])
        print(ProgInstrucciones[i][0:index])
        print(ProgInstrucciones)
        print(CIR.decode())

    def prueba2():
        PC = CU.programCounter()
        programa = CU.programa()
        progInstructions = programa.instrucciones
        for i in range (0, programa.n-1, 1):
            print(progInstructions[i])
            print(PC.value)
            CIR = CU.InstructionRegister.currentInstructionRegister(progInstructions[PC.value])
            print(CIR.current)
            print("addressInfo> %s" %CIR.FourBitsAddressInfo)
            print(CIR.decode())
            PC.update()
    prueba2()