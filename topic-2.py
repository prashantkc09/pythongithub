from functools import reduce

list1=[3,2,8,16,11,34,17]

output=list(filter(lambda i : i%2==0,
list1))
output2=list(map(lambda i:i**2,list1))

output3=reduce(lambda a,b:a+b,list1)
print(output3)