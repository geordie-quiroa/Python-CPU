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

##Clase de pruebas automatizadas de la memoria
class TestMemory(unittest.TestCase):

    def test_data_load(self):
        _m = memory.memory()
        _result = _m.data().instructions
        self.assertEqual(_result, ['00001111','11110000','10100000','11100111'])   


if __name__ == '__main__':
    #Si test.py está corriendo como dependencia entonces no correr las siguientes lineas:
    unittest.main()