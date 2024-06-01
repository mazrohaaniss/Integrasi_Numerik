import time
import math

def f(x):
    return 4 / (1 + x**2)

def simpson_one_third_integration(func, a, b, n):
    """
    Menghitung nilai integral fungsi 'func' dari 'a' ke 'b'
    menggunakan metode Integrasi Simpson 1/3 dengan 'n' subinterval.
    """
    if n % 2 != 0:
        raise ValueError("Jumlah subinterval harus genap.")

    h = (b - a) / n
    integral = func(a) + func(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * func(x)
        else:
            integral += 4 * func(x)

    integral *= h / 3
    return integral

# Batas integral
a = 0
b = 1

# Nilai referensi
reference_value = math.pi

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Simpan hasil integral dan waktu eksekusi
results = []

# Hitung integral untuk setiap nilai N
for N in N_values:
    start_time = time.time()
    integral_value = simpson_one_third_integration(f, a, b, N)
    end_time = time.time()
    execution_time = end_time - start_time
    error = abs(integral_value - reference_value)
    results.append((N, integral_value, error, execution_time))

# Cetak hasil
print("-----------------------------------------------------------------------------")
print("N\tPi\t\t\tGalat RMS\t\tWaktu Eksekusi")
print("-----------------------------------------------------------------------------")
for result in results:
    print(f"{result[0]}\t{result[1]}\t{result[2]}\t{result[3]}")
    

