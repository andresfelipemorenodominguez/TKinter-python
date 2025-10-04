import tkinter as tk

ventana = tk.Tk()  # Crea la ventana principal
ventana.title("Registro de Usuarios")  # Título de la ventana
ventana.geometry("300x400")  # Tamaño de la ventana

nombre = tk.Label(ventana, text="Nombre:")
nombre.pack(pady=10)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=5)

edad = tk.Label(ventana, text="Edad:")
edad.pack(pady=10)
entrada_edad = tk.Entry(ventana)
entrada_edad.pack(pady=5)

correo = tk.Label(ventana, text="Correo Electrónico:")
correo.pack(pady=10)
entrada_entrada = tk.Entry(ventana)
entrada_entrada.pack(pady=5)

def MostrarDatos():
    print("Nombre:", entrada_nombre.get())
    print("Edad:", entrada_edad.get())
    print("Nombre:", entrada_entrada.get())

boton = tk.Button(ventana, text="Guardar", command=MostrarDatos)
boton.pack(pady=20)
ventana.mainloop()