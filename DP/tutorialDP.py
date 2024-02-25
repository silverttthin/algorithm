import sys
sys.stdin = open('input.txt','r')

n = int(input())

nums = [0] * 100001
nums[1], nums[2] = 1, 1

for i in range(3, 100001):
    if nums[i] == 0:
        nums[i] = nums[i-2] + nums[i-1]

print(nums[n] % 1000000007)