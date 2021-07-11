from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.division import division

#Influenced by demo in instructional video
def median(num):
    try:
        num_values = len(num)
        list_num = [num[i] for i in range(num_values)]
        list_num.sort()
        if num_values % 2 < 1:
            temp1 = list_num[int(num_values // 2)]
            temp2 = list_num[int(subtraction((num_values // 2), 1))]
            median_result = division(addition(temp1, temp2), 2)
            return median_result
        else:
            median_result = list_num[int(division(num_values, 2))]
            return median_result
    except ZeroDivisionError:
        print("Cannot divide by 0") #the division function should catch this anyways.
    except ValueError:
        print("Wrong data type")