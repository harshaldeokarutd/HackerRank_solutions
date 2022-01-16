import numpy
arr = input().strip().split(' ')

y = numpy.array([arr])
y = y.astype("int64")
print (numpy.reshape(y,(3,3)))
