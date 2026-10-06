
for i in range(2):
 for j in range(3):
    print(f"{i} x {j} = {i*j}")
    #karna ada range 2 dan range 3, range(2) itu dimulai dari 0, 1
    #dipadukan dengan range(3) yaitu di mulai dari 0, 1, 2
    #perhitungan diulangi mencapai akhir range


jawab = "ya"
hitung = 0

while(jawab == "ya"):
  hitung += 1 # 0 -> 1
  jawab = input("mau lanjut?")

  print(f"jumlah perulangan: {hitung}")
  

for i in range(4):
  print(i)
  break

i = 0

while True:
  print(i)
  i += 2
  if i >= 11:
    break

for i in range(10):
  if i % 2 == 0:
    continue
  print(f"skip {i}")
  continue
print(f"berhasil print {i}")


for i in range(10):
  if i == 9:
    continue
  print("berhasil")
  elif i % 2 != 0:
  print(i)
  break

