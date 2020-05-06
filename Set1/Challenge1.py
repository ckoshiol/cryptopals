#!/usr/bin/python3

'''

CryptoPals Set 1 Challenge 1
Convert hex to base64
https://cryptopals.com/sets/1/challenges/1

'''

import base64

def hex_to_b64(hex_string):
    return base64.b64encode(bytes.fromhex(hex_string)).decode()

def main():
    input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    output = hex_to_b64(input)
    print("Output: " + output)

if __name__ == "__main__":
    main()