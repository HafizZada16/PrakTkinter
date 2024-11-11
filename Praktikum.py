import tkinter as tk
from tkinter import messagebox

def hasil_prediksi():
    try:
        # Memproses nilai dari input
        for entry in entries:
            value = entry.get()
            if not value.isdigit():
                raise ValueError("Nilai harus berupa angka")
            # Proses nilai langsung di sini jika diperlukan
            int_value = int(value)
            # Proses nilai int_value jika diperlukan
        
        # Logika prediksi
        prodi = "Teknologi Informasi"  # Hasil prediksi tetap
        hasil_label.config(text=f"Hasil Produksi: {prodi}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x550")
root.configure(bg="#DFF2EB")  # Configurasi tambahan

# Label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Brush Script MT", 20), bg="#DFF2EB")
judul_label.pack(pady=20)

# Frame untuk input nilai
input_frame = tk.Frame(root, bg="#DFF2EB")
input_frame.pack(pady=10)

# Membuat 10 input nilai mata pelajaran dengan label
entries = []
for i in range(10):
    label = tk.Label(input_frame, text=f"Nilai Mata Pelajaran {i+1}:", bg="#DFF2EB", font=("Comic Sans MS", 9))
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(input_frame)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Tombol untuk hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, bg="#B9E5E8")
prediksi_button.pack(pady=10)

# Label untuk menampilkan hasil produksi
hasil_label = tk.Label(root, text="Hasil Prediksi: ", font=("Comic Sans MS", 12, "bold"), bg="#DFF2EB", fg="#4A628A")
hasil_label.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()