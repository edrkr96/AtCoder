n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a + b
d = []
a_ans = []
b_ans = []

for idx, value in enumerate(c):
  d.append([idx, value])
d = dict(d)
#print(d)
d_value = sorted(d.items(), key=lambda x: x[1])
d_value = dict(d_value)
#print(d_value)
key = list(d_value.keys())
value = list(d_value.values())

for i in range(len(c)):
  if key[i] < n:
    a_ans.append(i+1)
  else:
    b_ans.append(i+1)    
print(*a_ans)
print(*b_ans)

 