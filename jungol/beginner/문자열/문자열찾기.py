import sys

sys.stdin = open('input.txt', 'r')
s = input()

koi_cnt =0
ioi_cnt =0

for idx, char in enumerate(s):
    if char == 'K':
        if s[idx:idx+3] == "KOI": koi_cnt +=1
    
    elif char == 'I':
        if s[idx:idx+3] == "IOI": ioi_cnt +=1
    
print(koi_cnt)
print(ioi_cnt)