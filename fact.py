p=int(input("Enter the numbers to be fact  "))
fact1=[]
fact2=[]
s=1
for i in range(0,p):
    ls1=int(input())
    fact1.append(ls1)
for j in fact1:
    for k in range(1,j+1):
        s = s * k
    fact2.append(s)
    s = 1

print(fact2)