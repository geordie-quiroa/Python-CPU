class IntegratedCircuit():
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
        for char in fileData:            
            if byte < 4:
                opCode += char
            elif byte >= 4:
                data += char
            if byte == 7:
                instructions.append([int(opCode, 2), int(data, 2)])
                opCode = ""
                data = ""
                byte = -1
            byte += 1
        return instructions



    def InstructionParser(self, instCode):
        # Python Dictionary
        ## Si "machineCode" es alguno de los elementos de la derecha entonces retornar el elemento de la izquierda.
        ## Es similar a un switch de otros lenguajes.
        return{
            '0000': 'OUTPUT',
            '0001': 'LD_A',
            '0010': 'LD_B',
            '0011': 'AND',
            '0100': 'ILD_A',
            '0101': 'STR_A',
            '0110': 'STR_B',
            '0111': 'OR',
            '1000': 'ILD_B',
            '1001': 'ADD',
            '1010': 'SUB',
            '1011': 'JMP',
            '1100': 'JMP_N',
            '1101': 'ROR?',
            '1110': 'ROL?',
            '1111': 'HLT'
        }.get(instCode, instCode)


if __name__ == '__main__': 
    ## Si controlUnit.py está corriendo como dependencia, entonces no correr las siguientes lineas:    
    ic = IntegratedCircuit()

    #print(ic.InstructionParser(input("Code: ")))
    ic.InstructionsSeparator(ic.FileReader("data.code"))