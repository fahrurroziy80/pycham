def analisis_investasi():

    harga_beli = float(input("Masukkan harga beli investasi: "))
    harga_jual = float(input("Masukkan harga jual investasi: "))
    jumlah_unit = int(input("Masukkan jumlah saham/unit: "))
    biaya_lainnya = float(input("Masukkan biaya lainnya (opsional): "))  # Biaya transaksi, dll.


    total_pembelian = harga_beli * jumlah_unit
    total_penjualan = harga_jual * jumlah_unit
    keuntungan_rugi = total_penjualan - total_pembelian - biaya_lainnya


    print(f"\n===== Hasil Analisis Investasi =====")
    if keuntungan_rugi > 0:
        print(f"Keuntungan Investasi: Rp {keuntungan_rugi:.2f}")
    elif keuntungan_rugi < 0:
        print(f"Kerugian Investasi: Rp {abs(keuntungan_rugi):.2f}")
    else:
        print("Tidak ada keuntungan atau kerugian.")


analisis_investasi()
