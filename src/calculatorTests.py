import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint
#Sourced from example file

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data = CsvReader('/src/subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_results_property(self):
        calculator = Calculator()
        calculator.add(2,1)
        self.assertEqual(self.calculator.result, 3)


if __name__ == '__main__':
    unittest.main()