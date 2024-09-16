#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18258                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: silverttthin <boj.kr/u/silverttthin>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18258                          #+#        #+#      #+#     #
#    Solved: 2024/09/16 20:42:09 by silverttthin  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque
import sys

input = sys.stdin.readline

N = int(input().rstrip())

queue = deque()

for _ in range(N):
    inst = input().rstrip()

    if inst == 'size': 
        print(len(queue))
    
    elif inst == 'empty':
        if len(queue) == 0: print(1)
        else: print(0)
    
    elif inst == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif inst == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    
    elif inst == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    
    else:
        num = int(inst.split()[1])
        queue.append(num)