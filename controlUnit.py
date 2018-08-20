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
                self.addressInfo = instructionAtPC[_index:_instructionLength]
            else:
                self.opcode = instructionAtPC # ver cual es la direccion de halt aqui va a ir
                self.addressInfo = instructionAtPC #ver cual es la direccion de HALT, aqui va a ir

    def InstructionDecoder(self, opcode, data):
        opcode = int(opcode, 2)
        if opcode == 0:
            print(opcode)
            ## DO OUTPUT
        elif opcode == 1:
            print(opcode)
            ## DO LD_A
        elif opcode == 2:
            print(opcode)
            ## DO LD_B
        elif opcode == 3:
            print(opcode)
            ## DO AND
        elif opcode == 4:
            print(opcode)
            ## DO ILD_A
        elif opcode == 5:
            print(opcode)
            ## DO STR_A
        elif opcode == 6:
            print(opcode)
            ## DO STR_B
        elif opcode == 7:
            print(opcode)
            ## DO OR
        elif opcode == 8:
            print(opcode)
            ## DO ILD_B
        elif opcode == 9:
            print(opcode)
            ## DO ADD
        elif opcode == 10:
            print(opcode)
            ## DO SUB
        elif opcode == 11:
            print(opcode)
            ## DO SUB
        elif opcode == 12:            
            ## DO JMP
            print("TEST")            
        elif opcode == 13:
            print(opcode)
            ## DO JMP_N
        elif opcode == 14:
            print(opcode)
            ## DO ROR?
        elif opcode == 15:
            print(opcode)
            ## DO ROL?
        elif opcode == 16:            
            ## DO HLT
            self.halt()
        else:
            print(opcode)
            ## DO NOTHING
        return opcode

    def halt(self):
        exit()


if __name__ == '__main__': 
    PC = CU.programCounter()
    programa = CU.programa()
    ProgInstrucciones = programa.instrucciones
    for i in range(0, programa.n-1,1):
        print(PC.value)
        CIR = CU.currentInstructionRegister(ProgInstrucciones[PC.value])
        print(CIR.current, "opcode> %s" %CIR.opcode, "address Info> %s" %CIR.addressInfo)
        PC.update()
        #print(programa.programInstructions[i])
    i = 2
    index = ProgInstrucciones[i].find(' ')
    print(ProgInstrucciones[i][0:index])
    print(ProgInstrucciones)