#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4949                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: silverttthin <boj.kr/u/silverttthin>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4949                           #+#        #+#      #+#     #
#    Solved: 2024/09/16 11:17:43 by silverttthin  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 부울로 처리하고 마지막에 출력하기
# 출력단이 중첩돼있으니 버그 확률이 높아짐

while 1:
    stack = []
    string = input()
    balanced = True

    if string == '.': break
    
    for c in string:
        if c in ["(", "["]:
            stack.append(c)

        elif c == ")":
            # 스택이 비어있거나 매칭되지 않는다면
            if not stack or stack.pop()!= '(':
                balanced= False
                break
        
        elif c == "]":
            if not stack or stack.pop()!= '[':
                balanced = False
                break
    
    # 순회 종료 후 스택 빈 유무 따라 
    if stack:
        balanced = False
    
    print("yes") if balanced else print("no")
