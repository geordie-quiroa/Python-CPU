class CU:
    class programa:
        # Cada funcion debe estar "autocontenida" para poder hacer pruebas autmatizadas.
        _readMe = open("program.code", 'r').read()
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

        def update(self):
            self.value += 1
            
    class currentInstructionRegister:
        def __init__(self, instructionAtPC): #tiene que recibir el string del programa.code at PC. Sin procesar ni nada, porque adentro lo procesa.
            self.current = instructionAtPC
            _index = instructionAtPC.find(' ')
            _instructionLength = len(instructionAtPC)
            if _index >0:
                self.opcode = instructionAtPC[0:_index]
                self.FourBitsAddressInfo = instructionAtPC[_index:_instructionLength]
            else:
                self.opcode = instructionAtPC # ver cual es la direccion de halt aqui va a ir
                self.FourBitsAddressInfo = instructionAtPC #ver cual es la direccion de HALT, aqui va a ir
        def decode(self):
            #_data2evaluate = CU.InstructionRegister()
            #_data2evaluate.evaluate(self.opcode)
            opcode = self.opcode
            if opcode == 'OUTPUT' or opcode == '0000':
                return('Fuciono output')
            if opcode == 'LD_A' or opcode == '0001':
                return('Funciono LD_A')
                ## DO OUTPUT
            elif opcode == 'LD_B' or opcode == '0010':
                return('Funciono LD_B')
                ## DO LD_A
            elif opcode == 'AND' or opcode == '0011':
                return ('Funciono AND')
                ## DO LD_B
            elif opcode == 'ILD_A' or opcode == '0100':
                return ('Funciono ILD_A')
                ## DO AND
            elif opcode == 'ILD_B' or opcode == '0010':
                return ('Funciono ILD_B')
            elif opcode == 'STR_A' or opcode == '0101':
                return ('Funciono STR_A')
                ## DO ILD_A
            elif opcode == 'STR_B' or opcode == '0110':
                return ('Funciono STR_B')
                ## DO STR_A
            elif opcode == 'STR_C' or opcode == '0111':
                return ('Funciono STR_C')
                ## DO STR_B
            elif opcode == 'ADD' or opcode == '1001':
                return ('Funcionon ADD')
                ## DO ILD_B
            elif opcode == 'SUB' or opcode == '1010':
                return ('Funciono SUB')
                ## DO ADD
            elif opcode == 'JMP' or opcode == '1011':
                return ('Funciono JMP')
                ## DO SUB
            elif opcode == 'JMP_N' or opcode == '1100':
                return ('Funciono JMP_N')
                ## DO SUB
            elif opcode == 'ROR?' or opcode == '1101':
                ## DO JMP
                return ("Funciono ROR?")
            elif opcode == 'ROL?' or opcode == '1110':
                return ('Funciono ROL?')
            elif opcode == 'HLT' or opcode == '1111':
                return ('Funciono HALT')
    
    class InstructionRegister:
        def evaluate(self, opcodeSent):
            opcode = opcodeSent
            if opcode == 'OUTPUT' or opcode == '0000':
                return(opcode + '1')
            if opcode == 'LD_A' or opcode == '0001':
                return(opcode)
                ## DO OUTPUT
            elif opcode == 'LD_B' or opcode == '0010':
                print(opcode)
                ## DO LD_A
            elif opcode == 'AND' or opcode == '0011':
                print(opcode)
                ## DO LD_B
            elif opcode == 'ILD_A' or opcode == '0100':
                print(opcode)
                ## DO AND
            elif opcode == 'ILD_B' or opcode == '0010':
                print(opcode)
            elif opcode == 'STR_A' or opcode == '0101':
                print(opcode)
                ## DO ILD_A
            elif opcode == 'STR_B' or opcode == '0110':
                print(opcode)
                ## DO STR_A
            elif opcode == 'STR_C' or opcode == '0111':
                print(opcode)
                ## DO STR_B
            elif opcode == 'ADD' or opcode == '1001':
                print(opcode)
                ## DO ILD_B
            elif opcode == 'SUB' or opcode == '1010':
                print(opcode)
                ## DO ADD
            elif opcode == 'JMP' or opcode == '1011':
                print(opcode)
                ## DO SUB
            elif opcode == 'JMP_N' or opcode == '1100':
                print(opcode)
                ## DO SUB
            elif opcode == 'ROR?' or opcode == '1101':
                ## DO JMP
                print("TEST")
            elif opcode == 'ROL?' or opcode == '1110':
                print(opcode)
            elif opcode == 'HLT' or opcode == '1111':
                print(opcode)

    def InstructionDecoder(self, opcode, data):
        opcode = int(opcode, 2)
        
    def halt(self):
        exit()


if __name__ == '__main__': 
    def prueba1():
        PC = CU.programCounter()
        programa = CU.programa()
        ProgInstrucciones = programa.instrucciones
        
        for i in range(0, programa.n-1,1):
            print(PC.value)
            CIR = CU.currentInstructionRegister(ProgInstrucciones[PC.value])
            print(CIR.current, "opcode> %s" %CIR.opcode, "address Info> %s" %CIR.FourBitsAddressInfo)
            print(CIR.decode())
            PC.update()
            print(programa.instrucciones[i])
        i = 2
        index = ProgInstrucciones[i].find(' ')
        CIR = CU.currentInstructionRegister(ProgInstrucciones[PC.value])
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
            CIR = CU.currentInstructionRegister(progInstructions[PC.value])
            print(CIR.current)
            print(CIR.decode())
            PC.update()
    prueba2()