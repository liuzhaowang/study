from ddt import ddt, data ,file_data,unpack
import unittest,os,csv



from ddt_test.calculator import Calculator

def csv_reader(file):
    if not os.path.exists(file):
        return None
    with open(file,'r') as f:
        result = csv.reader(f)
        content = []
        for item in result:
            elements = []
            for i in item:
                elements.append(Calculator.aton(i))
            # print(elements)
            content.append(elements)
        return content
@ddt
class CalculatorTestCase(unittest.TestCase):

    @data([8,5,3],[15,8,7],[16,8,8])
    @unpack
    def test_add(self,expected,num1,num2):
        result = Calculator.add(num1,num2)
        self.assertEqual(result,expected)

    @data(*csv_reader('./data/sub_data.csv'))
    @unpack
    def test_sub(self,expect,num1,num2):
        result = Calculator.sub(num1,num2)
        self.assertEqual(result,expect)

    @file_data('./data/multi_data')
    @unpack
    def test_multi(self,expect,num1,num2):
        result = Calculator.multi(num1,num2)
        self.assertEqual(result,expect)

    @file_data('./data/div_data.yaml')
    @unpack
    def test_div(self,expected,num1,num2):
        result = Calculator.div(num1,num2)
        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
    # csv_reader('./data/sub_data.csv')