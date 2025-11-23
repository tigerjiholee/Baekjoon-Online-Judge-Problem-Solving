n = int(input())
li = []
for i in range(n):
  s,e = map(int,input().split())
  li.append((s,e))
li.sort(key = lambda x: (x[1],x[0]))

ans = 0
e = 0
for i in range(n): 
  if li[i][0] >= e: 
    ans += 1
    e = li[i][1]
print(ans)