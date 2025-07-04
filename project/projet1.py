def faktorial(n):
  """
  Fungsi rekursif untuk menghitung faktorial.
  """
  if n == 0:  # Kasus dasar: faktorial dari 0 adalah 1
    return 1
  else:  # Langkah rekursif
    return n * faktorial(n-1)

# Contoh penggunaan
hasil = faktorial(5)
print(f"Faktorial dari 5 adalah: {hasil}")  # Output: Faktorial dari 5 adalah: 120