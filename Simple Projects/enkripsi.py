import cryptocode


kunci=[]
i=0
x=0
print("----------------------------------------------")
pesan=input("Masukan Pesan : ")
print("----------------------------------------------")
jumlah_kunci=int(input("Berapa kali pesan tersebut ingin dikunci?  : "))
print("----------------------------------------------")


def pengunci(pesan, jumlah_kunci, i, x):

    if jumlah_kunci > 1:
        x+=1
        print("Kunci ke ", x)
        kunci.append((input("Masukan Kunci : ")))
        pesan_rahasia=cryptocode.encrypt(pesan, kunci[i])
        jumlah_kunci-=1
        i+=1
        print("")
        return pengunci(pesan_rahasia, jumlah_kunci, i, x)
    
    else:
        x+=1
        print("Kunci ke ", x)
        kunci.append((input("Masukan Kunci : ")))
        print("----------------------------------------------")
        pesan_rahasia=cryptocode.encrypt(pesan, kunci[i])
        return pesan_rahasia
      

print("Pesan rahasia untuk" ,"'",pesan,"'" ,"adalah :", pengunci(pesan, jumlah_kunci, i, x))
print("")
print("Jumlah Penguncian :", jumlah_kunci)
print("Isi Kunci :", kunci)
print("----------------------------------------------")

