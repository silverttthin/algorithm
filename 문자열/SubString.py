import sys
sys.stdin = open('input.txt','r')

s = input().split()
if len(s) %2 :
    for elem in s[-2::-2]: print(elem, end=" ")
else:
    for elem in s[-1::-2]: print(elem, end=" ")


# a b c d e => b d를 거꾸로 하는 d b
# a b c d e f g