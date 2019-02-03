a=int(input("Enter the Number: "))
b=a
c=0
while a!= 0:
    c+=(a%10)**3
    a=a//10
if(b==c):
    print("yes")
else:
    print("no")