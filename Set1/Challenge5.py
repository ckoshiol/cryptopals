#!/usr/bin/python3

'''

CryptoPals Set 1 Challenge 5
Implement repeating-key XOR
https://cryptopals.com/sets/1/challenges/5

'''

def repeating_key_xor(plaintext, key):
    ciphertext = b''
    letter = 0
    for byte in plaintext.encode():
        ciphertext += bytes([byte ^ key.encode()[letter]])
        if (letter + 1) == len(key):
            letter = 0
        else:
            letter += 1
    
    return ciphertext

def main():
    input = 'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
    key = 'ICE'
    output = repeating_key_xor(input, key)
    print(output.hex())

if __name__ == "__main__":
    main()