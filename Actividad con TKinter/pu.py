import tkinter as tk

root = tk.Tk()
root.title("lista")
root.geometry("400x450")

lista=tk.Listbox(root, width=40, height=20)
lista.pack(pady=10, padx=10)

entrada=tk.Entry(root, width=20)
entrada.pack(pady=10, padx=10)

def agregar_productos():
    nuevo = entrada.get().strip()
    lista.insert(tk.END, nuevo)
    entrada.delete(0, tk.END)
boton2=tk.Button(root, text="Agregar Producto", command=agregar_productos)
boton2.pack(padx=10, pady=10)

root.mainloop()