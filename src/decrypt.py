from cipher import decrypt
from convert_to import convert_to_ascii

n = input("Please enter the first key of the private key pair: ")
#n = input("Please enter n, the modulus for both the public and private keys. This is the first key in the key pairs for both the public and private keys: ")
d = input("Please enter the second key of the private key pair: ")
c = input("Finally, please enter the ciphertext: ")

print("The decrypted message is: ")
#decrypt cipher, then convert to hex, then convert to ascii, and print the result
print(convert_to_ascii(format(decrypt(int(c),int(d),int(n)),'x')))

print("\n\nIf you believe the decrypted message is incorrect, it's because you failed to enter the keys properly. Make sure there are no spaces or EOLs in your input.")
