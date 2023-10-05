import sys
sys.stdin= open('input.txt', 'r')

def fibo(x):
    if x == 1: return 1
    elif x == 2: return 1
    else:
        if not memo[x]:
            memo[x]= fibo(x-1) + fibo(x-2)
        return memo[x]

# d번째 날에 준 떡의 개수 = k
# d와 k를 알 때
# 첫날 준 떡의 개수 a와 그 다음날에 준 떡의 개수 = b를 구하라
memo = [0 for _ in range(100000)]
memo[1], memo[2] = 1, 1
d, k = map(int,input().split())


# fibo(d) * a + fibo(d+1) * b = k를 만족시키는 a와 b를 찾기
a_coef, b_coef = fibo(d-2), fibo(d-1)

for i in range(1, 100001):
    remain = k - i * b_coef
    tmp= remain//a_coef
    if remain % a_coef == 0 and tmp <= i:
        print(tmp)
        print(i)
        break
