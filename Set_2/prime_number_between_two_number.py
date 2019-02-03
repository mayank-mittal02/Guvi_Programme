n,q=input("Enter two numbers: ").split()
for i in range(int(n),int(q)):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            print(i,end=" ")