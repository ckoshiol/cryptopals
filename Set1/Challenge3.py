#!/usr/bin/python3

'''

CryptoPals Set 1 Challenge 3
Single-byte XOR cipher
https://cryptopals.com/sets/1/challenges/3

'''

def single_char_xor(input, key_ascii):
    plaintext = b''
    for byte in bytes.fromhex(input):
        plaintext += bytes([byte ^ key_ascii])
    return (plaintext)

def get_score(potential_plaintext):
    # frequency values are from http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
    frequency = {'e': 12.02, 't': 9.10, 'a': 8.12, 'o': 7.68, 'i': 7.31, 'n': 6.95,
                 's': 6.28, 'r': 6.02, 'h': 5.92, 'd': 4.32, 'l': 3.98, 'u': 2.88,
                 'c': 2.71, 'm': 2.61, 'f': 2.30, 'y': 2.11, 'w': 2.09, 'g': 2.03,
                 'p': 1.82, 'b': 1.49, 'v': 1.11, 'k': .69, 'x': .17, 'q': .11,
                 'j': .10, 'z': .07}
    
    score = 0
    for byte in potential_plaintext:
        value = frequency.get(chr(byte), 0)
        score += value

    return(score)

def main():
    input = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    data = []
    for key_ascii in range(256):
        potential_plaintext = single_char_xor(input, key_ascii)
        score = get_score(potential_plaintext)
        data_entry = {'plaintext': potential_plaintext, 'key_char': chr(key_ascii), 'key_ascii': key_ascii, 'score': score}
        data.append(data_entry)
    
    # display only the top 5 scoring data entries for easier reading
    top_scores = sorted(data, key = lambda s: s['score'],reverse=True)
    for i in range(5) : print(top_scores[i])

if __name__ == "__main__":
    main()