from Calculator.Calculator import addition
from Calculator.Calculator import division
import getSamp
#Pulled From Example Files
def sample_mean(data, sample_size):

    if(sample_size>0) and (sample_size <= data.len()):
        total = 0
        # check that get sample returns the proper number of samples
        # check that sample size is not 0
        # check that sample size is not larger than the population
        # https://realpython.com/python-exceptions/
        # https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
        sample = getSamp(data, sample_size)
        num_values = len(sample)
        for num in sample:
            total = addition(total,num)

        return division(total, num_values)
    else:
        raise Exception("Sample must be larger than 0 and no more than the sample size")
        #TO DO implement unit test that tests this exception
