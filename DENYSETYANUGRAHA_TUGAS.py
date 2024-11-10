import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([10, 20, 30, 40, 50])

hasil = array1 + array2
print("Data awal:")
print("Array1:", array1)
print("Array2:", array2)
print("\nHasil penjumlahan array1 dan array2:", hasil)

print("\nAritmetika")
import pandas as pd

data = {
        'A' : [11, 21, 33],
        'B' : [7, 2, 3]
        }
df = pd.DataFrame(data)

print("Data awal: ")
print(df)

df['C'] = df['A'] + df['B'] 
df['D'] = df['A'] - df['B'] 
df['E'] = df['A'] * df['B'] 
df['F'] = df['A'] / df['B'] 

print("\nData awal setelah memakai aritmetika: ")
print(df)

print("\nData tabel")
import pandas as pd

data = {
    'Nama': ['Andi', 'Budi', 'Cici', 'Dodi', 'Eka', 'Fajar', 'Gita', 'Hani', 'Ivan', 'Joko']
}
df = pd.DataFrame(data)

atas = df.head(5)

bawah = df.tail(5)

print("Keseluruhan: ")
print(df)

print("\nLima data teratas:")
print(atas)

print("\nLima data terbawah:")
print(bawah)

