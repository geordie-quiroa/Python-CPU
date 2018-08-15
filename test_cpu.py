import controlUnit
import unittest

class TestCPU(unittest.TestCase):

    def test_add_integers(self):        
        result = controlUnit.HelloPerson('Juan')
        self.assertEqual(result, 'Hello Juan')

if __name__ == '__main__':
    unittest.main()