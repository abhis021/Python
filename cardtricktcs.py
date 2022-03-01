#number of elements
n=int(input())
#below reads inputs from user using map()
a=list(map(int,input().split()))[:n]

def arraySortedOrNot(a):
    n=len(a)

    if n==1 or n==0:
        return True
    return a[0]<=a[1] and arraySortedOrNot(a[1:])
if arraySortedOrNot(a):
    print("Yes")
else:
    print("No")