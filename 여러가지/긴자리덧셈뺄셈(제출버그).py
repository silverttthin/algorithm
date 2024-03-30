import sys
sys.stdin = open('input.txt','r')

# def add(a,b):
#     ans = [0] * 201
#     for i in range(-1, -1*len(t1)-1, -1):
#         s = a[i]+b[i]
#         if s<10:
#             ans[i] = s
#         else:
#             ans[i] = s-10
#             a[i-1] += 1
    
#     ans = ''.join(map(str,ans))
#     print(ans[i:])

# def sbt(a,b):
#     ans = [0] * 201
#     for i in range(-1, -1*len(t1)-1, -1):
#         st = a[i] - b[i]
#         if st>=0: ans[i] = st
#         else:
#             if a[i-1]>0:
#                 a[i-1]-=1
#                 a[i]+=10
#                 ans[i] = a[i]-b[i]
#             elif a[i-1]==0:
#                 k=0
#                 while a[i-1-k] == 0:
#                     a[i-1-k] = 9
#                     k+=1
#                 a[i-1-k] -= 1
#                 ans[i] = -st
            
#     ans = ''.join(map(str,ans))
#     print(ans[i:])

# while 1:
#     t1,t2=  input().split()

#     if t1=='0' and t2=='0': break

#     a = [0] * 201
#     b = [0] * 201
#     if len(t1)<len(t2): 
#         t1,t2 = t2,t1
#     elif len(t1) == len(t2):
#         if t1<t2: 
#             t1, t2 = t2, t1

#     for i in range(-1,-1*len(t1)-1,-1):
#         a[i] = int(t1[i])
#     for i in range(-1,-1*len(t2)-1,-1):
#         b[i] = int(t2[i])


#     add(a,b)
#     # sbt(a,b)

def add(a,b):
    ans = [0] * 10001
    for i in range(-1, -1*len(t1)-1, -1):
        s = a[i]+b[i]
        if s<10:
            ans[i] = s
        else:
            ans[i] = s-10
            a[i-1] += 1

    if a[i-1] == 1:
        ans[i-1]=1
        i-=1
        
    ans = ''.join(map(str,ans))
    print(ans[i:])

    
t1,t2= input().split()

a = [0] * 10001
b = [0] * 10001
if len(t1)<len(t2): 
    t1,t2 = t2,t1
elif len(t1) == len(t2):
    if t1<t2: 
        t1, t2 = t2, t1

for i in range(-1,-1*len(t1)-1,-1):
    a[i] = int(t1[i])
for i in range(-1,-1*len(t2)-1,-1):
    b[i] = int(t2[i])


add(a,b)