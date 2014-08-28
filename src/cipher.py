#Encryption
#C - ciphertext; m - message; 

#We know c = m^e (mod n)
def encrypt (m, e, n):
	c = int((m**e)) % n
	return c

#We know m = c^d (mod n)
def decrypt (c, d, n):
	m = int((c**d)) % n #This is not fast enough. Use wikipedia algo.
	return m
	
