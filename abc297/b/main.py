s = input()
s = list(s)
b_sum = 0
r = []
k = 0

for i in range(len(s)):
  if s[i] == "B":
    b_sum += i
  elif s[i] == "R":
    r.append(i)
  elif s[i] == "K":
    k = i

if (b_sum % 2 == 1) and (r[0] < k < r[1]):
  print("Yes")
else:
  print("No")