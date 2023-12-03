import unittest
from before import count_fruits, count_fruits2


class KissTest(unittest.TestCase):

    def setUp(self) -> None:
        self.test_input = [
            "apple",
            "banana",
            "apple",
            "cherry",
            "banana",
            "cherry",
            "apple",
            "apple",
            "cherry",
            "banana",
            "cherry",
        ]

    def test_fruit_count(self):
        expected_result = {"apple": 4, "banana": 3, "cherry": 4}
        result = count_fruits(self.test_input)
        self.assertDictEqual(result, expected_result)

    def test_fruit_count2(self):
        expected_result = {"apple": 4, "banana": 3, "cherry": 4}
        result = count_fruits2(self.test_input)
        self.assertDictEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()