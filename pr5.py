from random import randint

# Prime number P and primitive root G
P = 23
G = 9

print("The value of P is: %d" % P)
print("The value of G is: %d" % G)

# Alice chooses her secret number
a = randint(1, P)
print("Secret number for Alice is: %d" % a)

# Bob chooses his secret number
b = randint(1, P)
print("Secret number for Bob is: %d" % b)

# Alice calculates her public value (X = G^a mod P)
x = pow(G, a, P)

# Bob calculates his public value (Y = G^b mod P)
y = pow(G, b, P)

# Alice and Bob exchange their public values and compute the shared secret key
# Alice calculates the shared secret key (K_A = Y^a mod P)
ka = pow(y, a, P)

# Bob calculates the shared secret key (K_B = X^b mod P)
kb = pow(x, b, P)

print("Secret key for Alice is: %d" % ka)
print("Secret key for Bob is: %d" % kb)
