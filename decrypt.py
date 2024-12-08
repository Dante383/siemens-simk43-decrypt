import sys, array
from pathlib import Path

LOOKUP_TABLE = {
        0: 3,
        1: 11,
        2: 2,
        3: 10,
        4: 1,
        5: 9,
        6: 0,
        7: 8,
        8: 12,
        9: 4,
        10: 13,
        11: 5,
        12: 14,
        13: 6,
        14: 15,
        15: 7
}

def decode_word(inw, lut):
    result = 0

    for i in range(16):
        if inw & (1 << i) != 0:
            result += 1 << lut[i]

    return result

def process (input_filename, output_filename, lut):
	with open(input_filename, 'rb') as file:
		with open(output_filename, 'wb') as output:
			while True:
				chunk = file.read(2)
				if not chunk:
					break

				decoded = decode_word(int.from_bytes(chunk, "big"), lut)
				output.write(decoded.to_bytes(2, "big"))
	print('Saved to {}'.format(output_filename))

def print_help ():
	print('''Usage:
	Decryption:  
		{} d <filename> 
	Encryption:
		{} e <filename>'''.format(sys.argv[0], sys.argv[0]))
	sys.exit(1)

if __name__ == '__main__':
	if (len(sys.argv) < 3):
		print_help()

	input_filename = sys.argv[2]

	if (sys.argv[1] == 'd'): # decrypt
		output_filename = '.'.join(input_filename.split('.')[:-1]) + '_decrypted.bin'
		LUT = {v: k for k, v in LOOKUP_TABLE.items()}        
		process(input_filename, output_filename, LUT)
	elif (sys.argv[1] == 'e'): # encrypt
		output_filename = '.'.join(input_filename.split('.')[:-1]) + '_encrypted.SIE'
		process(input_filename, output_filename, LOOKUP_TABLE)
	else:
		print_help()
