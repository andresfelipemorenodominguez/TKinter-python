import tkinter as tk

root = tk.Tk()
root.title("Calculadora")
root.geometry("400x450")

label_decoracion = tk.Label(root, text="Decoracion: ", font=("Helvetica", 16))
label_decoracion.pack(pady=10)

entry_decoracion = tk.Entry(root, font=("Helvetica", 14))
entry_decoracion.pack(pady=10)

label_comida = tk.Label(root, text="Comida: ", font=("Helvetica", 16))
label_comida.pack(pady=10)

entry_comida = tk.Entry(root, font=("Helvetica", 14))
entry_comida.pack(pady=10)

label_musica = tk.Label(root, text="Musica: ", font=("Helvetica", 16))
label_musica.pack(pady=10)

entry_musica = tk.Entry(root, font=("Helvetica", 14))
entry_musica.pack(pady=10)

label_transporte = tk.Label(root, text="Transporte: ", font=("Helvetica", 16))
label_transporte.pack(pady=10)

entry_transporte = tk.Entry(root, font=("Helvetica", 14))
entry_transporte.pack(pady=10)

def calcular_total():
        decoracion = float(entry_decoracion.get() or 0)
        Musica = float(entry_musica.get() or 0)
        comida = float(entry_comida.get() or 0)
        transporte = float(entry_transporte.get() or 0)
        total = decoracion + Musica + comida + transporte
        label_result.config(text=f"Total: {total:.2f} €")

# Label para mostrar el resultado en la misma ventana
label_result = tk.Label(root, text="Total: 0.00 €", font=("Helvetica", 16), fg="blue")
label_result.pack(pady=10)

boton_calcular = tk.Button(root, text="Calcular Total", font=("Helvetica", 16), command=calcular_total)
boton_calcular.pack(pady=20)



root.mainloop()