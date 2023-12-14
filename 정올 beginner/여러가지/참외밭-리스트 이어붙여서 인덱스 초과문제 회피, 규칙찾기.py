import sys
sys.stdin= open('input.txt', 'r')
# arr*2해서 이어붙이는 아이디어!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

charmwae= int(input())

arr = []
for _ in range(6):
    v, q = map(int, input().split())
    arr.append((v,q))
# arr *= 2 

max_w, max_h= -1, -1

for idx,(v, q) in enumerate(arr):
    if v == 1 or v == 2:
        if q > max_w : 
            max_w = q
            max_w_idx = idx
        
    if v == 3 or v == 4:
        if q > max_h : 
            max_h = q
            max_h_idx = idx

# 만약 max_w 인덱스가 먼저라면 sub_h의 인덱스는 +3 sub_w 인덱스는 +4
# 만약 max_w 인덱스가 나중이라면 sub_h 인덱스는 +3, sub_w 인덱스는 +2

if arr[(max_w_idx +1)%6] == arr[max_h_idx] : # 인덱스를 비교하면 안되고 값을 비교
    sub_h_idx = max_w_idx+3
    sub_w_idx = max_w_idx+4
else:
    sub_h_idx = max_w_idx+3
    sub_w_idx = max_w_idx+2



print((max_h * max_w - arr[sub_h_idx%6][1] * arr[sub_w_idx%6][1])* charmwae)

# % 연산자로 아이템 개수로 나눠 우회할 수도 있다.
