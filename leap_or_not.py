leap=int(input())
if(leap%4==0):
    if(leap%100==0):
        if(leap%400!=0):
            print("yes")
        else:
            print("No")
    else:
        print("yes")
else:
    print("no")
    
