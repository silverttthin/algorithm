import sys
sys.stdin = open('input.txt','r')

n, jinsu= map(int,input().split())

if jinsu== 2:
    print(bin(n)[2:])

elif jinsu== 8:
    print(oct(n)[2:])

else:
    print(hex(n).upper()[2:])