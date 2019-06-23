def geometric_mean(numbers):
    product = 1
    for n in numbers:
        product *= n
    return product ** (1.0/len(numbers))
        
    
print(geometric_mean([1,2,3,4,5]))


