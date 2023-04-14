input = [int(x) for x in input()] #文字ごとに整数型に変換してリストに格納

for i in range(2**3): #記号の分だけビット探索
  ans = input[0]
  out = [input[0]]
  for j in range(3):
    if (i >> j) & 1 == 1: #右にずらしていき最後尾の1との論理和(AND)をとる
      ans += input[j+1] #桁が1なら足し算
      out.append("+") 
      out.append(input[j+1])
    else:
      ans -= input[j+1] #桁が0なら引き算
      out.append("-")
      out.append(input[j+1])
  #print(ans, out)    
  if ans == 7:
    out.append("=7")
    print(*out, sep="")
    break

'''
n = input()
op_cnt = len(n) - 1  # すき間の個数
for i in range(2 ** op_cnt):
    op = ["-"] * op_cnt  # あらかじめ ["-", "-", "-"] というリストを作っておく
    for j in range(op_cnt):
        if ((i >> j) & 1):
            op[op_cnt - 1 - j] = "+"  # フラグが立っていた箇所を "+" で上書き

    formula = ""
    for p_n, p_o in zip(n, op + [""]):  # opに空白を足すことで元の数列nとの要素数を揃える
        formula += (p_n + p_o) # 数列と記号(+,-)を前から交互にたす
    if eval(formula) == 7: #
        print(formula + "=7")
        break
'''

'''
eval関数は、文字列をPythonのコードとして実行するための関数
文字列が「式」として評価され、実行し出力されます。
例：
eval("2+3")
>> 5
→ eval関数を用いることで、文字列を、「文字列」としてではなく、「式」として評価できます。

使用方法
eval("式", globals=None, locals=None)
第1引数の”式”には、ダブルクォーテーションで囲った式を代入します。
第2引数と第3引数には、任意でそれぞれグローバル、ローカルの「名前空間」を指定します。
eval関数の返り値としては、第1引数で指定した式の値が返されます。

eval関数を使って結果を変数に格納したい場合は、以下のように記述します。
変数 = eval("式")
'''