import sys;sys.stdin=open('input.txt','r')

# n번째 피보나치 수를 구할 때 0과1이 각각 몇번 출력됐는지 구하라
# fibo(n) 0or1출력횟수 = fibo(n-1) fibo(n-2) 에서의 0or1 출력횟수 합

fibo_call_0 = [0] * 41
fibo_call_1 = fibo_call_0[:]

fibo_call_0[0] = 1
fibo_call_0[1] = 0
fibo_call_1[0] = 0
fibo_call_1[1] = 1
for i in range(2,41):
    fibo_call_0[i] = fibo_call_0[i-1] + fibo_call_0[i-2]
    fibo_call_1[i] = fibo_call_1[i-1] + fibo_call_1[i-2]

T = int(input())

for i in range(T):
    n = int(input())
    print(fibo_call_0[n], fibo_call_1[n])