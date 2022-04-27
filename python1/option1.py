# 30から60までの数で素数の場合はPrime
# それ以外の場合はその数字を出力するプログラムを作成してください

for i in range(30, 61):
    for j in range(i-1, 0, -1):
        if i % j == 0:
            break
    
    if j == 1:
        print("Prime")
    else:
        print(i)
