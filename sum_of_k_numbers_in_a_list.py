n=int(input())
k=int(input())
sum=0
list=[]
for i in range(n):
    a=int(input())
    list.append(a)
for i in range(k):
    sum=sum+list[i]
print(sum)


