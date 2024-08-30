#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10773                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: silverttthin <boj.kr/u/silverttthin>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10773                          #+#        #+#      #+#     #
#    Solved: 2024/08/30 17:44:24 by silverttthin  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


K= int(input())
stack = []

for _ in range(K):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))

