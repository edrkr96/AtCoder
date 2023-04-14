n = int(input())
ans = []

for i in range(10):
  dgt = (n // (2**(9-i)))%2
  ans.append(str(dgt))

print("".join(ans))


'''
デフォルトではprint()の出力は末尾で改行される
引数endに任意の文字列を指定すると、その文字列が改行の代わりに最後に挿入される。
例えば連続するprint()の出力を改行なしで単純に連結したい場合は空文字列''を指定すればよい。

print('abc', end='---')
print('xyz')
# abc---xyz

print('abc', end='')
print('xyz')
# abcxyz

リストの出力
print(*l)  # => print(0, 1, 2)
# 0 1 2
print(*l, sep='')
# 012
print(*l, sep='-')
# 0-1-2
'''