import cryptocode

kunci=[]

pesan_rahasia=input("Masukan Pesan Rahasia : ")
print("")
jumlah_kunci=int(input("Masukan Jumlah Kunci : "))


i=jumlah_kunci
x=0
print("")


#membuka pesan rahasia

def pembuka(pesan_rahasia, jumlah_kunci, i, x):

    if jumlah_kunci > 0:
        x+=1
        print("Kunci ke ", x)
        kunci.append(input("Masukan Kunci : "))
        jumlah_kunci-=1
        print("")
        return pembuka(pesan_rahasia, jumlah_kunci, i, x)
    else:
        pesan_asli=cryptocode.decrypt(pesan_rahasia, kunci[i-1])
        i-=1
        if i > 0:
            return pembuka(pesan_asli, jumlah_kunci, i, x)
        else:
            return pesan_asli

print("Pesan asli : ", pembuka(pesan_rahasia, jumlah_kunci, i, x))
print("")


