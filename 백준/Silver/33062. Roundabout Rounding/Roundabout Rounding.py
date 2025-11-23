t = int(input())
for test in range(t):
  n = int(input())
  p = len(str(n))
  ans = 0
  for i in range(1,p-1): 
    ans += int("5"*i)
  if p >= 2 :
    l = int("4"*(p-1) + "5") 
    r =  (int("4"+"9"*(p-1)))
    if n >= l  : 
      tmp = int("5"*(p-1))
      if n <= r : 
        ans += tmp - (r-n)
      else : 
        ans += tmp 
      
  print(ans)