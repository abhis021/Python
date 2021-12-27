from pycipher import Caesar

p = input("Enter the plaintext: ")
k = int(input("Enter the key: "))
c = Caesar(k).encipher(p)
print("The ciphertext is: ", c)