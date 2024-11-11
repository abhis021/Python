# abc="bond"
# print("Hello", abc)
count =0
sum=0
print("before",count,sum)
for value in [9,41,12,3,74,15]:
    count+=1
    sum+=value
    print(count,sum,value)
print('after',count,sum,sum/count)