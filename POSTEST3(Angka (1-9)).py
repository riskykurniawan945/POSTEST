# Angka (1-9)
# Karena Program akan mengoutput angka nol jika kelipatan 9
# Bisa diakali dengan print(9)


angka = int(input("Masukkan Angka =    "))

for i in range(angka):
    if ((i+1) % 9 == 0):
        print(9)
    else:
        print ((i+1) % 9)




# # DENGAN INPUT MENGGUNAKAN NIM
# # NIM = 2009106050

# nim = int(input("Masukkan NIM =    "))
# angka = int(input("Ingin Menghitung berapa kali =    "))
# for i in range(angka):
#     print (nim + (i)) # ini jika tidak mau angka berulang di 1-10

#     # print (nim + (i % 10)) # ini akan selalu mengulang 1-10
