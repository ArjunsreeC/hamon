import unittest
import os
from q1 import get_contents

class TestGetContents(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for testing
        self.test_file = 'test_file.txt'
        with open(self.test_file, 'w') as f:
            f.write('Hello, world!')

    def tearDown(self):
        # Remove the temporary file after the test
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass

    def test_file_exists(self):
        # Test reading from an existing file
        content = get_contents(self.test_file)
        self.assertEqual(content, 'Hello, world!')

    def test_file_not_exists(self):
        # Test reading from a non-existing file
        content = get_contents('non_existent_file.txt')
        self.assertIsNone(content)

    def test_file_permission_error(self):
        # Test reading a file without proper permissions
        protected_file = 'protected_file.txt'
        try:
            with open(protected_file, 'w') as f:
                f.write('This file is protected.')
            os.chmod(protected_file, 0o000)  # Remove all permissions
            content = get_contents(protected_file)
            self.assertIsNone(content)
        finally:
            os.chmod(protected_file, 0o666)  # Restore permissions so it can be deleted
            os.remove(protected_file)

if __name__ == '__main__':
    unittest.main()
