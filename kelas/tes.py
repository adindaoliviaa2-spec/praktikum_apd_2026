input_benar = "rahasia123"

# Perulangan akan berjalan maksimal 3 kali (i mulai dari 1 sampai 3)
for i in range(1, 4):
    tebakan = input("Masukkan password: ")
    
    if tebakan == input_benar:
        print("Akses diterima! Selamat datang.")
        break  # Berhenti jika jawaban benar
    else:
        sisa = 3 - i
        if sisa > 0:
            print(f"Input salah! Sisa kesempatan: {sisa}")
        else:
            print("Input salah 3 kali! Akun Anda terblokir.")
