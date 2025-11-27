"""
SIMPLE TO-DO LIST APPLICATION
================================
Project pertama kamu untuk practice fundamental concepts:
- Variables & Lists
- Functions
- Loops & Conditionals
- File I/O (bonus)

Concepts yang digunakan:
✓ while loop (untuk menu)
✓ if-elif-else (untuk pilihan user)
✓ List operations (append, remove, display)
✓ Functions (untuk modularitas)
✓ User input handling

Instruksi:
1. Copy code ini ke file bernama 'todo_app.py'
2. Run dengan: python todo_app.py
3. Try semua fitur (add, view, delete, exit)
4. Modifikasi & tambahkan fitur sendiri
5. Push ke GitHub
"""

# ============================================
# VERSION 1: BASIC TO-DO LIST (untuk dipelajari)
# ============================================

def display_menu():
    """Menampilkan menu pilihan"""
    print("\n" + "="*40)
    print("     SIMPLE TO-DO LIST APP")
    print("="*40)
    print("1. View All Tasks")
    print("2. Add New Task")
    print("3. Delete Task")
    print("4. Exit")
    print("="*40)


def view_tasks(tasks):
    """Menampilkan semua task"""
    if len(tasks) == 0:
        print("\n📭 No tasks yet!")
        return
    
    print("\n📋 YOUR TASKS:")
    for i, task in enumerate(tasks, 1):
        print(f"  {i}. {task}")


def add_task(tasks):
    """Menambahkan task baru"""
    task = input("\n✏️  Enter new task: ")
    if task.strip() != "":  # Ensure tidak kosong
        tasks.append(task)
        print(f"✅ Task '{task}' added successfully!")
    else:
        print("❌ Task cannot be empty!")


def delete_task(tasks):
    """Menghapus task"""
    if len(tasks) == 0:
        print("\n❌ No tasks to delete!")
        return
    
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"✅ Task '{removed}' deleted!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")


def main():
    """Main program logic"""
    tasks = []  # List untuk store semua tasks
    
    # Main loop - terus jalan sampai user pilih exit
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("\n👋 Goodbye! See you next time!")
            break  # Exit dari while loop
        else:
            print("❌ Invalid choice! Please enter 1-4")


# Entry point of program
if __name__ == "__main__":
    main()


# ============================================
# EXTENSION IDEAS (untuk setelah paham basics)
# ============================================
# 1. Mark task as complete (menggunakan tuple/dict)
# 2. Save tasks ke file (file I/O)
# 3. Load tasks dari file saat startup
# 4. Priority levels untuk setiap task
# 5. Due dates untuk setiap task
# 6. Search/filter tasks
# 7. Edit existing task
# 8. Undo last action
#
# Setelah bisa implement di atas, Anda sudah siap
# untuk belajar OOP dan membuat Task sebagai class!

