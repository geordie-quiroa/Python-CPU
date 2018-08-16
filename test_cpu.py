import controlUnit
import unittest

##Clase de pruebas automatizadas
class TestCPU(unittest.TestCase):    

    def test_reader(self):
        cu = controlUnit.ControlUnit()
        result = cu.FileReader("test.code")
        self.assertEqual(result, "00001111")

    def test_separator(self):
        cu = controlUnit.ControlUnit()
        result = cu.InstructionsSeparator("0000111111110000")
        self.assertEqual(result, [["0000","1111"], ["1111", "0000"]])
    
    def test_fetcher(self):
        cu = controlUnit.ControlUnit()
        result = cu.InstructionFetcher([["0000","1111"], ["1111", "0000"]], "0001")
        self.assertEqual(result, ["1111", "0000"])
        

if __name__ == '__main__':
    #Si test_cpu.py está corriendo como dependencia entonces no correr las siguientes lineas:
    unittest.main()