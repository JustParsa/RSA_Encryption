from fractions import gcd
from gnt_prime import generateLargePrime
from gnt_prime import inp
from EEA import EEA
from convert_to import convert_to_ascii
from convert_to import convert_to_hex
from write_to_file import write_to_file
import cipher
import math

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

raw_message = input("Please enter a message to be encrypted: ")
m = convert_to_hex(raw_message)  #encoded hex message to be used for RSA

#d * e = 1 (mod O) => linear diophantine: e(d) + O(y) = 1 -- trying to find d
#Implement Extended Euclidean Algorithm 
d = EEA (O , e, 1, 0, 0, 1)

#prevent d with negative value
if d < 0: 
	d += (1 + abs(d)//O)*O

c = cipher.encrypt (m, e, n)

write_to_file(raw_message, m, c, n, e, d)
