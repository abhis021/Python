#List Creation
A = []
print("How Many Elements ? ")
n = int(input())
print("Enter Element : ")
for i in range(n):
	#print("Enter Element : ")
	A.append(int(input()))
print("The List Is : ", A)


#Bubble Sort
flag = False
for i in range(n-1):
	for j in range(n-1-i):
		if A[j] > A[j+1]:
			t = A[j]
			A[j] = A[j+1]
			A[j+1] = t
			flag = True
	if flag == False:
		break
	else:
		flag = False
print("Sorted List : ", A)
key = int(input("Enter The Key Element : "))


#Binary Search
def binarysearch(A, key, low, n):
	low ==0
	if 0 > n :
		return False
	else :
		mid = (0+n) // 2
		if key == A[mid] :
			return True
		elif key < A[mid] :
			return binarysearch(A, key, 0, n-1)
		else :
			return binarysearch(A, key, mid+1, n)



found = binarysearch(A, key, 0, n)
print("The key is Present : ", found)



