a=int(input('Enter the number: '))
b=a
reverse=0
while a!= 0:
    reverse=(reverse*10)+(a%10)
    a=a//10
if(b==reverse):
    print("yes")
else:
    print("no")