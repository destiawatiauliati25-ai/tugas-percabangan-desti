harga = int(input("Masukkann Harga Barang: "))
if harga >= 100000 :
    diskon = harga * 0.10
    total_bayar = harga - diskon 
    print ("Anda mendapatkan diskon 10%")
    print ("jumlah diskon: ", diskon)

else :
    total_bayar = harga
    print ("Anda tidak mendapatkan diskon")
    
print ("Total yang harus dibayar: ", total_bayar)
