n = int(input())
w = list(input().split())
id = ['and', 'not', 'that', 'the', 'you']
flag = False

for i in range(len(w)):
  for j in range(len(id)):
    if w[i] == id[j]:
      flag = True
      break

if flag:
  print('yes')
else:
  print('No')