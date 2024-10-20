import unittest
from average_two_numbers import average_two_numbers

class TestAverage(unittest.TestCase):
    def test_2_3(self):
        result = average_two_numbers(1,19)
        self.assertEqual(result, 10)


if __name__ == "__main__":
    unittest.main()


