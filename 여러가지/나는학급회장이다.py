import sys

sys.stdin = open("input.txt",'r')

input = sys.stdin.readline

n = int(input())
score_arr = [0]*3
weight_arr = score_arr[:]

for _ in range(n):
    a,b,c = map(int,input().split())
    score_arr[0]+=a
    weight_arr[0] += a**2

    score_arr[1]+=b
    weight_arr[1] += b**2

    score_arr[2]+=c
    weight_arr[2] += c**2

maxval = max(score_arr)
if score_arr.count(maxval) ==1:
    idx = score_arr.index(maxval)
    print(idx+1, score_arr[idx])
else:
    biggest_w = max(weight_arr)
    idx = weight_arr.index(biggest_w)
    
    if weight_arr.count(biggest_w) == 1:
        print(idx+1, score_arr[idx])
    else:
        print(0, score_arr[idx]) 