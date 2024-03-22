# Siemens EEPROM Decoder 

This is a tool used to encrypt and decrypt EEPROM dumps from early 90's Siemens ECUs. 
Tested and developed on [SIMK41/43](https://github.com/Dante383/GKFlasher) but certainly applies to a lot 
more ECUs from that era. If you test it out on a ECU different than SIMK41/43 - let me know, I'll update the readme.

## Usage 

Decryption:

	python3 decrypt.py d <filename>
Output will be saved to <filename>_decrypted.bin

Encryption:
	python3 decrypt.py e <filename>
Output will be saved to <filename>_encrypted.SIE

## How does it work? 

Analyzing the pattern from the lookup table it seems like there is some bit-flip operation going on with an extra twist but there wasn't any need to go any further.

Encryption is treated as a substitution cipher with 2 byte long keys. A binary file counting up from 0x0000 to 0xFFFF was generated (available in tools/reference_plain.bin)
and encrypted (tools/reference_encrypted.SIE). Then, the build_lookup_table.py script was used to read both files 2 bytes at a time and generate the 65k entry-long lookup table.
You should be able to use this approach with other _encryption_ mechanisms from that era.