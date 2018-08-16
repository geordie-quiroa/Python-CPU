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


if __name__ == '__main__': 
    ## Si controlUnit.py está corriendo como dependencia, entonces no correr las siguientes lineas:    
    cu = ControlUnit()
    print(cu.InstructionsSeparator(cu.FileReader("data.code")))