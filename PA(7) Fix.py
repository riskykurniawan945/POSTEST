import math
import os
import turtle
from time import sleep
from turtle import *

i = 0
riwayat = []

def gambarPersegi():
    # Persegi
    turtle.bgcolor("#393e46")

    # sisi 1
    turtle.color("#393e46")
    begin_fill()    
    turtle.forward(100)
    turtle.left(90)
    end_fill() 
    turtle.color("#ffd369", "#222831")
    begin_fill()
    turtle.write(' sisi', move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)

    # sisi 2 
    turtle.forward(100)
    turtle.write('sisi', move=False, align = "center", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)
    
    # sisi 3 
    turtle.forward(100)
    turtle.write(' sisi', move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)

    # sisi 4
    turtle.forward(100)
    turtle.write("\n\nsisi", move=False, align = "center", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)   
    turtle.forward(100)
    turtle.left(90)
    end_fill()

    turtle.color("#222831")
    begin_fill()    
    turtle.forward(15)
    end_fill() 

    return turtle



def gambarPersegiPanjang():
    # Persegi Panjang
    turtle.bgcolor("#393e46")

    # sisi 1
    turtle.color("#393e46")
    begin_fill()    
    turtle.forward(150)
    turtle.left(90)
    end_fill() 
    turtle.color("#ffd369", "#222831")
    begin_fill()    
    turtle.write(" Lebar", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)

    # sisi 2 
    turtle.forward(150)
    turtle.write("Panjang", move=False, align = "center", font=("Arial", 13, "italic"))    
    turtle.forward(150)
    turtle.left(90)
    
    # sisi 3 
    turtle.forward(100)
    turtle.write(" Lebar", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.forward(100)
    turtle.left(90)

    # sisi 4
    turtle.forward(150)
    turtle.write("Panjang", move=False, align = "center", font=("Arial", 13, "italic"))    
    turtle.forward(150)
    turtle.left(90)   
    turtle.forward(100)
    turtle.left(90)
    end_fill()

    turtle.color("#222831")
    begin_fill()    
    turtle.forward(15)
    end_fill() 

    return turtle



def gambarJajarGenjang():
    # JAJAR GENJANG

    turtle.bgcolor("#393e46")

    turtle.color("#393e46")
    begin_fill()    
    turtle.goto(0, -50)
    end_fill()
    turtle.color("#ffd369", "#222831")
    begin_fill()
    turtle.write("Sisi Alas", move=False, align = "center", font=("Arial", 13, "italic"))        
    turtle.goto(105, -50)
    turtle.goto(-195, -50)
    turtle.goto(-150, 0)
    turtle.write("Sisi Miring  ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(-105, 50)
    turtle.goto(195, 50)
    turtle.goto(105, -50)
    turtle.goto(-105, -50)
    turtle.goto(-105, 0)
    turtle.write(" Tinggi", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.goto(-105, 50)
    end_fill()

    return turtle




def gambarTrapesium():
    # TRAPESIUM
    turtle.bgcolor("#393e46")
    turtle.color("#ffd369", "#222831")
    begin_fill()
    turtle.write(" Sisi Alas", move=False, align = "center", font=("Arial", 13, "italic"))    
    turtle.goto(120, 0)
    turtle.goto(120, 60)
    turtle.write("Tinggi ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(120, 150)
    turtle.goto(0, 150)
    turtle.write(" Sisi Atas", move=False, align = "center", font=("Arial", 13, "italic"))
    turtle.goto(-120, 150)
    turtle.goto(-120, 75)
    # turtle.write(" Tinggi", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.goto(-120, 0)
    turtle.goto(210, 0)
    turtle.goto(165, 75)
    turtle.write(" Sisi Miring", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.goto(120, 150)
    turtle.goto(-120, 150)
    turtle.goto(-165, 75)
    turtle.write("Sisi Miring ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(-210, 0)

    turtle.goto(120, 0)
    end_fill()

    return turtle



def gambarBelahKetupat():
    #BELAH KETUPAT
    turtle.bgcolor("#393e46")
    turtle.color("#ffd369", "#222831")
    begin_fill()
    turtle.write("      Diagonal 1", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.goto(150, 0)
    turtle.goto(-150, 0)
    turtle.goto(-75, 100)
    turtle.write("Sisi 1 ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(0, 200)
    turtle.goto(0, -85)
    turtle.write("Diagonal 2 ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(0, -200)
    turtle.goto(75, -100)
    turtle.write("     Sisi 2 ", move=False, align = "left", font=("Arial", 13, "italic"))
    turtle.goto(150, 0)
    turtle.goto(75, 100)
    turtle.write(" Sisi 3", move=False, align = "left", font=("Arial", 13, "italic"))
    turtle.goto(0, 200)
    turtle.goto(0, -200)
    turtle.goto(-75, -100)
    turtle.write("Sisi 4    ", move=False, align = "right", font=("Arial", 13, "italic"))
    turtle.goto(-150, 0)
    end_fill()

    return turtle




def gambarLayangLayang():
    turtle.bgcolor("#393e46")
    turtle.color("#393e46")
    begin_fill()
    turtle.goto(50, 0)
    end_fill()
    turtle.color("#ffd369", "#222831")
    begin_fill()
    turtle.goto(50, 120)
    turtle.goto(50, -120)
    turtle.goto(50, -50)
    turtle.write("Diagonal 1 ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(50, 0)
    turtle.goto(155, 0)
    turtle.goto(0, 0)
    turtle.write("Diagonal 2 ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(-155, 0)
    turtle.goto(-52.5, -60)
    turtle.write("Sisi 1      ", move=False, align = "right", font=("Arial", 13, "italic"))    
    turtle.goto(50, -120)
    turtle.goto(102.5, -60)
    turtle.write("      Sisi 2", move=False, align = "left", font=("Arial", 13, "italic"))    
    turtle.goto(155, 0)
    turtle.goto(50, 120)
    turtle.goto(-155, 0)
    end_fill()

    return turtle




def gambarSegitiga():
    turtle.bgcolor("#393e46")
    turtle.color("#393e46", "white")
    begin_fill()
    turtle.goto(0, -50)
    end_fill()
    turtle.color("#ffd369", "#222831")
    begin_fill()
    turtle.write("Sisi 1 (Alas) ", move=False, align = "right", font=("Arial", 13, "italic"))
    turtle.goto(120, -50)
    turtle.goto(-120, -50)
    turtle.goto(-60, 55)
    turtle.write("Sisi 2 ", move=False, align = "right", font=("Arial", 13, "italic"))
    turtle.goto(0, 160)
    turtle.goto(60, 55)
    turtle.write(" Sisi 3", move=False, align = "left", font=("Arial", 13, "italic"))
    turtle.goto(120, -50)
    turtle.goto(0, -50)
    turtle.goto(0, 50)
    turtle.write(" Tinggi", move=False, align = "left", font=("Arial", 13, "italic"))
    turtle.goto(0, 160)

    return turtle




def gambarLingkaran():
    #Lingkaran
    turtle.bgcolor("#393e46")

    turtle.color("#ffd369", "#222831")
    begin_fill()
    turtle.circle(100)
    turtle.left(90)   
    turtle.goto(0, 50)
    turtle.write(" Jari-Jari", move=False, align = "left", font=("Arial", 13, "italic"))
    turtle.goto(0, 100)
    turtle.left(180)
    turtle.forward(100)
    end_fill()

    return turtle
    


    


def persegi(pil, indeks):
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Persegi")
                salah = True
                while(salah):
                    s = int(input("Masukkan panjang sisinya (cm):   "))
                    if (s == 0):
                        print("Ups, Panjang sisi tidak boleh 0!!")
                    elif (s < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        L = s * s 
                        print("L = sisi * sisi")
                        print("L =", s, "*", s)
                        print("Luas = {} cm^2\n".format(L))
                        salah = False                            
                kerjakan = True
                while (kerjakan):
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarPersegi()
                        done()
                        kerjakan = False
                        turtle.TurtleScreen._RUNNING = True
                    except turtle.Terminator:
                        turtle.TurtleScreen._RUNNING = True
                        print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                        continue
                return L
                EROR = False

            elif (str.upper(pil) == "KELILING"):
                print("Keliling Persegi")
                salah = True
                while (salah):
                    s = int(input("Masukkan panjang sisinya (cm):   "))
                    if (s == 0):
                        print("Ups, Panjang sisi tidak boleh 0!!")
                    elif (s < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        K = 4 * s
                        print("K = sisi + sisi + sisi + sisi")
                        print("K =", s, "+", s, "+", s, "+", s)
                        print("Keliling = {} cm\n".format(K))
                        salah = False    
                kerjakan = True
                while (kerjakan):
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarPersegi()
                        done()
                        kerjakan = False
                        turtle.TurtleScreen._RUNNING = True
                    except turtle.Terminator:
                        turtle.TurtleScreen._RUNNING = True
                        print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                        continue
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")





def persegiPanjang(pil, indeks):
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Persegi panjang")
                salah = True
                while (salah):
                    p = int(input("Masukkan panjangnya (cm):    "))
                    l = int(input("Masukkan lebarnya   (cm):    "))
                    if (p == 0 and l == 0):
                        print("Ups, Panjang dan Lebar tidak boleh 0!!")
                    elif (p == 0):
                        print("Ups, Panjang tidak boleh 0!!")
                    elif (l == 0):
                        print("Ups, Lebar tidak boleh 0!!")
                    elif (p < 0 or l < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        L = p * l
                        print("L = panjang * lebar")
                        print("L =", p, "*", l)
                        print("Luas = {} cm^2\n".format(L))
                        salah = False
                kerjakan = True
                while (kerjakan):
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarPersegiPanjang()
                        done()
                        kerjakan = False
                        turtle.TurtleScreen._RUNNING = True
                    except turtle.Terminator:
                        turtle.TurtleScreen._RUNNING = True
                        print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                        continue
                return L   
                EROR = False

            elif (str.upper(pil) == "KELILING"):
                print("Keliling Persegi panjang")
                salah = True
                while (salah):
                    p = int(input("Masukkan panjangnya (cm):    "))
                    l = int(input("Masukkan lebarnya   (cm):    "))
                    if (p == 0 and l == 0):
                        print("Ups, Panjang dan Lebar tidak boleh 0!!")
                    elif (p == 0):
                        print("Ups, Panjang tidak boleh 0!!")
                    elif (l == 0):
                        print("Ups, Lebar tidak boleh 0!!")
                    elif (p < 0 or l < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        K = 2 * (p + l)
                        print("K = 2 * (panjang + lebar)")
                        print("K = 2 *", "(", p, "+", l, ")")  
                        print("Keliling = {} cm\n".format(K))    
                        salah = False
                kerjakan = True
                while (kerjakan):
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarPersegiPanjang()
                        done()
                        kerjakan = False
                        turtle.TurtleScreen._RUNNING = True
                    except turtle.Terminator:
                        turtle.TurtleScreen._RUNNING = True
                        print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                        continue
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")





def jajarGenjang(pil, indeks):
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Jajar genjang")
                salah = True
                while (salah):
                    sBawah = int(input("Masukkan panjang alasnya (cm):    "))
                    t = int(input("Masukkan tingginya       (cm):    "))
                    if (sBawah == 0 and t == 0):
                        print("Ups, Panjang alas dan Tinggi tidak boleh 0!!")
                    elif (sBawah == 0):
                        print("Ups, Panjang alas tidak boleh 0!!")
                    elif (t == 0):
                        print("Ups, Tinggi tidak boleh 0!!")
                    elif (sBawah < 0 or t < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:                        
                        L = sBawah * t
                        print("L = alas * tinggi")
                        print("L =", sBawah, "*", t)
                        print("Luas = {} cm^2\n".format(L))
                        salah = False
                kerjakan = True
                while (kerjakan):
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarJajarGenjang()
                        done()
                        kerjakan = False
                        turtle.TurtleScreen._RUNNING = True
                    except turtle.Terminator:
                        turtle.TurtleScreen._RUNNING = True
                        print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                        continue
                return L  
                EROR = False

            elif (str.upper(pil) == "KELILING"):
                print("Keliling Jajar genjang")
                salah = True
                while (salah):
                    sBawah = int(input("Masukkan panjang alasnya        (cm):    "))
                    sMiring = int(input("Masukkan panjang sisi miringnya (cm):    "))
                    if (sBawah == 0 and sMiring == 0):
                        print("Ups, Panjang alas dan Sisi miring tidak boleh 0!!")
                    elif (sBawah == 0):
                        print("Ups, Panjang alas tidak boleh 0!!")
                    elif (sMiring == 0):
                        print("Ups, Sisi Miring tidak boleh 0!!")
                    elif (sBawah < 0 or sMiring < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        K = 2 * (sBawah + sMiring)
                        print("K = 2 * (sisiAlas + sisiMiring)")
                        print("K = 2 * (", sBawah, "+", sMiring, ")")
                        print("Keliling = {} cm".format(K))
                        salah = False 
                kerjakan = True
                while (kerjakan):
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarJajarGenjang()
                        done()
                        kerjakan = False
                        turtle.TurtleScreen._RUNNING = True
                    except turtle.Terminator:
                        turtle.TurtleScreen._RUNNING = True
                        print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                        continue
        
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")
    

    


def trapesium(pil, indeks):
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Trapesium")
                salah = True
                while(salah):
                    sBawah = int(input("Masukkan panjang alasnya      (cm):    "))
                    sAtas = int(input("Masukkan panjang sisi atasnya (cm):    "))
                    t = int(input("Masukkan tingginya            (cm):    "))
                    if (sBawah == 0 and sAtas == 0 and t == 0):
                        print("Ups, Panjang alas, Sisi atas, dan Tinggi tidak boleh 0!!")
                    elif(sBawah == 0 and sAtas == 0):
                        print("Ups, Panjang alas, Sisi atas, tidak boleh 0!!")
                    elif (sAtas == 0 and t == 0):
                        print("Ups, Panjang Sisi atas, dan Tinggi tidak boleh 0!!")
                    elif (sAtas == 0):
                        print("Ups, Panjang Sisi Atas tidak boleh 0!!")
                    elif (sBawah == 0):
                        print("Ups, Panjang Sisi Alas tidak boleh 0!!")
                    elif (t == 0):
                        print("Ups, Tinggi tidak boleh 0!!")
                    elif (sBawah < 0 or t < 0 or sAtas < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        L = .5 * (sBawah + sAtas) * t
                        print("L = 1/2 * (alas + sisiAtas) * tinggi")
                        print("L = 1/2 * (", sBawah, "+", sAtas, ")", "*", t)
                        print("Luas = {} cm^2".format(L)) 
                        salah = False 
                kerjakan = True
                while (kerjakan):
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarTrapesium()
                        done()
                        kerjakan = False
                        turtle.TurtleScreen._RUNNING = True
                    except turtle.Terminator:
                        turtle.TurtleScreen._RUNNING = True
                        print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                        continue
                return L
                EROR = False
            elif (str.upper(pil) == "KELILING"):
                print("Keliling Trapesium")
                salah = True
                while(salah):
                    sBawah = int(input("Masukkan panjang sisi alasnya (cm):\t"))
                    sAtas = int(input("Masukkan panjang sisi atasnya (cm):\t"))
                    sKanan = int(input("Masukkan panjang sisi kanannya (cm):\t"))
                    sKiri = int(input("Masukkan panjang sisi Kirinya (cm):\t")) 
                    if (sBawah == 0 and sAtas == 0 and sKanan == 0 and sKiri == 0):
                        print("Ups, Panjang Alas, sisi Atas, sisi Kanan, sisi Kiri tidak boleh 0!!" )
                    elif (sBawah == 0 and sAtas == 0 and sKanan == 0):
                        print("Ups, Panjang Alas, sisi Atas, sisi Kanan, tidak boleh 0!!" )
                    elif (sBawah == 0 and sAtas == 0 and sKiri == 0):
                        print("Ups, Panjang Alas, sisi Atas, sisi Kiri tidak boleh 0!!" )
                    elif (sBawah == 0 and sKanan == 0 and sKiri == 0):
                        print("Ups, Panjang Alas, sisi Kanan, sisi Kiri tidak boleh 0!!" )
                    elif (sAtas == 0 and sKanan == 0 and sKiri == 0):
                        print("Ups, Panjang sisi Atas, sisi Kanan, sisi Kiri tidak boleh 0!!" )
                    elif (sBawah == 0 and sAtas == 0):
                        print("Ups, Panjang Alas, sisi Atas tidak boleh 0!!" )
                    elif (sBawah == 0 and sKanan == 0):
                        print("Ups, Panjang Alas, sisi Kanan tidak boleh 0!!" )
                    elif (sBawah == 0 and sKiri == 0):
                        print("Ups, Panjang Alas, sisi Kiri tidak boleh 0!!" )
                    elif (sAtas == 0 and sKanan):
                        print("Ups, Panjang sisi Atas, sisi Kanan tidak boleh 0!!" )
                    elif (sAtas == 0 and sKiri == 0):
                        print("Ups, Panjang sisi Atas, sisi Kiri tidak boleh 0!!" )
                    elif (sKanan == 0 and sKiri == 0):
                        print("Ups, Panjang sisi Kanan, sisi Kiri tidak boleh 0!!" )
                    elif (sBawah == 0):
                        print("Ups, Panjang alas tidak boleh 0!!")
                    elif (sAtas == 0):
                        print("Ups, Panjang Sisi Atas tidak boleh 0!!")
                    elif (sKanan == 0):
                        print("Ups, Panjang Sisi Kanan tidak boleh 0!!")
                    elif (sKiri == 0):
                        print("Ups, Panjang Sisi Kiri tidak boleh 0!!")
                    elif (sBawah < 0 or sAtas < 0 or sKanan < 0 or sKiri < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        K = sAtas + sKiri + sKanan + sBawah
                        print("K = sAtas+sKiri+sKanan+sBawah")
                        print("K =", sAtas, "+", sKiri, "+", sKanan, "+", sBawah)
                        print("Keliling = {} cm".format(K))
                        salah = False
                kerjakan = True
                while (kerjakan):
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarTrapesium()
                        done()
                        kerjakan = False
                        turtle.TurtleScreen._RUNNING = True
                    except turtle.Terminator:
                        turtle.TurtleScreen._RUNNING = True
                        print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                        continue
                  
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")




def belahKetupat(pil, indeks):
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Belah Ketupat")
                salah = True
                while(salah):
                    d1 = int(input("Masukkan panjang diagonal1 (cm):     "))
                    d2 = int(input("Masukkan panjang diagonal2 (cm):     "))
                    if(d1 == 0 and d2 == 0):
                        print("Ups, Diagonal 1 dan Diagonal 2 tidak boleh 0!!")
                    elif(d1 == 0):
                        print("Ups, Diagonal 1 tidak boleh 0!!")
                    elif(d2 == 0):
                        print("Ups, Diagonal 2 tidak boleh 0!!")
                    elif (d1 < 0 or d2 < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        L = .5 * d1 * d2
                        print("L = 1/2 * diagonal1 * diagonal2")
                        print("L = 1/2 *", d1, "*", d2)
                        print("Luas = {} cm^2".format(L))
                        salah = False 
                kerjakan = True
                while (kerjakan):
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarBelahKetupat()
                        done()
                        kerjakan = False
                        turtle.TurtleScreen._RUNNING = True
                    except turtle.Terminator:
                        turtle.TurtleScreen._RUNNING = True
                        print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                        continue
                  
                return L
                EROR = False

            elif (str.upper(pil) == "KELILING"):
                print("Keliling Belah Ketupat")
                salah = True
                while (salah):
                    s = int(input("Masukkan panjang sisinya (cm):   "))
                    if (s == 0):
                        print("Ups, Panjang sisi tidak boleh 0!!")
                    elif (s < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        K = 4 * s
                        print("K = sisi + sisi + sisi + sisi")
                        print("K = ", s, "+", s, "+", s, "+", s)
                        print("Keliling = {} cm".format(K))
                        salah = False
                kerjakan = True
                while (kerjakan):
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarBelahKetupat()
                        done()
                        kerjakan = False
                        turtle.TurtleScreen._RUNNING = True
                    except turtle.Terminator:
                        turtle.TurtleScreen._RUNNING = True
                        print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                        continue
                  
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")
    

    


def layangLayang(pil, indeks):
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Layang-layang")
                salah = True
                while(salah):
                    d1 = int(input("Masukkan panjang diagonal1 (cm):    "))
                    d2 = int(input("Masukkan panjang diagonal2 (cm):    "))
                    if(d1 == 0 and d2 == 0):
                        print("Ups, Diagonal 1 dan Diagonal 2 tidak boleh 0!!")
                    elif(d1 == 0):
                        print("Ups, Diagonal 1 tidak boleh 0!!")
                    elif(d2 == 0):
                        print("Ups, Diagonal 2 tidak boleh 0!!")
                    elif (d1 < 0 or d2 < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:     
                        L =  .5 * d1 * d2
                        print("L = 1/2 * diagonal1 * diagonal2")
                        print("L = 1/2 *", d1, "*", d2)
                        print("Luas = {} cm^2".format(L))
                        salah = False  
                kerjakan = True
                while (kerjakan):
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarLayangLayang()
                        done()
                        kerjakan = False
                        turtle.TurtleScreen._RUNNING = True
                    except turtle.Terminator:
                        turtle.TurtleScreen._RUNNING = True
                        print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                        continue
                return L
                EROR = False

            elif (str.upper(pil) == "KELILING"):
                print("Keliling Layang-layang")
                salah = True
                while(salah):
                    s1 = int(input("Masukkan panjang sisi1 (cm):     "))
                    s2 = int(input("Masukkan panjang sisi2 (cm):     "))
                    if (s1 == 0 and s2 == 0):
                        print("Panjang Sisi 1 & Sisi 2 tidak boleh nol")
                    elif (s1 == 0):
                        print("Panjang Sisi 1 tidak boleh nol")
                    elif (s2 == 0):
                        print("Panjang Sisi 2 tidak boleh nol")    
                    elif (s1 < 0 or s2 < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        K = 2 * (s1 + s2)
                        print("K = 2 * (sisi1 + sisi2)")
                        print("K = 2 * (", s1, "+", s2, ")")
                        print("Keliling = {} cm".format(K))
                        salah = False
                kerjakan = True
                while (kerjakan):
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarLayangLayang()
                        done()
                        kerjakan = False
                        turtle.TurtleScreen._RUNNING = True
                    except turtle.Terminator:
                        turtle.TurtleScreen._RUNNING = True
                        print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                        continue
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")
   

    


def segitiga(pil, indeks):
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Segitiga")
                salah = True
                while (salah):
                    sBawah = int(input("Masukkan panjang alasnya (cm):\t"))
                    t = int(input("Masukkan tingginya (cm):\t"))
                    if (sBawah == 0 and t == 0):
                        print("Ups, Panjang alas dan Tinggi tidak boleh 0!!")
                    elif (sBawah == 0):
                        print("Ups, Panjang alas tidak boleh 0!!")
                    elif (t == 0):
                        print("Ups, Tinggi tidak boleh 0!!")
                    elif (sBawah < 0 or t < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        L = .5 * sBawah * t
                        print("L = 1/2 * alas * tinggi")
                        print("L = 1/2 *", sBawah, "*", t)
                        print("Luas = {} cm^2".format(L)) 
                        salah = False
                kerjakan = True
                while (kerjakan):
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarSegitiga()
                        done()
                        kerjakan = False
                        turtle.TurtleScreen._RUNNING = True
                    except turtle.Terminator:
                        turtle.TurtleScreen._RUNNING = True
                        print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                        continue
                return L
                EROR = False

            elif (str.upper(pil) == "KELILING"):
                print("Keliling Segitiga")
                salah = True
                while (salah):
                    s1 = int(input("Masukkan panjang sisi1 (cm):     "))
                    s2 = int(input("Masukkan panjang sisi2 (cm):     "))
                    s3 = int(input("Masukkan panjang sisi3 (cm):     "))
                    if (s1 == 0 and s2 == 0 and s3 == 0):
                        print("Panjang Sisi 1, Sisi 2, dan Sisi 3 tidak boleh nol")
                    elif (s1 == 0 and s2 == 0):
                        print("Panjang Sisi 1 & Sisi 2 tidak boleh nol")
                    elif (s1 == 0 and s3 == 0):
                        print("Panjang Sisi 1 & Sisi 3 tidak boleh nol")
                    elif (s2 == 0 and s3 == 0):
                        print("Panjang Sisi 2 & Sisi 3 tidak boleh nol")
                    elif (s1 == 0):
                        print("Panjang Sisi 1 tidak boleh nol")
                    elif (s2 == 0):
                        print("Panjang Sisi 2 tidak boleh nol")
                    elif (s3 == 0):
                        print("Panjang Sisi 3 tidak boleh nol")
                    elif (s1 < 0 or s2 < 0 or s3 < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        K = s1 + s2 +s3
                        print("K = s1 + s2 + s3")
                        print("K =", s1, "+", s2, "+", s3)
                        print("Keliling = {} cm".format(K))
                        salah = False
                kerjakan = True
                while (kerjakan):
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarSegitiga()
                        done()
                        kerjakan = False
                        turtle.TurtleScreen._RUNNING = True
                    except turtle.Terminator:
                        turtle.TurtleScreen._RUNNING = True
                        print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                        continue
                return K
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")
    

   


def lingkaran(pil, indeks):
    EROR = True
    while (EROR): 
        try:
            if (str.upper(pil) == "LUAS"):
                print("Luas Lingkaran")
                salah = True
                while(salah):
                    r = int(input("Masukkan panjang jari-jarinya (cm):   "))
                    if (r == 0):
                        print("Ups, Panjang Jari-jari tidak boleh 0!!")
                    elif (r < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        L = math.pi * r**2
                        print("L = π * jari-jari^2")
                        print("L = 3.141592 *", r**2)
                        print("Luas = {} cm^2".format(L)) 
                        salah = False
                kerjakan = True
                while (kerjakan):
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarLingkaran()
                        done()
                        kerjakan = False
                        turtle.TurtleScreen._RUNNING = True
                    except turtle.Terminator:
                        turtle.TurtleScreen._RUNNING = True
                        print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                        continue
                return L
                EROR = False
                
            elif (str.upper(pil) == "KELILING"):
                print("Keliling Lingkaran")
                salah = True
                while(salah):
                    r = int(input("Masukkan panjang jari-jarinya (cm):   "))
                    if (r == 0):
                        print("Ups, Panjang Jari-jari tidak boleh 0!!")
                    elif (r < 0):
                        print("Tidak boleh Negatif!!!!")
                    else:
                        K = 2 * math.pi * r
                        print("K = 2 * π * jari-jari")
                        print("K = 2 * 3.141592 *", r)
                        print("Keliling = {} cm".format(K))
                        salah = False
                kerjakan = True
                while (kerjakan):
                    try:
                        turtle.TurtleScreen._RUNNING = True
                        gambarLingkaran()
                        done()
                        kerjakan = False
                        turtle.TurtleScreen._RUNNING = True
                    except turtle.Terminator:
                        turtle.TurtleScreen._RUNNING = True
                        print("JANGAN DI CLOSE SEBELUM GAMBAR SELESAI!!!")
                        continue
                return K    
                EROR = False
        except ValueError:
            print("Input anda salah, Masukkan angka!!")
    



def mulaiMenghitung(user):
    global i, riwayat
    print("================\n")
    print("[1] Persegi\t\t||")
    print("[2] Persegi panjang\t||")
    print("[3] Jajar Genjang\t||")
    print("[4] Trapesium\t\t||")
    print("[5] Belah Ketupat\t||")
    print("[6] Layang-Layang\t||")
    print("[7] Segitiga\t\t||")
    print("[8] Lingkaran\t\t||")
    bangun = ["Persegi", "Persegi Panjang", "Jajar Genjang", "Trapesium", "Belah Ketupat", "Layang-Layang", "Segitiga", "Lingkaran"]
    
    EROR = True
    while (EROR): 
        try:
            indeks = int(input("\nBangun apa yang ingin anda pilih? (Angkanya saja):     "))
            if (indeks >= 1 and indeks <= 8):
                EROR = False
                print("Anda Memilih bangun {}\n".format(bangun[indeks-1]))   
            elif(indeks == 0):
                showMenu1()
            else:
                print("Masukkan angka diantara 1 - 8")
        except ValueError:
            print("Input anda salah, Masukkan angka diantara 1 - 8")

    EROR = True
    while (EROR): 
        pil = input("LUAS / KELILING? :    ")
        if (str.upper(pil) == "LUAS" or str.upper(pil) == "KELILING"):
            EROR = False
            print("Anda Memilih {} {}\n\n".format(str.capitalize(pil), bangun[indeks-1]))
        else:
            print("Input anda salah!")
            


    if (indeks == 1):
        hasil = persegi(pil, indeks)

    elif (indeks == 2):
        hasil = persegiPanjang(pil, indeks)
    
    elif (indeks == 3):
        hasil = jajarGenjang(pil, indeks)
    
    elif (indeks == 4):
        hasil = trapesium(pil, indeks)
    
    elif (indeks == 5):
        hasil = belahKetupat(pil, indeks)
    
    elif (indeks == 6):
        hasil = layangLayang(pil, indeks)
    
    elif (indeks == 7):
        hasil = segitiga(pil, indeks)
    
    elif (indeks == 8):
        hasil = lingkaran(pil, indeks)

    i += 1
    riwayat.append("[{}] Nama: {}, \nBangun yang dipilih: {},  \n{},  \nHasil = {}cm^2\n\n".format(i, str.capitalize(user), bangun[indeks-1], str.capitalize(pil), hasil))  
    showMenu1()



def editHistory():
    print("\n\n")
    for j in range(len(riwayat)):
        print(str(riwayat[j]))
    EROR = True
    while(EROR):
        try:
            try:    
                ubah = int(input("Indeks ke berapa yang ingin anda ubah?:    "))
                if (ubah == 0):
                    showMenu1()
                elif (ubah > 1):
                    del riwayat[ubah-1]
                    EROR = False
                else:
                    print("Input anda salah!!")        
            except IndexError:
                print("Mohon maaf, anda salah memasukkan Index!!")
        except ValueError:
            print("Input anda salah, Masukkan angka!!")

    print("\n\n==========================")
    print("Silahkan Ubah")
    print("==========================\n")
    print("[1] Persegi\t\t||")
    print("[2] Persegi panjang\t||")
    print("[3] Jajar Genjang\t||")
    print("[4] Trapesium\t\t||")
    print("[5] Belah Ketupat\t||")
    print("[6] Layang-Layang\t||")
    print("[7] Segitiga\t\t||")
    print("[8] Lingkaran\t\t||")
    bangun = ["Persegi", "Persegi Panjang", "Jajar Genjang", "Trapesium", "Belah Ketupat", "Layang-Layang", "Segitiga", "Lingkaran"]
    
    EROR = True
    while (EROR): 
        try:
            indeks = int(input("\nBangun apa yang ingin anda pilih? (Angkanya saja):     "))
            if (indeks >= 1 and indeks <= 8):
                EROR = False
                print("Anda Memilih bangun {}\n".format(bangun[indeks-1]))   
            else:
                print("Masukkan angka diantara 1 - 8")
        except ValueError:
            print("Input anda salah, Masukkan angka diantara 1 - 8")

    EROR = True
    while (EROR): 
        pil = input("LUAS / KELILING? :    ")
        if (str.upper(pil) == "LUAS" or str.upper(pil) == "KELILING"):
            EROR = False
            print("Anda Memilih {} {}\n\n".format(str.capitalize(pil), bangun[indeks-1]))
        else:
            print("Input anda salah!")
            


    if (indeks == 1):
        hasil = persegi(pil, indeks)

    elif (indeks == 2):
        hasil = persegiPanjang(pil, indeks)
    
    elif (indeks == 3):
        hasil = jajarGenjang(pil, indeks)
    
    elif (indeks == 4):
        hasil = trapesium(pil, indeks)
    
    elif (indeks == 5):
        hasil = belahKetupat(pil, indeks)
    
    elif (indeks == 6):
        hasil = layangLayang(pil, indeks)
    
    elif (indeks == 7):
        hasil = segitiga(pil, indeks)
    
    elif (indeks == 8):
        hasil = lingkaran(pil, indeks)

    riwayat.insert(ubah-1, "[{}] Nama: {}, \nBangun yang dipilih: {},  \n{},  \nHasil = {}cm^2\n\n".format(i, str.capitalize(user), bangun[indeks-1], str.capitalize(pil), hasil))  
    print("Data Berhasil diubah!")
    showMenu1()

def lihatHistory():
    print("\n\n")
    if (len(riwayat) < 1):
        print("=====================================")
        print("History Kosong!")
        print("=====================================")
    else:    
        print("History:")
        print("=====================================")
        for j in range(len(riwayat)):
            print(str(riwayat[j]))
        print("=====================================")
    showMenu1()
    
def hapusHistory():
    for j in range(len(riwayat)):
        print(str(riwayat[j]))
    EROR = True
    while(EROR):
            buang = input("Anda ingin menghapus semuanya?:    ")
            if (str.upper(buang) == "TIDAK"):
                EROR = True
                while(EROR):
                    try:
                        hapus = int(input("Indeks ke berapa yang ingin anda hapus?:    "))
                        if (hapus == 0):
                            showMenu1()
                        else:    
                            del riwayat[hapus-1]
                            print("History Berhasil dihapus!\n\n")
                            EROR = False
                            showMenu1()
                    except ValueError:
                        print("Input anda salah, Masukkan Angka!!!")        
                    except IndexError:
                        print("Mohon maaf, anda salah memasukkan Index!!")
            elif (str.upper(buang) == "YA"):
                riwayat.clear()
                print("History Berhasil dibersihkan!\n\n")
                EROR = False
                showMenu1()
            elif (str.upper(buang) == "0"):
                showMenu1()
            else:
                print("Input anda salah!!")    

def exitMenu():
    save = True
    while(save):
        simpan = input("Apakah anda ingin Menyimpan History dalam file Text? (YA / TIDAK):    ")
        if (str.upper(simpan) == "YA"):
            file_history = open("history.txt", "a")
            for i in range(len(riwayat)):
                history = str(riwayat[i])
                file_history.write(history)
            file_history.close()
            print("History anda Tersimpan!")   
            print("\n\n\n\nTerima Kasih telah menggunakan Program Kami!\n\n\n\n")    
            exit()
        elif (str.upper(simpan) == "TIDAK"): 
            print("\n\n\n\nTerima Kasih telah menggunakan Program Kami!\n\n\n\n")       
            exit()
        elif (str.upper(simpan) == "0"):
            showMenu1()
        else:
            print("Input Anda Salah!!!")



def showMenu1():
    print(15*"\n")
    print("[1] Lanjut Menghitung")
    print("[2] Edit History")
    print("[3] Lihat History")
    print("[4] Hapus History")
    print("[0] Exit")
    ulangi = True
    while(ulangi):
        selected_menu = str(input("Pilih menu yang ingin anda pilih >>>    "))
        print("([0] Untuk membatalkan pilihan)\n\n")
        if(selected_menu == "1"):
            print(43*"\n")
            mulaiMenghitung(user)
            ulangi = False
        elif(selected_menu == "2"):
            editHistory()
            ulangi = False
        elif(selected_menu == "3"):
            lihatHistory()
            ulangi = False
        elif(selected_menu == "4"):
            hapusHistory()
            ulangi = False
        elif (selected_menu == "0"):
            exitMenu()
        else:
            print("Kamu memilih menu yang salah!")



user = ""
while (user == ""):
    user = input("\n\nMasukkan Nama anda :    ")
    print("\n\t\t\tSelamat datang!,  {}".format(str.capitalize(user)))
    print("\t\t//====================================================\\\\")
    print("\t\t|| \t\t\t\t\t\t  === ||")
    print("\t\t||\t\t\t\t\t\t      ||")
    print("\t\t|| Aplikasi Penghitung Luas dan Keliling Bangun datar ||")
    print("\t\t||\t\t\t\t\t\t      ||")
    print("\t\t||\t\t\t\t\t\t      ||")
    print("\t\t\\\\=========================||=========================//\n\n")
    mulaiMenghitung(user)   
