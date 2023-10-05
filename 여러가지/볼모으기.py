import sys
sys.stdin = open('input.txt','r')

import collections
N = int(input())
balls = input()

if 'R' not in balls or 'B' not in balls: 
    print(0)
    exit()

cnter = collections.Counter(balls)
total_R, total_B = cnter['R'], cnter['B']
cntlist = []
#옮겨야 하는 횟수는 기준과 색다른 공 이후 중 기준 색 공의 개수이다.

# 1. 좌측으로 옮겨야할때

# 빨간공을 옮겨야 할 경우
for idx, ball in enumerate(balls):
    if idx == 0 and ball == 'B': # 첫 시작부터 다른색공, 횟수는 나머지 R의 개수
        cntlist.append(total_R)
        break
    else:
        if ball == 'B': # 해당 인덱스+1 위치부터 나머지 balls 중 R의 개수
            tmp = collections.Counter(balls[idx+1:])
            cntlist.append(tmp['R'])
            break

# 파란공을 옮겨야 할 경우
for idx, ball in enumerate(balls):
    if idx == 0 and ball == 'R': # 첫 시작부터 플래그라 횟수는 B의 개수
        cntlist.append(total_B)
        break
    else:
        if ball == 'R': # 해당 인덱스 + 1위치부터의 나머지 balls 중 R의 개수
            tmp = collections.Counter(balls[idx+1:])
            cntlist.append(tmp['B'])
            break


###############################

balls= balls[::-1]
for idx, ball in enumerate(balls):
    if idx == 0 and ball == 'B': 
        cntlist.append(total_R)
        break
    else:
        if ball == 'B': 
            tmp = collections.Counter(balls[idx+1:])
            cntlist.append(tmp['R'])
            break

# 파란공을 옮겨야 할 경우
for idx, ball in enumerate(balls):
    if idx == 0 and ball == 'R': 
        cntlist.append(total_B)
        break
    else:
        if ball == 'R': 
            tmp = collections.Counter(balls[idx+1:])
            cntlist.append(tmp['B'])
            break

print(min(cntlist))