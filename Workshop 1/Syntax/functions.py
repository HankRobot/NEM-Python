def geometric_mean(numbers):
    product = 1
    for n in numbers:
        product *= n
    return product ** (1.0/len(numbers))

def helloworld():
    print('hi')

helloworld()


