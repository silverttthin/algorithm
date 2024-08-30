import sys
sys.stdin = open('input.txt', 'r')

# a회의를 골랐으면 다음 회의 b는 반드시 시작시간이 a의 끝나는 시간보다 나중이여야 한다.

n = int(input())
ans, meetings = [],[]
for i in range(n): meetings.append(list(map(int,input().split())))

meetings.sort(key=lambda x : x[2])

prev_endtime = -1
for meetingNum, start, end in meetings:
    if prev_endtime <= start:
        ans.append(meetingNum)
        prev_endtime = end

print(len(ans))
for num in ans : print(num, end=" ")