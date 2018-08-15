import controlUnit
import unittest

class TestCPU(unittest.TestCase):

    def test_parser(self):
        result = controlUnit.Parser('0101')
        self.assertEqual(result, 'Hello 0101')

if __name__ == '__main__':
    unittest.main()