t = int(input())
for i in range(t):
  n = int(input())
  li = list(map(int,input().split()))
  ans = 0
  m = li[-1]
  for j in range(n-1,-1,-1):
    if li[j] > m: 
      m = li[j]
    else: 
      ans += m-li[j]
  print(ans)