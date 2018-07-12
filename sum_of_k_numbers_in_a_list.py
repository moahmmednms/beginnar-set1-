n=input()
b=n.split()
sum=0
list=[]
for i in range(int(b[0])):
    a=int(input())
    list.append(a)
for i in range(int(b[1])):
    sum=sum+list[i]
print(sum)


