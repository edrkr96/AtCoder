n, q = map(int, input().split())
event = list(map(int, input().split()))
print(event)
called = []
#最後に呼ばれた人
last = 0

for i in range(q):
  #print(called)
  if event[i][0] == '1':
    #calledの最後から取ってくると、イベント2で後ろの人が先に呼ばれた場合にずれる
    #初めて呼ばれるたびにプラス1
    last  += 1
    called.append(last)
  elif event[i] == '3':
    print(called[0])
  else:
    idx = int(event[i][1:])
    called.remove(idx)
