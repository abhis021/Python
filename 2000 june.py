thisset = ("apple", "banana", "cherry")
print(thisset)
for x in thisset:
    print(x)
print("banana" in thisset)
thisset.add("orange")
print(thisset)
thisset.remove("banana")
print(thisset)
thisset.discard("banana")
print(thisset)
thisset = ("apple", "banana", "cherry")
x = thisset.pop()
print(x)
print(thisset)

