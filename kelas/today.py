#lemari = ["baju", "celana", 69, 7,2, True, 70, 22, 240]

#angka1 = [ [1, 2], [3, 4] ]
#print(angka1[0][1])

#angka1 = [1, 3, 5]
#angka2 = [2, 4, 6]
#angka3 = angka1 + angka2
#print(angka3)
#ulang = angka1 * 3
#print(ulang)

# for index, item in enumerate(lemari):
  #  print(f"Index ke-{index, + 1} : {item}")

#print("sebelum diubah")
#print(lemari)
#lemari[4] = "kolor"
#print("sesudah diubah")
#print(lemari)

#print("sebelum diubah")
#print(lemari)
#hapus = "baju"
#lemari.remove(hapus)
#del lemari[1]
#lemari[0:2] = ["baju baru", "celana baru"]
#print("sesudah diubah")
#print(lemari)
#sisa = lemari.pop(2)
#print(sisa)

#angka = (1, 2, 3, "halo", True)
#ubah = list(angka)
#ubah.append("hai")

#angka = tuple(ubah)
#print(angka)

lemari = ("baju", "celana", "sepatu")
(atasan, *bawahan) = lemari

print(bawahan)

