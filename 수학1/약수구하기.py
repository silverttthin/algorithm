import sys
sys.stdin = open('input.txt', 'r')

n, k = map(int,input().split())

yaksu = []

# 자기자신은 당연히 약수
for i in range(1, n//2+1):
    if n % i == 0:
        yaksu.append(i)

yaksu.append(n)

try:
    print(yaksu[k-1])
except:
    print(0)
