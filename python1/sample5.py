# 3127と8201の最大公約数を求めるプログラムを書いてください。

for i in range(3127):
    x = 3127 % (i+1)
    y = 8201 % (i+1)

    if x == 0 and y == 0:
        ans = (i+1)

print("3127 と 8201の最大公約数は" + str(ans))


# a = 3127
# b = 8201

# i = a

# while a % i != 0 or b % 8 != 0:
#     i = i -1

# print(i)

