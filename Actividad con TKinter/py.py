import tkinter as tk

root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Listbox directamente en la ventana (sin frame ni scrollbar)
lista_productos = tk.Listbox(root, width=45, height=15)
lista_productos.pack(side="left", fill="both", expand=True)

# Entrada para agregar nuevo producto desde la ventana
entrada_producto = tk.Entry(root, width=30)
entrada_producto.pack(padx=10, pady=(10, 0))

def AgregarProducto():  # Agrega el producto ingresado en el Entry al listado y al Listbox
    nuevo = entrada_producto.get().strip()   # Lee el texto del Entry y elimina espacios
    lista_productos.insert(tk.END, nuevo)    # Inserta el nuevo producto en el Listbox
    entrada_producto.delete(0, tk.END)       # Limpia el Entry después de agregar

boton2 = tk.Button(root, text="Agregar Producto", command=AgregarProducto)
boton2.pack(padx=10, pady=10)

root.mainloop()