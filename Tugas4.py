angka = int(input("Masukkan nilai desimal: "))
# Konversi Desimal ke Oktal
desimal_ke_oktal = oct(angka)[2:]
# Konversi Desimal ke Hexadesimal
desimal_ke_hex = hex(angka)[2:]

# Konversi dan output hasil
print("\nNilai oktal: ", desimal_ke_oktal)
print("Nilai hexadesimal: ", desimal_ke_hex)
