import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# Пути к программам и папкам
PROGRAMS = {
    "Everything": r"C:\myapp\Everything.exe",
    "LastActivityView": r"C:\myapp\LastActivityView.exe",
    "ShellBag Analyzer": r"C:\myapp\shellbag_analyzer_cleaner.exe",
    "Process Hacker": r"C:\myapp\ProcessHacker.exe",
}

FOLDERS = {
    "AppData": os.path.expandvars(r"%APPDATA%"),
    "Prefetch": r"C:\Windows\Prefetch",
    "Recycle Bin": r"C:\$Recycle.Bin",
}

def open_program(name):
    """Запускает программу, если файл существует."""
    path = PROGRAMS.get(name)
    if path and os.path.exists(path):
        subprocess.Popen(path, shell=True)
    else:
        messagebox.showerror("Ошибка", f"{name} не найдено!")

def open_folder(name):
    """Открывает папку, если она существует."""
    path = FOLDERS.get(name)
    if path and os.path.exists(path):
        subprocess.Popen(f'explorer "{path}"', shell=True)
    else:
        messagebox.showerror("Ошибка", f"{name} не найдено!")

def create_gui():
    """Создает графический интерфейс."""
    root = tk.Tk()
    root.title("Выбор запуска")
    root.geometry("300x350")  # Размер окна

    # Создание кнопок для программ
    tk.Label(root, text="Запуск программ:", font=("Arial", 12, "bold")).pack(pady=5)
    for name in PROGRAMS:
        tk.Button(root, text=name, command=lambda n=name: open_program(n), width=30).pack(pady=2)

    # Создание кнопок для папок
    tk.Label(root, text="Открытие папок:", font=("Arial", 12, "bold")).pack(pady=5)
    for name in FOLDERS:
        tk.Button(root, text=name, command=lambda n=name: open_folder(n), width=30).pack(pady=2)

    # Кнопка выхода
    tk.Button(root, text="Выход", command=root.quit, width=30, bg="red", fg="white").pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()