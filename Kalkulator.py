import tkinter as tk
import math

def tekan(tombol):
    current = layar_var.get()
    
    if tombol == "C":
        layar_var.set("")
    elif tombol == "=":
        try:
            ekspresi = layar_var.get()
            ekspresi = ekspresi.replace('^', '**')
            ekspresi = ekspresi.replace('√', 'math.sqrt')
            ekspresi = ekspresi.replace('%', '/100')

            open_paren = ekspresi.count('(')
            close_paren = ekspresi.count(')')

            if open_paren > close_paren:
                ekspresi += ')' * (open_paren - close_paren)
            hasil = eval(ekspresi)
            layar_var.set(hasil)
        except Exception as e:
            layar_var.set("Error")
    elif tombol == "√":
        layar_var.set(current + '√(')
    else:
        layar_var.set(current + str(tombol))

root = tk.Tk()
root.title("Kalkulator Sederhana dengan Tkinter")

layar_var = tk.StringVar()

layar = tk.Entry(root, textvariable=layar_var, font=('Arial', 20), bd=10, insertwidth=4, width=25, borderwidth=4, justify='right')
layar.grid(row=0, column=0, columnspan=5)

tombol_list = [
    '7', '8', '9', '/', '√',
    '4', '5', '6', '*', '^',
    '1', '2', '3', '-', '%',
    'C', '0', '=', '+', '.'
]

baris = 1
kolom = 0
for tombol in tombol_list:
    tk.Button(root, text=tombol, padx=20, pady=20, font=('Arial', 18),
              command=lambda t=tombol: tekan(t)).grid(row=baris, column=kolom)
    kolom += 1
    if kolom > 4:
        kolom = 0
        baris += 1

for i in range(5):
    root.grid_columnconfigure(i, weight=1)
for i in range(baris + 1):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()

