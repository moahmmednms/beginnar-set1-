a=input()
b=a.split()
c=input()
d=c.split()
sum=0
for i in range(int(b[1])):
    sum=sum+int(d[i])
print(sum)
