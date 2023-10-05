import sys
sys.stdin = open('input.txt','r')

s = [c for c in input()]
cnt, ans = 0, 0

# 내신 확통처럼 직접 다 케이스를 세는게 더 편한 때가 많다
for i in range(len(s)-1):
    # 레이저 아닌 여는괄호라며 cnt+=1 
    if [s[i], s[i+1]] == ['(', '(']:
        cnt += 1
    # 레이저라면 중첩만큼 ans증가
    elif [s[i], s[i+1]] == ['(', ')']:
        ans += cnt
    elif [s[i], s[i+1]] == [')', ')']:
        ans+= 1
        cnt-= 1

print(ans)
