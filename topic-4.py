#list1=[34,88,30,22,10,15,18]
#print out all the ,ultiples of 5 using filtert and lambda

list1=[34,88,30,22,10,15,18]
output=list(filter(lambda i : i%5==0,
list1))
print(output)