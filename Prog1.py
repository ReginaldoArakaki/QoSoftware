import unittest

def add (x, y):
    return x + y


class TestAddFunc (unittest.TestCase):
    def test_add_numeros_positivos (self):
        self.assertEqual (add(2,3), 5)
        
    def test_add_numeros_negativos (self):
        self.assertEqual (add (-1, -1), -2)
        

if __name__ == '__main__':
    unittest.main()
    
