# 自然数nが偶数であるときeven、奇数であるときoddと表示するプログラムを書いてください。

n = int(input("自然数を入力してください\n"))

if n % 2 == 0:
    print("even")
else:
    print("odd")