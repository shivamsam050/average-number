n= int(input("enter the Nth Number:"))
sum=0
for i in range(1,n+1):
    x=int(input("enter th number"))
    sum = sum+x
avg = float(sum/n)
print("\n average of ",n," is ",avg)
    