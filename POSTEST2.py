List = []


a = int(input("Masukkan isi variabel Integer\t1 =\t"))
List.append(a)
b = int(input("Masukkan isi variabel Integer\t2 =\t"))
List.append(b)

c = input("Masukkan isi variabel String\t1 =\t")
List.append(c)
d = input("Masukkan isi variabel String\t2 =\t")
List.append(d)

e = float(input("Masukkan isi variabel Float\t1 =\t"))
List.append(e)
f = float(input("Masukkan isi variabel Float\t2 =\t"))
List.append(f)

g = complex(input("Masukkan isi variabel Complex\t1 =\t"))
List.append(g)
h = complex(input("Masukkan isi variabel Complex\t2 =\t"))
List.append(h)

print("\n\nIsi dari List :\n{}.".format(List))

# Untuk Integer
print("\nInteger : ")
ab = a + b
print(a, "+", b, "=", ab)
ab = a - b
print(a, "-", b, "=", ab)
ab = a * b
print(a, "*", b, "=", ab)
ab = a / b
print(a, "/", b, "=", ab)
ab = a % b
print(a, "%", b, "=", ab)

# Untuk String
print("\nString : ")
cd = c + d
print(c ,"+", d, "= {}".format(cd))
if (d.isnumeric() == True) : 
    dInt = int(d)
    cd = c * dInt
    print(c ,"*", d, "= {}".format(cd))


# Untuk float
print("\nFloat : ")
ef = e + f
print(e, "+", f, "=", ef)
ef = e - f
print(e, "-", f, "=", ef)
ef = e * f
print(e, "*", f, "=", ef)
ef = e / f
print(e, "/", f, "=", ef)
ef = e % f
print(e, "%", f, "=", ef)

# Untuk Complex
print("\nComplex : ")
gh = g + h
print(g, "+", h, "=", gh)
gh = g - h
print(g, "-", h, "=", gh)
gh = g * h
print(g, "*", h, "=", gh)
gh = g / h
print(g, "/", h, "=", gh)

print("\n\nIni adalah Perulangan Untuk Menampilkan isi List :    ")
for x in List:
    print (x)