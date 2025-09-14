a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("Choose Arithmetic operation\n1 for addition\n2 For subtraction\n3 For multiplication\n4 For division")
ch=int(input("Enter your choice:"))
while ch!=1 and ch!=2 and ch!=3 and ch!=4:
    print("Please enter valid input")
    ch=int(input("Enter your choice again:"))
else:
    if ch==1:
        print("Addition of ",a," and ",b," is:",a+b)
    elif ch==2:
        print("Subtraction of ",a," and ",b," is:",a-b)
    elif ch==3:
        print("Multiplication of ",a," and ",b," is:",a*b)
    elif ch==4:
        if b==0:
            print("Cannot divide by 0")
        else:
            print("Division of ",a," and ",b," is:",a/b)