n, k=input("").split(" ")
arr=[]
sum=0
for i in range(1,(int(n)+1)):
    arr.append(i)
for j in range(0,int(k)):
    sum+=arr[j]
print(sum)