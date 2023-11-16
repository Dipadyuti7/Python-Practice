p=input("Enter the char to be masked ")#789561238
v=""
n=""
i=len(p)#9
if i<3:
    print("masking is not possible")
else:
    for j in range(i-6,i):
        v="*"
        n=n+v
print(p[0:i-6]+n)







