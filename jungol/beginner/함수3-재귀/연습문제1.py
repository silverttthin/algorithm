import sys
sys.stdin = open('input.txt', 'r')



def print_hong(n):
    if n != 0:
        print("홍길동")
        print_hong(n-1)
    else:
        return
        
print_hong(10)