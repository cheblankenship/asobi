# Run the test file under 'python -m unittest tests.test_sample'
# python -m unittest tests.test_sample
import unittest
import sample

class TestSample(unittest.TestCase):
    def test_add(self):
        self.assertEqual(sample.add(1, 2), 3)

if __name__ == "__main__":
    unittest.main()
