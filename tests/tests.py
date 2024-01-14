import unittest
from modules import FizzBuzzCompute


class TestFizzBuzzEvaluations(unittest.TestCase):

    def test_fizzbuzz_result(self):
        # Arrange
        n1 = 3
        n2 = 5
        limit = 20
        str1 = "fizz"
        str2 = "buzz"

        # Act
        actual_result = FizzBuzzCompute.GetFizzBuzzResult(n1, n2, limit, str1, str2)
        expected_result = "1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz,16,17,fizz,19,buzz"

        # Assert
        self.assertEqual(actual_result, expected_result, "The result is incorrect, test failed!")


if __name__ == "__main__":
    unittest.main()
