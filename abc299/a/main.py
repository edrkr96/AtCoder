n = int(input())
s = input()

fst = s.index("|")
if fst< s.index("*") and s[fst+1:].index("*") < s[fst+1:].index("|"):
  print("in")
else:
  print("out")