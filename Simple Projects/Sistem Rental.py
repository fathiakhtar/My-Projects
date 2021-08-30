print("----------------------")
print("Rental Mobil Pak jaya")
print("----------------------")
print("1. Avamza = 5jt/jam")
print("2. Terios = 4jt/jam")
print("3. Pickup = 7jt/jam")
print("4. Kijang = 5jt/jam")
print("5. Ertiga = 5jt/jam")
user = input("Pilih Mobil Mana yang anda akan Sewa (ketik dalam bentuk angka saja): ")
if user == "1":
    jumlah_sewa_avanza = int(input("Berapa jam anda sewa? ketik dalam bentuk angka "))
    total = 5000000 * jumlah_sewa_avanza
    print("Anda akan menyewa Avanza selama " + str(jumlah_sewa_avanza) + " jam")
    print("Total biaya Rp " + str(total) )
    konfirmasi = input("Konfirmasi pemesanan? ketika ya untuk melanjutkan, ketik tidak untuk membatalkan : ")
    if konfirmasi == "ya":
        print("Pesanan anda telah diteruskan ke si penyewa")
    elif konfirmasi == "tidak":
        print("pesanan dibatalkan")
    else:
        print("input tidak jelas")
elif user == "2":
    jumlah_sewa_terios = int(input("Berapa jam anda sewa? ketik dalam bentuk angka "))
    total = 4000000 * jumlah_sewa_terios
    print("Anda akan menyewa Terios selama " + str(jumlah_sewa_terios) + " jam")
    print("Total biaya Rp " + str(total) )
    konfirmasi = input("Konfirmasi pemesanan? ketika ya untuk melanjutkan, ketik tidak untuk membatalkan : ")
    if konfirmasi == "ya":
        print("Pesanan anda telah diteruskan ke si penyewa")
    elif konfirmasi == "tidak":
        print("pesanan dibatalkan")
    else:
        print("input tidak jelas")
elif user == "3":
    jumlah_sewa_pickup = int(input("Berapa jam anda sewa? ketik dalam bentuk angka "))
    total = 4000000 * jumlah_sewa_pickup
    print("Anda akan menyewa Pickup selama " + str(jumlah_sewa_pickup) + " jam")
    print("Total biaya Rp " + str(total) )
    konfirmasi = input("Konfirmasi pemesanan? ketika ya untuk melanjutkan, ketik tidak untuk membatalkan : ")
    if konfirmasi == "ya":
        print("Pesanan anda telah diteruskan ke si penyewa")
    elif konfirmasi == "tidak":
        print("pesanan dibatalkan")
    else:
        print("input tidak jelas")
elif user == "4":
    jumlah_sewa_kijang = int(input("Berapa jam anda sewa? ketik dalam bentuk angka "))
    total = 4000000 * jumlah_sewa_kijang
    print("Anda akan menyewa Kijang selama " + str(jumlah_sewa_kijang) + " jam")
    print("Total biaya Rp " + str(total) )
    konfirmasi = input("Konfirmasi pemesanan? ketika ya untuk melanjutkan, ketik tidak untuk membatalkan : ")
    if konfirmasi == "ya":
        print("Pesanan anda telah diteruskan ke si penyewa")
    elif konfirmasi == "tidak":
        print("pesanan dibatalkan")
    else:
        print("input tidak jelas")
elif user == "5":
    jumlah_sewa_ertiga = int(input("Berapa jam anda sewa? ketik dalam bentuk angka "))
    total = 4000000 * jumlah_sewa_ertiga
    print("Anda akan menyewa Ertiga selama " + str(jumlah_sewa_ertiga) + " jam")
    print("Total biaya Rp " + str(total) )
    konfirmasi = input("Konfirmasi pemesanan? ketika ya untuk melanjutkan, ketik tidak untuk membatalkan : ")
    if konfirmasi == "ya":
        print("Pesanan anda telah diteruskan ke si penyewa")
    elif konfirmasi == "tidak":
        print("pesanan dibatalkan")
    else:
        print("input tidak jelas")
else:
    print("input tidak valid")
                     
