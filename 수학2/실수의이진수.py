import sys
sys.stdin = open('input.txt','r')

n = float(input())

integerPart = int(n)
decimalPart = n-float(integerPart)

tmp = []
for _ in range(4):
    # 1보다 크면 자리올림수 1을 넣고 -1을 한 값을 다음 계산에 ㅏㅅ용
    decimalPart *= 2
    if decimalPart >=1:
        tmp.append(1)
        decimalPart -= 1
    else:
        tmp.append(0)


print(f'{bin(integerPart)[2:]}.{"".join(map(str, tmp))}')
