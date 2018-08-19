import controlUnit
import unittest
import memory

##Clase de pruebas automatizadas del CPU
class TestCPU(unittest.TestCase):    

    def test_reader(self):
        cu = controlUnit.ControlUnit()     
        # La variable /result/ va a retornar el text del archivo 'test.code'
        result = cu.FileReader("test.code")
        # Yo espero que el resultado sea '00001111\n11110000\n10100000\n11100111'
        # Si no me da ese resultado entonces me tiene que tirar un error y decirme cual fue
        ### el resultado real.
        self.assertEqual(result, "00001111\n11110000\n10100000\n11100111")

    def test_separator(self):
        cu = controlUnit.ControlUnit()
        # La variable /result/ va a retornar el string separado de 4 caracters en 4
        result = cu.InstructionsSeparator("0000111111110000")
        # Yo espero que el resultado sea '[["0000","1111"], ["1111", "0000"]]'
        # Si no me da ese resultado entonces me tiene que tirar un error y decirme cual fue
        ### el resultado real.
        self.assertEqual(result, [["0000","1111"], ["1111", "0000"]])
    
    def test_fetcher(self):
        cu = controlUnit.ControlUnit()
        # La variable /result/ va a retornar el item en la posicion 1 (que esta dada en binario)
        result = cu.InstructionFetcher([["0000","1111"], ["1111", "0000"]], "0001") 
        # Yo espero que el resultado sea '["1111", "0000"]'
        # Si no me da ese resultado entonces me tiene que tirar un error y decirme cual fue
        ### el resultado real.       
        self.assertEqual(result, ["1111", "0000"])

##Clase de pruebas automatizadas de la memoria
class TestMemory(unittest.TestCase):

    def test_data_load(self):
        m = memory.memory()
        m.data()        

if __name__ == '__main__':
    #Si test.py está corriendo como dependencia entonces no correr las siguientes lineas:
    unittest.main()