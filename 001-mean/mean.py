import random

def mean(input_list):
    n = len(input_list)
    sum = 0.0
    for i in range(0, n):
        sum += input_list[i]
    return sum / n


input_list = []
# use a seed to always return the same values (remember that algorithm is pseudo random)
# random.seed(42)
for i in range(100):
    input_list.append(random.randrange(0, 100))

mean = mean(input_list)
print('list = ', input_list)
print('mean = ', mean)
