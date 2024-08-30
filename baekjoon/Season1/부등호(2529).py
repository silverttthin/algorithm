import sys
sys.setrecursionlimit(10000000)

sys.stdin = open('input.txt','r')

k = int(input())

signs = input().split()
num = [-1] * (k+1) # 고른 숫자들을 담아 최종 숫자 구현용 변수
check = [0] * 10
ans = [-1, 10000000000]
compare_list = ans[:]
a = []
def dfs(stage):
    global num, check, a

    if stage == k+1:
        
        # str_tmp = list(map(str,num))
        # int_tmp = int(''.join(str_tmp))

        
        # if compare_list[0] < int_tmp:
        #     ans[0] = ''.join(str_tmp)
        #     compare_list[0] = int_tmp
        # if compare_list[1] > int_tmp:
        #     ans[1] = ''.join(str_tmp)
        #     compare_list[1] = int_tmp
        return


    if stage == 0:
        # 첨엔 적당히 아무거나
        for i in range(10):
            num[stage] = i
            check[i] = 1
            dfs(stage + 1)
            check[i] = 0
        return
    
    elif stage > 0:
        prev_num = num[stage - 1]
        sign = signs[stage - 1]
        if sign == '<' : # 무조건 prev보다 큰 수만을 뽑아야함
            for i in range(prev_num+1, 10):
                if check[i] == 0 :
                    check[i] = 1
                    num[stage] = i
                    dfs(stage+1)
                    check[i]= 0
            return
        else:
            for i in range(prev_num):
                if check[i] == 0 :
                    check[i] = 1
                    num[stage] = i
                    dfs(stage+1)
                    check[i]= 0

dfs(0)



# for i in range(2):
#     print(ans[i])