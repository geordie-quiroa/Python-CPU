import controlUnit
import unittest
import memory

##Clase de pruebas automatizadas del CPU
#class TestCPU(unittest.TestCase):
##Clase de pruebas automatizadas de la memoria
class TestMemory(unittest.TestCase):

#    def test_data_load(self):
#        _m = memory.memory()
#        _result = _m.data().instructions
#        self.assertEqual(_result, ['00001111','11110000','10100000','11100111'])

if __name__ == '__main__':
    #Si test.py está corriendo como dependencia entonces no correr las siguientes lineas:
    unittest.main()