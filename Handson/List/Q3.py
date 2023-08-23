n=int(input("Enter the Count of Values: "))
list1 = []
outlist = []
for i in range(n):
    list1.append(int(input("Enter the Value in a List: ")))
for j in list1:
    if j%5==0:
        outlist.append(j)
print(list1)
print(outlist)