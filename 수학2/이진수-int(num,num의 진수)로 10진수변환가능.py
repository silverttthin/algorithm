import sys
sys.stdin = open('input.txt','r')

n= input()
# exponent = 0
# ans = 0
# for bit in n[::-1]:
#     if bit == '1':
#         ans += 2 ** exponent
#     exponent+= 1
# print(ans)


print(int(n, 2))