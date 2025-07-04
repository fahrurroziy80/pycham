def mesin_kasir():
    daftar_belanja = []
    total_bayar = 0

    print("=== MESIN KASIR SEDERHANA ===")

    while True:
        nama = input("Nama barang     : ")
        harga = int(input("Harga satuan    : "))
        jumlah = int(input("Jumlah beli     : "))

        total = harga * jumlah
        total_bayar += total

        daftar_belanja.append({
            'nama': nama,
            'harga': harga,
            'jumlah': jumlah,
            'total': total
        })

        lagi = input("Tambah barang lain? (y/n): ").lower()
        if lagi != 'y':
            break

    print("\n=== STRUK PEMBELIAN ===")
    print("{:<20} {:<10} {:<10} {:<10}".format("Nama", "Harga", "Jumlah", "Total"))
    print("-" * 60)
    for barang in daftar_belanja:
        print("{:<20} {:<10} {:<10} {:<10}".format(
            barang['nama'], barang['harga'], barang['jumlah'], barang['total']
        ))

    print("-" * 60)
    print(f"Total yang harus dibayar: Rp{total_bayar:,}")

    bayar = int(input("Uang dibayarkan       : Rp"))
    kembalian = bayar - total_bayar
    print(f"Kembalian             : Rp{kembalian:,}")
    print("Terima kasih telah berbelanja!")


# Panggil fungsi
mesin_kasir()

