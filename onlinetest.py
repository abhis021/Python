b=3
c=4
d=5
for a in range(1,4):
    c=a+b
    if(((b+c)%10)!=0):
        c=c+a
    else:
        d=d+a
print(c)
print(d)