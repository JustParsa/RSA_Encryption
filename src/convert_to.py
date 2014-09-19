#Returns decimal representation of a message to feed into RSA
def convert_to_decimal (message):

	chr_input = []

	for letter in message:
		chr_input.append (str(ord(letter)).zfill(3))	#Pad to 3 decimals to ensure consistent length

	M = ''.join (chr_input)

	return M

#Takes in a numeric message from RSA and decodes into readable ASCII
def convert_to_ASCII (M):

	a = 0
	M = str(M)
	num_arr = []
	char_arr = []

	for num in M:
		num_arr.append(num)

	while a != len (num_arr):

		char = ''

		for x in range (3):
			char += str(num_arr[x + a])

		char = chr(int(char))

		char_arr.append(char)

		a += 3		#Iterate to next sequence of numbers to convert to char

	message = ''.join (char_arr)

	return message