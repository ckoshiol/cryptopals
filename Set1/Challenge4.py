#!/usr/bin/python3

'''

CryptoPals Set 1 Challenge 4
Detect single-character XOR
https://cryptopals.com/sets/1/challenges/4

'''

from Challenge3 import single_char_xor, get_score

def get_message_top_score(input):
    data = []
    for key_ascii in range(256):
        potential_plaintext = single_char_xor(input, key_ascii)
        score = get_score(potential_plaintext)
        data_entry = {'plaintext': potential_plaintext, 'key_char': chr(key_ascii), 'key_ascii': key_ascii, 'score': score}
        data.append(data_entry)
    
    return(sorted(data, key = lambda s: s['score'],reverse=True)[0])

def main():
    data = []
    with open("4.txt") as potential_messages:
        line_count = 1
        line = potential_messages.readline()
        while line:
            data_entry = get_message_top_score(line.strip())
            # new value in the dataset to keep track of which line the message comes from
            data_entry['line'] = line_count
            data.append(data_entry)
            line_count += 1
            line = potential_messages.readline()
    
    # display only the top 5 scoring data entries for easier reading
    top_scores = sorted(data, key = lambda s: s['score'],reverse=True)
    for i in range(5) : print(top_scores[i])

if __name__ == "__main__":
    main()