n = int(input())
A = sorted(list(map(int,input().split())),reverse=True)
B = sorted(list(map(int,input().split())))
ans = 1
for i in A: 
  cnt = 0
  for j in B: 
    cnt += 1 if j>=i else 0
  ans *= cnt
  B.pop(-1)
print(ans)