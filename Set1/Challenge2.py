#!/usr/bin/python3

'''

CryptoPals Set 1 Challenge 2
Fixed XOR
https://cryptopals.com/sets/1/challenges/2

'''

def fixed_xor(hex_string1, hex_string2):
    if len(hex_string1) != len(hex_string2):
        return ("Inputs are not of equal length")
    
    bytes1 = bytes.fromhex(hex_string1)
    bytes2 = bytes.fromhex(hex_string2)
    bytes_ciphertext = bytes(byte1 ^ byte2 for byte1, byte2 in zip(bytes1, bytes2))
    
    return (bytes_ciphertext.hex())

def main():
    input1 = '1c0111001f010100061a024b53535009181c'
    input2 = '686974207468652062756c6c277320657965'
    output = fixed_xor(input1, input2)
    print("Output: " + output)

if __name__ == "__main__":
    main()