from random import random
#pulled from the example file on your page/video

def getSamp(data, sample_size):
    random_values = random.sample(data, k=sample_size)
    return random_values