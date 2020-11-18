# Angka (1-9)

# CARA 1

angka = int(input("Masukkan Angka =    "))
for i in range(angka):
    print(9) if ((i+1) % 9 == 0) else print ((i+1) % 9)


# CARA 2
# Cara dibawah kurang efektif karena menambah variabel hanya untuk print output
# j = 1
# for i in range(angka):
#     print(j)
#     j += 1
#     if (j == 10):
#         j -= 9


# CARA 3
# a = 1
# b = 1
# while(a <= angka):
#     print(b)
#     b += 1
#     if (b == 10):
#         b -= 9
#     a += 1
