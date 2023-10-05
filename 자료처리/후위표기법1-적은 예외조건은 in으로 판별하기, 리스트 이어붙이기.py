import sys
sys.stdin = open('input.txt','r')

N= int(input())
line = input().split()

while len(line)!=1:
    for i in range(N-2): 
        # python 내장함수로는 문자열 음의 정수 판별이 불가
        # 이때 정수형으로 바꿀 때 연산자 예외처리!  
        if line[i+2] in ['*', '/', '+', '-']:
            ans = eval(f'{line[i]} {line[i+2]} {line[i+1]}')
            line = line[:i] +[str(ans)]+ line[i+3:]
            break

print(int(eval(line[0])))
