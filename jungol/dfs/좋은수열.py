import sys
sys.stdin = open('input.txt','r')


n = int(input())

def check(seq): # 나쁜수열인지 좋은수열인지 체크
    for s in range(1, len(seq)//2 + 1): # i개로 이뤄진 부분수열, 최대는 문자열의 반
        for i in range(len(seq) - 2*s +1): # i개 탐색시 총 탐색 횟수는 len - 2s + 1번이다
            if seq[i:i+s] == seq[i+s:i+2*s] :
                return False
    return True

def check(num): # 더 깔끔한 체크함수. 체크한 문자열 부분은 안봐도 되니 뒤쪽에 추가되는 것들만 보기
    length = len(num)
    for idx in range(1, length//2 + 1):
        if num[-idx:] == num[-(idx*2):-idx]:
            return False
    else:
        return True



def dfs(num, seq): # 숫자 붙인게 체크에 통과하면 seq를 업데이트
    if check(seq + [num]):
        seq.append(num)

        if len(seq) == n:
            seq = list(map(str, seq))
            print(''.join(seq))
            exit()

        for i in [1,2,3]:
            if seq[-1] == i: # 이전수와 같은 경우는 탐색할 필요도 없음
                continue
            dfs(i, seq)

        seq.pop() # 바로위 for문을 다 돌고 내려왔단 것은 exit실행 안됐다는 뜻은 답이 될수 없다는 뜻
    return

for i in [1,2,3]:
    dfs(i, [])

