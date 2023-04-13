s = input()
sm = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(s)):
    if s[i] not in sm:
        print(i+1)