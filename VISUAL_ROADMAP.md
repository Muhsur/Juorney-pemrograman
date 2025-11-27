# 🎓 KONSEP PROGRAMMING YANG WAJIB DIPAHAMI PEMULA

## Level 1: Basic Concepts (Wajib Dikuasai)

### 1. VARIABEL & DATA TYPES
```python
# Variabel adalah "tempat penyimpanan" nilai
nama = "Budi"           # String - teks
umur = 25               # Integer - bilangan bulat
tinggi = 5.9            # Float - bilangan desimal
aktif = True            # Boolean - true/false

# Menampilkan tipe data
print(type(nama))       # <class 'str'>
print(type(umur))       # <class 'int'>

# Mengubah tipe data
angka_text = "123"
angka_int = int(angka_text)  # Convert string ke int
```

**Mengapa penting?**
- Setiap data di program disimpan dalam variable
- Berbagai data type untuk berbagai keperluan
- Type conversion sering dibutuhkan

---

### 2. OPERATORS
```python
# ARITHMETIC OPERATORS
hasil_tambah = 5 + 3        # 8
hasil_kurang = 10 - 4       # 6
hasil_kali = 5 * 3          # 15
hasil_bagi = 10 / 3         # 3.333...
hasil_bagi_bulat = 10 // 3  # 3
sisa_bagi = 10 % 3          # 1
pangkat = 2 ** 3            # 8

# COMPARISON OPERATORS (return True/False)
apakah_sama = (5 == 5)      # True
apakah_beda = (5 != 3)      # True
apakah_lebih_besar = (5 > 3)  # True
apakah_lebih_kecil = (5 < 10)  # True
apakah_lebih_atau_sama = (5 >= 5)  # True

# LOGICAL OPERATORS
syarat1 = (5 > 3)
syarat2 = (10 < 20)
hasil_and = syarat1 and syarat2    # True (kedua harus true)
hasil_or = syarat1 or syarat2      # True (salah satu cukup true)
hasil_not = not syarat1            # False (kebalikan)
```

**Mengapa penting?**
- Operators adalah "action" dalam programming
- Akan digunakan di hampir setiap program
- Essential untuk control flow logic

---

### 3. CONTROL FLOW - IF STATEMENTS
```python
# IF - jika kondisi true, jalankan code
nilai = 80
if nilai >= 80:
    print("Lulus dengan nilai A")

# IF-ELSE - dua pilihan
umur = 15
if umur >= 18:
    print("Anda sudah dewasa")
else:
    print("Anda masih anak-anak")

# IF-ELIF-ELSE - banyak pilihan
skor = 75
if skor >= 85:
    print("Grade A")
elif skor >= 75:
    print("Grade B")
elif skor >= 65:
    print("Grade C")
else:
    print("Grade D - Not Passed")

# NESTED IF (if dalam if)
umur = 20
pendapatan = 5000000
if umur >= 18:
    if pendapatan >= 2000000:
        print("Bisa apply credit card")
    else:
        print("Pendapatan belum cukup")
else:
    print("Terlalu muda untuk apply")
```

**Mengapa penting?**
- Decision making adalah core dari programming
- Kontrol alur program berdasarkan kondisi
- Digunakan di setiap program modern

---

### 4. LOOPS - FOR & WHILE

#### FOR LOOP (loop dengan jumlah pasti)
```python
# Bentuk dasar
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# Loop melalui list
buah = ["apel", "mangga", "jeruk"]
for fruit in buah:
    print(fruit)

# Loop dengan enumerate (index + value)
for index, fruit in enumerate(buah):
    print(f"{index}: {fruit}")

# Loop dengan range(start, end, step)
for i in range(1, 6):      # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8 (step 2)
    print(i)
```

#### WHILE LOOP (loop dengan kondisi)
```python
# Jalankan selama kondisi true
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# Menu loop (umum di aplikasi)
while True:
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    choice = input("Choose: ")
    
    if choice == "1":
        print("Anda pilih 1")
    elif choice == "2":
        print("Anda pilih 2")
    elif choice == "3":
        break  # keluar dari loop
    else:
        print("Invalid choice")

# BREAK & CONTINUE
for i in range(10):
    if i == 5:
        break  # keluar dari loop
    print(i)

for i in range(10):
    if i == 3:
        continue  # skip ke iterasi berikutnya
    print(i)
```

**Mengapa penting?**
- Menjalankan kode berulang kali (sangat penting!)
- Meproses list/data secara otomatis
- Menu-driven aplikasi menggunakan while True + break

---

### 5. LISTS (Kumpulan Data Terurut)
```python
# Create list
buah = ["apel", "mangga", "jeruk"]
angka = [10, 20, 30, 40, 50]
mixed = [1, "hello", 3.14, True]

# Indexing (akses element berdasarkan posisi)
print(buah[0])   # "apel" (index mulai dari 0)
print(buah[1])   # "mangga"
print(buah[-1])  # "jeruk" (index negative: -1 = last)

# Slicing (ambil range dari list)
print(buah[0:2])    # ["apel", "mangga"] (index 0-1)
print(buah[1:])     # ["mangga", "jeruk"] (dari index 1 ke end)
print(buah[:2])     # ["apel", "mangga"] (dari start ke index 1)

# List Methods
buah.append("pisang")        # tambah di akhir
buah.insert(1, "blueberry")  # tambah di posisi 1
buah.remove("mangga")        # hapus element tertentu
buah.pop()                   # hapus element terakhir
buah.pop(0)                  # hapus element di index 0

# Lain-lain
print(len(buah))             # jumlah element
print("apel" in buah)        # cek ada atau tidak
angka.sort()                 # sort ascending
angka.reverse()              # reverse order
```

**Mengapa penting?**
- Menyimpan banyak data dalam satu variable
- Akan digunakan di hampir setiap program
- Foundation untuk data structures yang lebih kompleks

---

### 6. DICTIONARIES (Key-Value Pairs)
```python
# Create dictionary
siswa = {
    "nama": "Budi",
    "umur": 20,
    "kelas": "A"
}

# Akses value dengan key
print(siswa["nama"])        # "Budi"
print(siswa["umur"])        # 20

# Add/Update
siswa["email"] = "budi@gmail.com"  # tambah key baru
siswa["umur"] = 21                 # update value

# Delete
del siswa["email"]          # hapus key

# Dictionary Methods
print(siswa.keys())         # semua keys
print(siswa.values())       # semua values
print(siswa.items())        # key-value pairs

# Loop through dictionary
for key, value in siswa.items():
    print(f"{key}: {value}")

# Cek key exist
if "nama" in siswa:
    print("Key 'nama' ada")
```

**Mengapa penting?**
- Menyimpan data terstruktur (seperti object)
- Lebih readable dari nested lists
- Foundation untuk OOP (Object-Oriented Programming)

---

## Level 2: Intermediate Concepts

### 7. FUNCTIONS
```python
# BASIC FUNCTION
def sapa(nama):
    """Fungsi untuk sapa seseorang"""
    print(f"Halo, {nama}!")

sapa("Andi")  # Call function

# FUNCTION DENGAN RETURN
def tambah(a, b):
    return a + b

hasil = tambah(5, 3)  # hasil = 8
print(hasil)

# FUNCTION DENGAN DEFAULT PARAMETER
def greet(nama="User", waktu="pagi"):
    return f"Selamat {waktu}, {nama}!"

print(greet())                      # default values
print(greet("Budi"))                # override nama
print(greet("Budi", "sore"))        # override keduanya
print(greet(waktu="malam"))         # keyword argument

# FUNCTION DENGAN MULTIPLE PARAMETERS & RETURN
def calculate(a, b, operation="+"):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b

# SCOPE (variable visibility)
global_var = "saya global"

def fungsi():
    local_var = "saya lokal"
    print(global_var)  # bisa akses
    print(local_var)   # bisa akses

print(global_var)  # bisa akses
# print(local_var)  # ERROR - tidak bisa akses dari luar
```

**Mengapa penting?**
- Reusable code (jangan repeat-repeat)
- Membuat code lebih organized
- Essential untuk modularitas

---

### 8. STRING MANIPULATION
```python
# String adalah teks
text = "Halo Dunia"

# Indexing & Slicing
print(text[0])        # "H"
print(text[5:])       # "Dunia"
print(text[:4])       # "Halo"

# String Methods
print(text.lower())      # "halo dunia"
print(text.upper())      # "HALO DUNIA"
print(text.split())      # ["Halo", "Dunia"]
print(text.replace("Dunia", "Python"))  # "Halo Python"
print(text.startswith("Halo"))  # True
print(text.endswith("Dunia"))   # True
print(len(text))  # 10

# String Formatting
nama = "Budi"
umur = 25
print(f"Nama saya {nama}, umur {umur}")  # f-string (recommended)
print("Nama saya {}, umur {}".format(nama, umur))  # .format()
```

---

### 9. ERROR HANDLING (Try-Except)
```python
# Program bisa error, kita handle dengan try-except
try:
    hasil = 10 / 0  # Ini akan error
except ZeroDivisionError:
    print("Tidak bisa bagi dengan nol!")

# Multiple except
try:
    angka = int("abc")  # Error: tidak bisa convert
except ValueError:
    print("Input harus berupa angka!")
except Exception as e:
    print(f"Error: {e}")

# Try-except-finally
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File tidak ditemukan!")
finally:
    print("Cleanup complete")  # Selalu dijalankan
```

---

### 10. READING & WRITING FILES
```python
# WRITE ke file
with open("data.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("Ini baris kedua\n")

# READ dari file
with open("data.txt", "r") as f:
    content = f.read()  # Read semua
    print(content)

# READ line by line
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())

# APPEND ke file (tambah tanpa overwrite)
with open("data.txt", "a") as f:
    f.write("Baris tambahan\n")
```

---

## 🧠 MENTAL MODEL UNTUK PEMULA

```
┌─────────────────────────────────────────────────┐
│  PROGRAM FLOW:                                  │
│                                                 │
│  1. INPUT (terima data dari user)               │
│     ↓                                           │
│  2. PROCESS (proses data dengan logic)          │
│     - Variables menyimpan data                  │
│     - Operators melakukan operasi               │
│     - If/loops mengontrol alur                  │
│     - Functions organize code                   │
│     ↓                                           │
│  3. OUTPUT (display hasil ke user)              │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## ✅ CHECKLIST PEMAHAMAN

Jika sudah bisa jawab SEMUA pertanyaan ini, Anda siap lanjut ke Phase 2:

- [ ] Apa perbedaan antara int, float, string, boolean?
- [ ] Kapan pakai for loop vs while loop?
- [ ] Bagaimana cara akses element di list?
- [ ] Apa bedanya list dan dictionary?
- [ ] Kenapa perlu function?
- [ ] Bagaimana cara membaca & menulis file?
- [ ] Apa itu try-except dan kapan digunakan?
- [ ] Bisa bikin program mini dengan kombinasi konsep di atas?

Jika menjawab "tidak" ke salah satu, kembali ke consep tersebut dan practice lagi!

---

## 🎯 PRACTICE EXERCISES

Untuk setiap konsep, coba bikin program mini:

1. **Variables & Data Types**
   - Bikin program yang minta input nama, umur, tinggi
   - Calculate BMI dan display hasilnya

2. **Operators**
   - Calculator yang support +, -, *, /

3. **If Statements**
   - Grade system berdasarkan nilai

4. **Loops**
   - Print multiplication table
   - Menu-driven program

5. **Lists & Functions**
   - To-do list app

6. **Dictionaries**
   - Simple phonebook

7. **File I/O**
   - Save dan load data ke file

---

**INGAT:** Jangan hanya baca, tapi PRAKTIK! Ketik ulang code sendiri, modify, experiment! 🚀
