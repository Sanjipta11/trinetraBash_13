# map-- map(function_name,collection)
# li = [10,23,46,89,78,]
# var = list(map(lambda n:n+5,li))
# print(var)
from functools import reduce

#

# from function import reduce
li = [10,23,46,89,78,]
var = reduce(lambda a,b:a+b,li)
print(var)