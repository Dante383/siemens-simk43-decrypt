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

In SIMK41/43's case, EEPROM data lines are crossed. Due to this, in every pair of bytes, bits are switched as so: 

	0  -  3
	1  -  11
	2  -  2
	3  -  10
	4  -  1
	5  -  9
	6  -  0
	7  -  8
	8  -  12
	9  -  4
	10  -  13
	11  -  5
	12  -  14
	13  -  6
	14  -  15
	15  -  7

In hardware variant 5WY19, there's a NXP 74HCT574D chip on the PCB responsible for unscrambling the data.

For more information about SIMK41/SIMK43 ECUs, visit https://opengk.org
