n = int(input())
A = sorted(list(map(int,input().split())))
t = 0
if n != 1:
  while A[-1] != 0 :
    t += 1
    A[-1] -= 1 
    if A[-2] != 0 : A[-2] -= 1 
    else : break 
    A = sorted(A)

t += A[-1]
if t > 1440 : print(-1)
else : print(t)