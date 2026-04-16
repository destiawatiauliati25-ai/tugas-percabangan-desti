score = int(input("Masukkan score nilai anda: "))
absensi = int(input("Masukkan score absensi anda: "))

if (score >70 and absensi > 50) :
    print("lulus")
elif (score <70 and absensi >70) or (score >70 and absensi <50) :
    print("boleh perbaikan")
else :
    print("tidak lulus dan tidak bisa perbaikan")
