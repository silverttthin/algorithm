import sys
sys.stdin = open('input.txt','r')

key = input()
encrypted_sentence = input()

decoding_map = {}

asc = 97
for c in key:
    decoding_map[chr(asc)] = c
    asc+=1
decoding_map[" "] = " "

for encrypted_c in encrypted_sentence:
    try:
        print(decoding_map[encrypted_c], end="")
    except:
        tmp = ord(decoding_map[encrypted_c.lower()]) -32
        print(chr(tmp), end="")




