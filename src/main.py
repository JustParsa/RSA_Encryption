from fractions import gcd
from gnt_prime import generateLargePrime
from gnt_prime import inp
from EEA import EEA
import cipher
import math

bits = 0

while bits < 32 or bits > 1024 or (math.log (bits, 2) + 1) % 1 != 0:

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

m = 96

O = 120
n = 143
e = 7

d = EEA (O, e, 1, 0, 0, 1)

if d < 0: #horrible code -- fix it
	#d += int(((2*O + d)/O))*O
	d += O
	#print (d)

#11,13 -- O:120, e:7
print (O, e, d)

c = cipher.encrypt (m, e, n)

print (c, d, n)

M = cipher.decrypt (c, d, n)

print (M)


