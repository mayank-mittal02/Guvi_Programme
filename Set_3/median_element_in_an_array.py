n=int(input("enter the number of element: "))
l=[]
for i in range(0,n):
    l.append(int(input("")))
l=sorted(l)
print(l[((n+1)//2)-1])