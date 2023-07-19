n=int(input())
c=""
while n>0:
    c=str(n%2)+c
    n//=2
count=0
for i in range(len(c)):
    if(c[i]=='1'):
        count+=1
print(count)
