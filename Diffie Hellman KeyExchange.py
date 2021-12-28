#Nishaant Goswamy

import cryptAlg as crypt

print("This is Diffie Hellman Key Exchange")
p = int(input("Enter a prime number p: "))

if not crypt.primeCheck(p): quit()

g = crypt.Generator(p-1, p)
print("Generator g:", g)

a = int(input("Alice select secret key (enter a int): "))

b = int(input("Bob select secret key (enter a int): "))

AlicePublicKey = crypt.Square_And_Multiply(g, a, p)
print("Alice's public key:", AlicePublicKey)

BobPublicKey = crypt.Square_And_Multiply(g, b, p)
print("Bob's public key:", BobPublicKey)

AliceSecretKey = crypt.Square_And_Multiply(BobPublicKey, a, p)
print("Alice's secret key:", AliceSecretKey)

BobSecretKey = crypt.Square_And_Multiply(AlicePublicKey, b, p)
print("Bob's public key:", BobSecretKey)

if AliceSecretKey == BobSecretKey:
    print("Success!! Alice and Bob have the same key. ", AliceSecretKey,"==", BobSecretKey)