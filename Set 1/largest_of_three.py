a=eval(input("Enter the First Number: "))
b=eval(input("Enter the Second Number: "))
c=eval(input("Enter the Third Number: "))
if a>b:
    if a>c:
        print("largest number is: ",a)
    else:
        print("largest number is: ",c)
elif b>c:
    print("largest number is: ",b)
else:
    print("largest number is: ",c)