rows = int(input("Enter the number of rows to create a pattern: "))
for num in range(rows):
    for i in range(2*num+1):
        print('*', end=" ")
    print(" ")
if rows >= 9:
    print("Impressive")
else:
    print("Nezumi XD")  