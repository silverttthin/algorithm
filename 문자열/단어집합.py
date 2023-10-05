import sys
sys.stdin = open('input.txt','r')

#스트링을 입력한 후 구성 단어 중 단어목록!에 포함돼있지 않은 단어를 append
#입력 END까지

voca_lst = []
while 1:
    s = input()
    if s == "END": break

    lst = s.split()
    

    for voca in lst:
        if voca not in voca_lst:
            voca_lst.append(voca)
    print(" ".join(voca_lst))


    
