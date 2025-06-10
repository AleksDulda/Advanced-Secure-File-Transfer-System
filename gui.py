import tkinter as tk
from tkinter import filedialog, messagebox
import os
import threading
import time
import client

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def send_file_thread():
    file_path = file_entry.get()
    if not os.path.exists(file_path):
        messagebox.showerror("Hata", "Dosya bulunamadı!")
        return
    try:
        time.sleep(0.5)  # Sunucu tam başlasın
        client.send_file(file_path)
        messagebox.showinfo("Başarılı", "Dosya başarıyla gönderildi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Dosya gönderilemedi:\n{str(e)}")

def send_file():
    threading.Thread(target=send_file_thread).start()

root = tk.Tk()
root.title("Secure File Transfer")

tk.Label(root, text="Gönderilecek Dosya:").pack(pady=5)
file_entry = tk.Entry(root, width=50)
file_entry.pack(pady=5)

tk.Button(root, text="Gözat", command=browse_file).pack(pady=5)
tk.Button(root, text="Gönder", command=send_file).pack(pady=10)

root.mainloop()
