#Encryption
#C - ciphertext; m - padded message; 
#exponentiation by squaring is not necessary because of python's awesome 3-arg pow()

#We know c = m^e (mod n)
def encrypt (m, e, n):
	c = pow (m ,e ,n)
	return c

#We know m = c^d (mod n)
def decrypt (c, d, n):
	m = pow(c, d, n)
	return m
	