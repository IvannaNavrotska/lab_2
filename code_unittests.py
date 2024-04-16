import unittest
import code
import sys
import io

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
        self.assertFalse(code.fibonacci(5.87))

    
    def setUp(self):
        self.stdin_backup = sys.stdin
        self.stdout_backup = sys.stdout
        self.stderr_backup = sys.stderr
    
    def tearDown(self):
        sys.stdin = self.stdin_backup
        sys.stdout = self.stdout_backup
        sys.stderr = self.stderr_backup
    
    def test_main_without_errors(self):

        input_0 = "6\n"
        expected_output = "13\n"

        sys.stdin = io.StringIO(input_0)
        sys.stdout = io.StringIO()

        with self.assertRaises(SystemExit) as cm:
            code.main()

        self.assertEqual(cm.exception.code, 0)
        self.assertEqual(sys.stdout.getvalue(), expected_output)
    
    def test_main_with_errors(self):
        test_cases = [
            ("six\n", "Error: Forgot about letters! Input must be an integer \n"),
            (" ", "Error: Wait, your input cannot be empty! \n") ]

        for input_data, expected_error_message in test_cases:
            sys.stdin = io.StringIO(input_data)
            sys.stdout = io.StringIO()
            sys.stderr = io.StringIO()

            with self.assertRaises(SystemExit) as cm:
                code.main()

            self.assertEqual(cm.exception.code, 1)
            self.assertEqual(sys.stderr.getvalue(), expected_error_message)


if __name__ == '__main__':
    unittest.main()
