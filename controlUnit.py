class ControlUnit:
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
        def __init__(self, instructionAtPC):
            self.current = instructionAtPC


    def FileReader(self, file):
        _file = open(file, "r")
        return(file.read())

    def InstructionsSeparator(self, fileData):
        _byte = 0
        _opCode = ""
        _data = ""
        _instructions = []
        fileData = fileData.replace("\n", "")
        fileData = fileData.replace(" ", "")
        for char in fileData:            
            if _byte < 4:
                _opCode += char
            elif _byte >= 4:
                _data += char
            if _byte == 7:
                _instructions.append([_opCode, _data])
                _opCode = ""
                _data = ""
                byte = -1
            byte += 1
        return _instructions


    def InstructionFetcher(self, instructionRegister, programCounter):
        return instructionRegister[int(programCounter, 2)]

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
    ## Si controlUnit.py está corriendo como dependencia, entonces no correr las siguientes lineas:    
    cu = ControlUnit()
    print(cu.InstructionsSeparator(cu.FileReader("data.code")))