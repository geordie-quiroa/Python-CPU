import controlUnit
import unittest
import memory

##Clase de pruebas automatizadas del CPU
class TestCPU(unittest.TestCase):    

    def test_reader(self):
        _cu = controlUnit.ControlUnit()     
        # La variable /_result/ va a retornar el text del archivo 'test.code'
        _result = _cu.FileReader("test.code")
        # Yo espero que el _resultado sea '00001111\n11110000\n10100000\n11100111'
        # Si no me da ese _resultado entonces me tiene que tirar un error y decirme _cual fue
        ### el _resultado real.
        self.assertEqual(_result, "00001111\n11110000\n10100000\n11100111")

    def test_separator(self):
        _cu = controlUnit.ControlUnit()
        # La variable /_result/ va a retornar el string separado de 4 caracters en 4
        _result = _cu.InstructionsSeparator("0000111111110000")
        # Yo espero que el _resultado sea '[["0000","1111"], ["1111", "0000"]]'
        # Si no me da ese _resultado entonces me tiene que tirar un error y decirme _cual fue
        ### el _resultado real.
        self.assertEqual(_result, [["0000","1111"], ["1111", "0000"]])
    
    def test_fetcher(self):
        _cu = controlUnit.ControlUnit()
        # La variable /_result/ va a retornar el item en la posicion 1 (que esta dada en binario)
        _result = _cu.InstructionFetcher([["0000","1111"], ["1111", "0000"]], "0001") 
        # Yo espero que el _resultado sea '["1111", "0000"]'
        # Si no me da ese _resultado entonces me tiene que tirar un error y decirme _cual fue
        ### el _resultado real.       
        self.assertEqual(_result, ["1111", "0000"])

##Clase de pruebas automatizadas de la memoria
class TestMemory(unittest.TestCase):

    def test_data_load(self):
        _m = memory.memory()
        _m.data()

if __name__ == '__main__':
    #Si test.py está corriendo como dependencia entonces no correr las siguientes lineas:
    unittest.main()