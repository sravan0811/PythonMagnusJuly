n = int(input("Enter the Value of n: "))
t = int(input("Enter the Value of t: "))
list1 = []
for i in range(n):
    a=int(input("Enter the Value in first List: "))
    list1.append((a))
for j in range(t):
    b=int(input("Enter the Value in second List: "))
    print(list1[b])