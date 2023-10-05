import sys

sys.stdin = open('input.txt', 'r')

arr = []
row_max = -1
for _ in range(5):
    input_s = input()
    row_max = max(row_max, len(input_s)) # 가장 긴 문자열의 개수
    arr.append(list(input_s))

# 리스트에 문자열을 넣고
# 열은 고정한 채 행을 하나씩 증가시켜 읽어내기
# 인덱스 초과 에러는 try except로 넘기기

for i in range(row_max):
    for j in range(5):
        try:
            print(arr[j][i], end="")
        except:
            print("",end="")
            

