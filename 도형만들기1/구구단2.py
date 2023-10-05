import sys
sys.stdin = open('input.txt', 'r')

s, e = map(int, input().split())

if s>e:
    while s >= e:
        for i in range(1, 9+1):
            print(f'{s} * {i} =', end="")

            if s*i <10: 
                print(f'  {s*i}', end="   ")
            else: 
                print(f' {s*i}', end="   ")

            if i % 3 == 0 : print()
        print()
        s -= 1

else :
    while s <= e:
        for i in range(1, 9+1):
            print(f'{s} * {i} =', end="")

            if s*i <10: 
                print(f'  {s*i}', end="   ")
            else: 
                print(f' {s*i}', end="   ")

            if i % 3 == 0 : print()
        print()
        s += 1

