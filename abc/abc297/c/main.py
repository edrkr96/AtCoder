h, w = map(int, input().split())

for i in range(h):
  s = input().split()
  s = list(s[0])
  #print(s)
  for j in range(w-1):
    if s[j] == s[j+1] == "T":
      s[j] = "P"
      s[j+1] = "C"
  print("".join(s))