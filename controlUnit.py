class ControlUnit():
    ## Cada funcion debe estar "autocontenida" para poder hacer pruebas autmatizadas.
    def FileReader(self, file):
        file = open(file, "r")
        return(file.read())

    def InstructionsSeparator(self, fileData):
        byte = 0
        opCode = ""
        data = ""
        instructions = []
        fileData = fileData.replace("\n", "")
        fileData = fileData.replace(" ", "")
        for char in fileData:            
            if byte < 4:
                opCode += char
            elif byte >= 4:
                data += char
            if byte == 7:
                instructions.append([opCode, data])
                opCode = ""
                data = ""
                byte = -1
            byte += 1
        return instructions


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