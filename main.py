#Baris atau Deret Aritmatika
#Rumus Baris aritmatika "Un = a + (n-1) x b"
#Rumus Deret aaritmatika "Sn = n/2 x (a+Un)"
import os

lanjut = "y"
while lanjut.lower() == "y":
    os.system('cls')
    print("====== Baris atau Deret Aritmatika ======")
    print("Pilih menu yang akan: \n1. Baris Aritmatika \n2. Deret Aritmatika")
    pilih = int(input("Masukan Nomor menu: "))
    os.system('cls')
    if pilih == 1:
        print("===== MENGHITUNG BARIS ARITMATIKA =====")
        a = int(input("Masukan Suku Pertama(a): "))
        b = int(input("Masukan beda atau selisih bilangan(b): "))
        n = int(input("Masukan banyak suku(n): "))
        un = a + (n-1)*b
        print ("Maka diketahui suku baris adalah U",n,"=",int(un))
    elif pilih == 2:
        print("===== MENGHITUNG BARIS ARITMATIKA =====")
        a = int(input("Masukan Suku Pertama(a): "))
        b = int(input("Masukan beda atau selisih bilangan(b): "))
        n = int(input("Masukan banyak suku(n): "))
        un = a + (n-1)*b
        print("Maka ditemukan suku barisnya adalah: U",n,"=",un)
        sn = n/2*(a+un)
        print("Jumlah Sn =",int(sn))
    else:
        print("============================================")
        print("YEEE ERROORR YEEEEE!!! \nPilih nomor yang terdaftar \npada menu ya.")
    print("============================================")

    lanjut = input("Lanjut berhitung yang lain? y/n: ")
    if lanjut == "n":
        break
