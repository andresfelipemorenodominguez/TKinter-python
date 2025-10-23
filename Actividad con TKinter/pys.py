import tkinter as tk 

root = tk.Tk()
root.title("Calculadora")
root.geometry("400x450")

decoracion= tk.Label(root, text="Decoracion: ")
decoracion.pack(pady=10)

decoracion_entry= tk.Entry(root)
decoracion_entry.pack(pady=10)

comida= tk.Label(root, text="comida: ")
comida.pack(pady=10)

comida_entry= tk.Entry(root)
comida_entry.pack(pady=10)

musica= tk.Label(root, text="musica: ")
musica.pack(pady=10)

musica_entry= tk.Entry(root)
musica_entry.pack(pady=10)

transporte= tk.Label(root, text="transporte: ")
transporte.pack(pady=10)

transporte_entry= tk.Entry(root)
transporte_entry.pack(pady=10)

def calcular_total():
        d = float(decoracion_entry.get())
        c = float(comida_entry.get())
        m = float(musica_entry.get())
        t = float(transporte_entry.get())
        total = d + c + m + t
        totals.config(text=f"Total: {total} ")

totals= tk.Label(root, text="Total: ")
totals.pack(pady=20)
botn= tk.Button(root, text="Calcular Total", command=calcular_total)
botn.pack(pady=20)

root.mainloop()