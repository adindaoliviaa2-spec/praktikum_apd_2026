
valid_username = "olivia"
valid_pin = "088"


for i in range(1,4):
    username = input("Masukan username: ")
    pin = input("Masukan pin: ")
    if username == valid_username and pin == valid_pin:
        print("Login berhasil!")
        
    else:
        sisa = 3 - i
        if sisa > 0:
         print(f"Username atau pin salah! Sisa kesempatan: {sisa}")
        else:
         print("Input salah 3 kali! Akun Anda terblokir.")
        break
saldo = 120000
while True:
    print("\n===================")
    print("|[1] Cek Saldo    |\n"
          "|[2] tarik tunai  |\n"
          "|[3] setor tunai  |\n"
          "|[4] Keluar       |")
    print("===================")
    user = input("Masukan pilihan: ")
    if user == "1":
        print(f"Saldo anda saat ini: {saldo}")
    elif user == "2":
        print("Pilihan tarik tunai: \n"
              "50000\n"
              "100000\n")
        tarik = int(input("Masukan jumlah tarik tunai: "))
        if tarik % 50000 != 0:
            print("Nominal harus kelipatan 50000!")
        elif tarik <= 0:
            print("Nominal harus diatas 0.")
        else:
            saldo -= tarik
            print(f"Tarik tunai berhasil! Saldo anda saat ini: {saldo}")
    elif user == "3":
        setor = int(input("Masukan jumlah setor tunai: "))
        if setor > 0:
            saldo += setor
            print(f"Setor tunai berhasil! Saldo anda saat ini: {saldo}")
        else:
            print("Nominal harus diatas 0.")
    elif user == "4":
        break  

