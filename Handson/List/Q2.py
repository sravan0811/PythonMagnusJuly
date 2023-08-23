a=int(input("Enter the List Count of Values: "))
list1 = []
for i in range(a):
    b=input("Enter the Value into a List: ")
    list1.append(b)
print(list1)
print(list1[:3]+list1[-3:])