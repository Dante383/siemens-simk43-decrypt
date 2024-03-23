import struct

plain_file = 'reference_plain.bin'
encrypted_file = 'reference_encrypted.SIE'
lut_file = 'lut.bin'

LOOKUP_TABLE = {}

with open(plain_file, 'rb') as plain_file:
	with open(encrypted_file, 'rb') as encrypted_file:
		while True:
			key = plain_file.read(2)
			if not key:
				break
			key = int.from_bytes(key, "big")
			value = int.from_bytes(encrypted_file.read(2), "big")
			LOOKUP_TABLE[key] = value

with open(lut_file, 'wb') as f:
	for _,v in LOOKUP_TABLE.items():
		f.write(struct.pack('<H', v))
