import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint
#Sourced from example file

class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator=Calculator()
        self.assertIsInstance(self.calculator, Calculator)

    def setUp(self) -> None:
        self.calculator = Calculator()
    def test_subtraction(self):
        test_data = CsvReader('/src/csvTests/Unit Test Subtraction.csv').data
        for row in test_data:
            myCalc = Calculator()
            myResult = myCalc.subtract((int(row['Value 1'])),(int(row['Value 2'])))
            self.assertEqual(((int(row['Result']))),(myResult))

            #self.assertEqual(self.calculator.result, int(row['Result']))
    #def test_instantiate_calculator(self):
        #self.assertIsInstance(self.calculator, Calculator)
    #def test_results_property(self):
        #self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()