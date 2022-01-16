import numpy
str = []
def arrays(arr):
    array1 = numpy.array(arr)
    reversed_arr = array1[::-1]   
    reversed_arr = reversed_arr.astype('float64')
    return reversed_arr
        
     
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
