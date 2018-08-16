class IntegratedCircuit():
    ## Cada funcion debe estar "autocontenida" para poder hacer pruebas autmatizadas.
    def FileReader(self, file):
        file = open(file, "r")
        return(file.read())

    def InstructionParser(self, machineCode):
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
        }.get(machineCode, machineCode)


if __name__ == '__main__': 
    ## Si controlUnit.py está corriendo como dependencia, entonces no correr las siguientes lineas:    
    ic = IntegratedCircuit()

    print(ic.InstructionParser(input("Code: ")))
    print(ic.FileReader("data.code"))