person1=int(input("enter the age of 1st person: "))
person2=int(input("enter the age of 2nd person: "))
person3=int(input("enter the age of 3rd person: "))


if person1>person2 and person1>person3:
    print("the oldest is", person1)

elif person2<person1 and person2>person3:
    print("the oldest is",person2)

elif person1<person3 and person2<person3:
    print("the oldest is",person3)

else:
    print("all have same age") 
