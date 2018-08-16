import controlUnit
import unittest

##Clase de pruebas automatizadas
class TestCPU(unittest.TestCase):

    #Definicion para comprobar que la funcion Parser de ControlUnit esté funcionando.
    def test_parser(self):
        #Listado de respuestas esperadas al parser
        instructions = [['0000', 'OUTPUT'],['0001', 'LD_A'],['0010', 'LD_B'],['0011', 'AND'],['0100', 'ILD_A'],['0101', 'STR_A'],['0110', 'STR_B'],['0111', 'OR'],['1000', 'ILD_B'],['1001', 'ADD'],['1010', 'SUB'],['1011', 'JMP'],['1100', 'JMP_N'],['1101', 'ROR?'],['1110', 'ROL?'],['1111', 'HLT']]
        #La variable result tiene la respuesta de la funcion Parser de Control Unit.
        #La idea de esta prueba es comprobar que parser está respondiendo los valores esperados.
        for inst in instructions:
            ic = controlUnit.IntegratedCircuit()
            result = ic.InstructionParser(inst[0])
            self.assertEqual(result, inst[1])

    def test_reader(self):
        ic = controlUnit.IntegratedCircuit()
        result = ic.FileReader("test.code")
        self.assertEqual(result, "00001111")
        

if __name__ == '__main__':
    #Si test_cpu.py está corriendo como dependencia entonces no correr las siguientes lineas:
    unittest.main()