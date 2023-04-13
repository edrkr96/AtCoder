a, b = map(int, input().split())
cnt = 0

while a != b:
  if a > b:
    tm = a % b
    rm = a//b
    if tm == 0:
      cnt += rm - 1
      break
    else:
      cnt += rm
      a = tm
  elif b > a:
    tm = b % a
    rm = b//a
    if tm == 0:
      cnt += rm - 1
      break
    else:
      cnt += rm
      b = tm

print(cnt)