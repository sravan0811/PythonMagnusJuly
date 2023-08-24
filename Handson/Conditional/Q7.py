digit = int(input("Enter the two Digit Number: "))
a=str(digit)
b=int(a[0])+int(a[1])
if b==7 or a[0]==7 or a[1]==7 or (digit%7)==0:
    print("Special Number")
else:
    print("Not a Special Number")
