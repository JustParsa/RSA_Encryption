#Returns decimal representation of a message to feed into RSA
def convert_to_hex (message):
  hex_arr = []
  for letter in message:
    hex_arr.append(str(format(ord(letter),'x').zfill(2)))
  return ''.join(hex_arr)

def convert_to_ascii(hex_input):
  hex_input = str(hex_input)
  chr_arr = []
  #iterate over the string and group two characters at a time (since all ascii chars will be two hex chars)
  num_digits = 2
  for i in range(0, len(hex_input), num_digits):
    hex_number = hex_input[i:i+num_digits]
    chr_arr.append(chr(int(hex_number, 16)))
  return ''.join(chr_arr)
