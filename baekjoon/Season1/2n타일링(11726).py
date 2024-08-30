n = int(input())

arr = [0] * (n+1)

if n <=2:
    print(n)
else:
    arr[1] = 1
    arr[2] = 2
    for i in range(3, n+1):
        arr[i] = (arr[i-2]%10007 + arr[i-1] %10007) % 10007


    print(arr[n])