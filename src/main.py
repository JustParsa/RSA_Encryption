from fractions import gcd
from gnt_prime import generateLargePrime
from gnt_prime import inp
from EEA import EEA
from convert_to import convert_to_ASCII
from convert_to import convert_to_decimal
import cipher
import math
import pdb

bits = 0

while bits < 32 or bits > 2048 or (math.log (bits, 2) + 1) % 1 != 0:

  bits = inp()

p = generateLargePrime(int(bits/2))
q = generateLargePrime(int(bits/2))

n = int(p*q) #key length

O = (p-1)*(q-1) #Euler's totient function

e = 2**16 + 1 #Default value -- a well known prime that works well most of the time

if gcd (e,O) != 1: #must be coprime
    e = generateLargePrime (17)

#d * e = 1 (mod O) => linear diophantine: e(d) + O(y) = 1 -- trying to find d

#Implement Extended Euclidean Algorithm 

#message
m = 90
#m = convert_to_decimal(input("Please enter your message to be encrypted :"))
# test values for debug
# O = 120
# n = 143
# e = 7

d = EEA (O , e, 1, 0, 0, 1)

#prevent d with negative value
if d < 0: 
	d += (1 + abs(d)//O)*O

c = cipher.encrypt (m, e, n)

f1 = open("cipher.txt", 'w')
f1.write(str(c))
f1.close()

# print (c, d, n) --debug

M = cipher.decrypt (c, d, n)
print(M)
#print(c)
#print (convert_to_ASCII(M))
#print('n:', n)
#print('d:', d)
#print('O:', O)
