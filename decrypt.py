import sys, array
from pathlib import Path

def process (input_filename, output_filename, lut):
	with open(input_filename, 'rb') as file:
		with open(output_filename, 'wb') as output:
			while True:
				chunk = file.read(2)
				if not chunk:
					break

				decoded = lut[int.from_bytes(chunk, "big")]
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

	LOOKUP_RAW = array.array("H")
	with Path(__file__).with_name('lut.bin').open('rb') as lutfile:
		LOOKUP_RAW.fromfile(lutfile, 65536)

	LOOKUP_TABLE = {i: v for i,v in enumerate(LOOKUP_RAW)}

	if (sys.argv[1] == 'd'): # decrypt
		output_filename = '.'.join(input_filename.split('.')[:-1]) + '_decrypted.bin'
		LUT = {v: k for k, v in LOOKUP_TABLE.items()}        
		process(input_filename, output_filename, LUT)
	elif (sys.argv[1] == 'e'): # encrypt
		output_filename = '.'.join(input_filename.split('.')[:-1]) + '_encrypted.SIE'
		process(input_filename, output_filename, LOOKUP_TABLE)
	else:
		print_help()
