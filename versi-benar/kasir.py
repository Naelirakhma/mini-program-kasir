print("===================================")
print("       MINI PROGRAM KASIR")
print("===================================")

nama_barang = input("Nama barang       : ")
harga = float(input("Harga barang      : Rp "))
jumlah = int(input("Jumlah barang     : "))

subtotal = harga * jumlah

print("\n--- PILIHAN DISKON ---")
print("1. Tidak ada diskon")
print("2. Diskon 10%")
print("3. Diskon 20%")

pilihan_diskon = input("Pilih diskon (1/2/3): ")

if pilihan_diskon == "1":
    diskon = 0
elif pilihan_diskon == "2":
    diskon = 10
elif pilihan_diskon == "3":
    diskon = 20
else:
    diskon = 0

potongan = subtotal * diskon / 100
total = subtotal - potongan

print("\n===================================")
print("           STRUK PEMBAYARAN")
print("===================================")
print("Barang       :", nama_barang)
print("Harga        : Rp", harga)
print("Jumlah       :", jumlah)
print("Subtotal     : Rp", subtotal)
print("Diskon       :", diskon, "%")
print("Potongan     : Rp", potongan)
print("Total        : Rp", total)

uang = float(input("\nUang pelanggan : Rp "))

kembalian = total + uang

print("Kembalian     : Rp", kembalian)
print("===================================")
print("Terima kasih!")