import sys

sys.stdin = open('input.txt', 'r')
s = input()


for idx, c in enumerate(s): 
    if idx ==0: 
        h = 0
        h += 10
    else:
        prev = s[idx-1]
        if c == prev: h += 5
        elif c != prev: h +=10

print(h)

