# 🏋️ DAILY PRACTICE EXERCISES

Gunakan file ini untuk latihan setiap hari. Setiap minggu ada 5-7 exercises yang bisa dikerjakan dalam 30-60 menit.

---

## 📅 WEEK 1: VARIABLES, OPERATORS & BASIC INPUT/OUTPUT

### Exercise 1.1: Variable Practice
**File:** `exercise_1_1.py`
**Time:** 10 min
**Concepts:** Variables, print(), input()

```python
# TODO: 
# 1. Ask user untuk nama, umur, dan kota
# 2. Store dalam 3 variables
# 3. Display dengan format: 
#    "Halo [nama], umur [umur] tahun, dari [kota]"

# Example:
# Input: nama="Budi", umur=25, kota="Jakarta"
# Output: Halo Budi, umur 25 tahun, dari Jakarta

# STARTER CODE:
nama = input("Masukkan nama: ")
# TODO: tambahkan input untuk umur dan kota
# TODO: display hasil dengan format di atas
```

---

### Exercise 1.2: Calculator
**File:** `exercise_1_2.py`
**Time:** 15 min
**Concepts:** Operators, type conversion

```python
# TODO:
# 1. Ask user untuk 2 angka
# 2. Hitung: sum, difference, product, division
# 3. Display semua hasil

# Example:
# Input: 10 dan 5
# Output:
# 10 + 5 = 15
# 10 - 5 = 5
# 10 * 5 = 50
# 10 / 5 = 2.0

# STARTER CODE:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# TODO: calculate and display
```

---

### Exercise 1.3: Temperature Converter
**File:** `exercise_1_3.py`
**Time:** 15 min
**Concepts:** Math operations, formatting

```python
# TODO:
# 1. Ask user untuk suhu dalam Celsius
# 2. Convert ke Fahrenheit: F = (C * 9/5) + 32
# 3. Display hasilnya dengan 2 decimal places

# Example:
# Input: 25
# Output: 25°C = 77.00°F

# STARTER CODE:
celsius = float(input("Suhu dalam Celsius: "))
# TODO: calculate Fahrenheit dan display
```

---

### Exercise 1.4: Age Calculator
**File:** `exercise_1_4.py`
**Time:** 15 min
**Concepts:** Variables, print formatting

```python
# TODO:
# 1. Ask user untuk tahun lahir mereka
# 2. Calculate umur (assume current year = 2025)
# 3. Display: "[nama] berumur [umur] tahun"

# STARTER CODE:
nama = input("Nama: ")
tahun_lahir = int(input("Tahun lahir: "))
# TODO: calculate age dan display
```

---

### Exercise 1.5: Simple Variables Game
**File:** `exercise_1_5.py`
**Time:** 20 min
**Concepts:** String manipulation, variable operations

```python
# TODO:
# 1. Store 3 variabel: first_name, last_name, hobby
# 2. Create message yang menggabungkan semuanya
# 3. Display message berbeda-beda format

# Example:
# My name is [Full Name] and I like [hobby]
# [Full Name]'s favorite activity is [hobby]
# I'm [first_name], and [hobby] is my passion!

# Bikin minimal 3 message berbeda
```

---

## 🔀 WEEK 2: IF STATEMENTS & CONTROL FLOW

### Exercise 2.1: Grading System
**File:** `exercise_2_1.py`
**Time:** 15 min
**Concepts:** if/elif/else

```python
# TODO:
# 1. Ask user untuk nilai (0-100)
# 2. Determine grade:
#    90-100: A
#    80-89:  B
#    70-79:  C
#    60-69:  D
#    <60:    E
# 3. Display grade

# STARTER CODE:
nilai = int(input("Masukkan nilai (0-100): "))
# TODO: determine dan display grade

# BONUS: Add message untuk setiap grade
# A: "Excellent!"
# B: "Good job!"
# C: "Okay"
# D: "Need improvement"
# E: "Study harder"
```

---

### Exercise 2.2: Age Verification
**File:** `exercise_2_2.py`
**Time:** 15 min
**Concepts:** Comparisons, if/else

```python
# TODO:
# 1. Ask user untuk umur
# 2. Check:
#    - Jika < 13: "Kamu terlalu muda"
#    - Jika 13-17: "Remaja"
#    - Jika 18-64: "Dewasa"
#    - Jika >= 65: "Lansia"
# 3. Display hasil
```

---

### Exercise 2.3: Number Properties
**File:** `exercise_2_3.py`
**Time:** 20 min
**Concepts:** if, modulo operator, logical operators

```python
# TODO:
# 1. Ask user untuk angka
# 2. Check apakah:
#    - Positive atau negative atau zero?
#    - Even atau odd?
#    - Single digit atau double digit atau >2 digit?
# 3. Display all properties

# Example:
# Input: 42
# Output:
# 42 adalah positive
# 42 adalah even
# 42 adalah double digit
```

---

### Exercise 2.4: Simple Login
**File:** `exercise_2_4.py`
**Time:** 15 min
**Concepts:** String comparison, if/else, logical operators

```python
# TODO:
# 1. Store username dan password (hardcoded di code)
# 2. Ask user untuk username dan password
# 3. Check:
#    - Jika both correct: "Login berhasil!"
#    - Jika hanya username salah: "Username tidak cocok"
#    - Jika hanya password salah: "Password tidak cocok"
#    - Jika keduanya salah: "Username dan password tidak cocok"

# STARTER CODE:
correct_username = "admin"
correct_password = "12345"

username = input("Username: ")
password = input("Password: ")
# TODO: check dan display message
```

---

### Exercise 2.5: Quiz Program
**File:** `exercise_2_5.py`
**Time:** 25 min
**Concepts:** if/else, variables tracking

```python
# TODO:
# 1. Ask 3 simple questions (multiple choice)
# 2. Track score
# 3. Display score dan grade

# Example Questions:
# Q1: Ibukota Indonesia adalah?
#     a) Jakarta b) Bandung c) Surabaya
# Q2: 5 + 5 sama dengan?
#     a) 9 b) 10 c) 11
# Q3: Programming language populer adalah?
#     a) HTML b) Python c) CSS

# STARTER CODE:
score = 0

answer1 = input("Q1: Ibukota Indonesia? ")
if answer1 == "a":
    score += 1
# TODO: add remaining questions dan calculate final grade
```

---

## 🔁 WEEK 3: LOOPS

### Exercise 3.1: Multiplication Table
**File:** `exercise_3_1.py`
**Time:** 15 min
**Concepts:** for loop, range()

```python
# TODO:
# 1. Ask user untuk angka (1-10)
# 2. Display multiplication table untuk angka tersebut
# 3. Use for loop dengan range()

# Example (input: 5):
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ... until 5 x 10 = 50

# STARTER CODE:
angka = int(input("Angka (1-10): "))
for i in range(1, 11):
    # TODO: print multiplication
```

---

### Exercise 3.2: Sum of Numbers
**File:** `exercise_3_2.py`
**Time:** 15 min
**Concepts:** for loop, accumulator

```python
# TODO:
# 1. Ask user untuk batas atas (n)
# 2. Calculate sum dari 1 + 2 + 3 + ... + n
# 3. Display hasil

# Example (input: 5):
# 1 + 2 + 3 + 4 + 5 = 15

# STARTER CODE:
n = int(input("Batas atas: "))
total = 0
for i in range(1, n+1):
    # TODO: add to total
# TODO: display total
```

---

### Exercise 3.3: Pattern Printing
**File:** `exercise_3_3.py`
**Time:** 20 min
**Concepts:** nested loops

```python
# TODO:
# 1. Ask user untuk ukuran (n)
# 2. Print pyramid pattern

# Example (n=5):
# *
# * *
# * * *
# * * * *
# * * * * *

# STARTER CODE:
n = int(input("Ukuran: "))
for i in range(1, n+1):
    for j in range(i):
        # TODO: print star
    # TODO: new line
```

---

### Exercise 3.4: Number Guessing Game
**File:** `exercise_3_4.py`
**Time:** 25 min
**Concepts:** while loop, break, user input

```python
# TODO:
# 1. Store secret number (1-100)
# 2. Ask user untuk guess berulang kali
# 3. Give hint: "Too high" atau "Too low"
# 4. Loop sampai guess benar
# 5. Display berapa attempts yang dibutuhkan

# STARTER CODE:
secret = 42
attempts = 0

while True:
    guess = int(input("Guess angka (1-100): "))
    attempts += 1
    
    if guess == secret:
        # TODO: break loop dan display attempts
    elif guess < secret:
        print("Terlalu rendah")
    else:
        print("Terlalu tinggi")
```

---

### Exercise 3.5: Countdown Timer
**File:** `exercise_3_5.py`
**Time:** 20 min
**Concepts:** while loop, counter

```python
# TODO:
# 1. Ask user untuk starting number
# 2. Countdown dari number tersebut sampai 0
# 3. Print setiap number
# 4. Print "LIFTOFF!" pada akhir

# Example (input: 5):
# 5
# 4
# 3
# 2
# 1
# 0
# LIFTOFF!

# STARTER CODE:
start = int(input("Mulai dari: "))
while start >= 0:
    # TODO: print dan decrease counter
# TODO: print LIFTOFF!
```

---

## 📝 WEEK 4: FUNCTIONS & LISTS

### Exercise 4.1: Simple Function
**File:** `exercise_4_1.py`
**Time:** 15 min
**Concepts:** Function definition, parameters, return

```python
# TODO:
# 1. Create function greet(name) yang return "Hello [name]!"
# 2. Create function add(a, b) yang return sum
# 3. Create function multiply(a, b) yang return product
# 4. Test semua functions dengan input dari user

# STARTER CODE:
def greet(name):
    # TODO: return greeting
    pass

def add(a, b):
    # TODO: return sum
    pass

def multiply(a, b):
    # TODO: return product
    pass

# Test functions
name = input("Nama: ")
print(greet(name))

num1 = int(input("Angka 1: "))
num2 = int(input("Angka 2: "))
print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} * {num2} = {multiply(num1, num2)}")
```

---

### Exercise 4.2: List Operations
**File:** `exercise_4_2.py`
**Time:** 20 min
**Concepts:** Lists, append, remove, loops

```python
# TODO:
# 1. Create list kosong
# 2. Ask user untuk masukkan 5 numbers
# 3. Store dalam list
# 4. Display:
#    - All numbers
#    - Total
#    - Average
#    - Max
#    - Min

# STARTER CODE:
numbers = []
for i in range(5):
    num = int(input(f"Angka {i+1}: "))
    # TODO: append ke list

# TODO: Calculate dan display
```

---

### Exercise 4.3: To-Do List Manager
**File:** `exercise_4_3.py`
**Time:** 30 min
**Concepts:** Lists, loops, if/else, functions

```python
# TODO:
# 1. Create function add_task(tasks, task)
# 2. Create function view_tasks(tasks)
# 3. Create function delete_task(tasks, index)
# 4. Create menu loop yang allow user untuk:
#    - View all tasks
#    - Add task
#    - Delete task
#    - Exit

# STARTER CODE:
tasks = []

def view_tasks():
    # TODO: print all tasks
    pass

def add_task():
    # TODO: get task input, append ke list
    pass

def delete_task():
    # TODO: get index, remove dari list
    pass

while True:
    print("1. View")
    print("2. Add")
    print("3. Delete")
    print("4. Exit")
    choice = input("Choice: ")
    
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
```

---

## ✅ SUBMISSION GUIDE

### How to Submit Your Work:

1. **Create file** dengan nama yang sesuai (contoh: `exercise_1_1.py`)
2. **Code dengan baik:**
   - Add comments explaining logic
   - Use meaningful variable names
   - Format code dengan proper indentation

3. **Test your code:**
   - Run dan pastikan tidak ada error
   - Test dengan berbagai input

4. **Commit to Git:**
   ```bash
   git add exercise_1_1.py
   git commit -m "Exercise 1.1: Variable Practice"
   git push
   ```

5. **Track di checklist:**
   - Mark exercise sebagai done
   - Estimate waktu yang dibutuhkan
   - Note berapa kesulitan (1-5 stars)

---

## 🎯 DIFFICULTY LEVELS

```
⭐ EASY: Straightforward, minimal logic
⭐⭐ MEDIUM: Need some decision making
⭐⭐⭐ MEDIUM-HARD: Combine multiple concepts
⭐⭐⭐⭐ HARD: Complex logic flow
⭐⭐⭐⭐⭐ VERY HARD: Advanced thinking needed
```

---

## 💡 HINTS IF STUCK

### Exercise 1.1
- Gunakan input() untuk setiap variable
- Gunakan f-string untuk display: f"Halo {nama}"

### Exercise 2.4
- Comparison untuk string: username == correct_username
- Logical AND: if username == ... and password == ...

### Exercise 3.4
- Use while True untuk infinite loop
- Use break untuk exit loop
- Count attempts dengan variable counter

### Exercise 4.3
- Store tasks dalam list
- Use for loop dengan enumerate() untuk get index
- Menu-driven program: while True + if/elif/else

---

## 🔍 SELF-ASSESSMENT RUBRIC

Untuk setiap exercise, grade diri sendiri:

```
FUNCTIONALITY (Does it work?): ___/10
- Program runs tanpa error
- Logic bekerja dengan benar
- Output sesuai ekspektasi

CODE QUALITY (Is it good code?): ___/10
- Variable names meaningful
- Comments jelas
- Indentation proper
- DRY principle (Don't Repeat Yourself)

TESTING (Did you test thoroughly?): ___/5
- Test dengan multiple inputs
- Test edge cases
- No unexpected behavior

TOTAL: ___/25
```

---

## 📈 PROGRESS TRACKER

Update setiap selesai exercise:

```
WEEK 1:
[ ] 1.1: Variable Practice
[ ] 1.2: Calculator
[ ] 1.3: Temperature Converter
[ ] 1.4: Age Calculator
[ ] 1.5: Variables Game

WEEK 2:
[ ] 2.1: Grading System
[ ] 2.2: Age Verification
[ ] 2.3: Number Properties
[ ] 2.4: Simple Login
[ ] 2.5: Quiz Program

WEEK 3:
[ ] 3.1: Multiplication Table
[ ] 3.2: Sum of Numbers
[ ] 3.3: Pattern Printing
[ ] 3.4: Guessing Game
[ ] 3.5: Countdown Timer

WEEK 4:
[ ] 4.1: Simple Function
[ ] 4.2: List Operations
[ ] 4.3: To-Do List Manager

TOTAL COMPLETED: ___/18
```

---

## 🚀 NEXT LEVEL

Setelah complete exercises minggu 1-4:
- Move ke WEEK 5-6 exercises (OOP, File I/O)
- Start dengan full projects (todo_app, grade_manager)
- Begin LeetCode problems

---

**REMEMBER:** Difficulty naik progressively. Jangan khawatir jika stuck, itu NORMAL! 💪

Happy Coding! 🎉

