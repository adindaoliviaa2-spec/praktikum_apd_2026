
print ("Selamat datang di OlivTopUP!")

valid_username = "olivia"
valid_password = "88"

username = input("Masukan username: ")
password = input("Masukan password: ")

if username == valid_username and password == valid_password:
    print("Login berhasil!")
    print("Hai, " + username + "! Hari ini mau Topup apa?")
    print ("pilihan topup yang tersedia: ")
    game = ["Genshin Impact", "Minecraft", "Mobile Legends"]
    print ("1. Genshin Impact")
    print ("2. Minecraft")
    print ("3. Mobile Legends")
    pilihan = input("Mau game yang mana? (1-3): ")
    if pilihan == "1":
        print("You have selected Genshin Impact.")
    elif pilihan == "2":
        print("You have selected Minecraft.")
    elif pilihan == "3":
        print("You have selected Mobile Legends.")
    else:
        print("Pilihan tidak valid. silakan pilih antara 1, 2, atau 3.")
        exit()
    
else:
    print("Invalid username or password.")
    exit()

id = input("Masukkan ID Game: ")
kategori_topup = {"1": 15000, "2": 50000, "3": 150000}
print("Kategori Topup yang tersedia: ")
print ("1. Kecil = 15.000")
print ("2. menengah = 50.000")
print ("3. Besar = 150.000")
kategori_topup = input("Masukkan kategori topup (1-3): ")
if kategori_topup == "1":
    harga = 15000
    print("anda telah memilih kategori topup 1.")
elif kategori_topup == "2":
    harga = 50000
    print("anda telah memilih kategori topup 2.")
elif kategori_topup == "3":
    harga = 150000
    print("anda telah memilih kategori topup 3.")
else:
    print("Kategori topup tidak valid. Silakan pilih antara '1', '2', atau '3'.")
    exit()

metode_pembayaran = ["Pulsa","E-wallet"]
print("Metode pembayaran yang tersedia: ")
print ("1. Pulsa")
print ("2. E-wallet")
metode_pembayaran = input("Pilih metode pembayaran (1-2): ")
if metode_pembayaran == "1":
    print("Metode pembayaran yang dipilih: Pulsa")
elif metode_pembayaran == "2":
    print("Metode pembayaran yang dipilih: E-wallet")
else:
    print("Metode pembayaran tidak valid. Silakan pilih antara 1 atau 2.")
    exit()

pulsa = 2500
E_wallet = 500
total_pembayaran = harga + pulsa if metode_pembayaran == "1" else harga + E_wallet if metode_pembayaran == "2" else None
print("Total pembayaran: ", total_pembayaran)

pembayaran = input("silahkan masukan jumlah pembayaran: ")
if metode_pembayaran == "1" or metode_pembayaran == "2":
     int(pembayaran) >= total_pembayaran
     kembalian = int(pembayaran) - total_pembayaran
     print("Pembayaran berhasil!")
else:
        print("Pembayaran gagal! Jumlah pembayaran tidak mencukupi.")
        exit()

print("==================================")
print ("ID Player: " + id)
print ("Game yang dipilih: " + game[int(pilihan)-1])
print ("Kategori Topup: " + str(harga))
print ("Metode Pembayaran: ",str("pulsa" if metode_pembayaran == "1" else "E-wallet"))
print ("biaya Admin: " + str(pulsa if metode_pembayaran == "1" else E_wallet))
print ("total pembayaran: ",total_pembayaran)
print ("total yang dibayar: ",pembayaran)
print ("total kembalian: ",kembalian)
print ("terimakasih sudah berbelanja di OlivTopUp!")
print ("==================================")