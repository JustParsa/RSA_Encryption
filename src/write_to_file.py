def write_to_file(raw_message, encoded_message, ciphertext, n, e, d):
  with open ('RSA.txt', 'a') as f:
    f.write('RAW MESSAGE: \n')
    f.write('\"'+ raw_message + '\"' + '\n\n')
    f.write('ENCODED MESSAGE (HEXADECIMAL): \n')
    f.write(encoded_message + '\n\n')
    f.write('CIPHERTEXT: \n')
    f.write(str(ciphertext) + '\n\n')
    f.write('PUBLIC KEY:\n')
    f.write('({0} , {1})\n\n'.format(n,e))
    f.write('PRIVATE KEY:)\n')
    f.write('({0} , {1})\n\n'.format(n,d))
    f.write('==================================================\n\n')
