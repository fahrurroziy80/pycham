def mesin_atm():
    daftar_penarikan = []
    total_penarikan = 0

    print("==== MESIN ATM SEDERHANA ====")

    while True:
        nama = input("Nama anda       : ")
        jumlah = int(input("Jumlah uang     : Rp"))
        jumlah_tarik = int(input("Jumlah penarikan: Rp"))


        total = jumlah_tarik
        total_penarikan += total

        daftar_penarikan.append({
            'nama': nama,
            'jumlah': jumlah,
            'total': total
        })

        tambah = input("Mau narik uang lagi? (Y/n): ").lower()
        if tambah != 'y':
            break

    # Tampilkan struk setelah selesai
    print("\n== BANK INDONESIA ==")
    print("{:<20} {:<15} {:<15}".format("Nama", "Saldo Awal", "Penarikan"))
    print("-" * 60)
    for bank in daftar_penarikan:
        print("{:<20} Rp{:<13,} Rp{:<13,}".format(
            bank['nama'], bank['jumlah'], bank['total']
        ))
    print("-" * 60)
    print(f"Total Penarikan         : Rp{total_penarikan:,}")

    bayar = int(input("Uang dibayarkan         : Rp"))
    kembalian = bayar - total_penarikan
    print(f"Kembalian               : Rp{kembalian:,}")
    print("Terima kasih telah menggunakan ATM!\n")

mesin_atm()
