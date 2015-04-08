RSA_Encryption
==============

I decided to implement the famous RSA encryption in python. I had fun doing it. Obviously I had to use  some well known  methods to allow python to quickly generate huge primes. I took the code for the Rabin Miller and the generation of huge prime from elsewhere, but aside from that, the rest is done by me.

All modules are fully functional and tested for python 3.4.1. 

Unfortunately, the generation of the huge primes is done with Mersenne Twister which is deterministic. Until I implement a cryptographically secure generation of random numbers, this project should not be used for serious cryptographic purposes.

Instructions:

To encrypt a message, run main.py and follow the prompts/instructions.
To decrypt a message given that you have the keys, run decrypt.py.

This project was mostly done out of my own curiosity because of my interest in RSA and is not intended for serious cryptographic purposes.
That being said, you may use the code found in this repository in part or whole as you wish. Please submit a pull request if you feel there should be any modifications/changes. 
