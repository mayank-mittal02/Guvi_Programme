a, d=input("Enter the Number: ").split(" ")
for i in range(int(a),int(d)):
    c=0
    b=i
    while i!= 0:
        c+=(i%10)**3
        i=i//10
    if(b==c):
        print(b,end=" ")
    else:
        pass