import unittest
import code

class TestCode(unittest.TestCase):


    def test_fibonacci(self):

        result = code.fibonacci(0)
        self.assertEqual(result, 1)

        result = code.fibonacci(1)
        self.assertEqual(result, 1)

        result = code.fibonacci(6)
        self.assertEqual(result, 13)

#it's time for negative testing

        result = code.fibonacci(5)
        self.assertNotEqual(result, 3)
        
        self.assertFalse(code.fibonacci('five'))  
        self.assertFalse(code.fibonacci(-5))
        self.assertFalse(code.fibonacci(' '))

if __name__ == '__main__':
    unittest.main()
