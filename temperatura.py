import tkinter as tk

ventana = tk.Tk()  # Crea la ventana principal
ventana.title("Registro de Usuarios")  # Título de la ventana
ventana.geometry("300x400")  # Tamaño de la ventana

grados = tk.Label(ventana, text="Ingresa un valor:")
grados.pack(pady=5)
entrada_grados = tk.Entry(ventana)
entrada_grados.pack(pady=5)

def convertirafarenheit():
    valor = entrada_grados.get()           
    try:
        farenheit = float(valor) * 9 / 5 + 32
        print(farenheit)
    except ValueError:
        print("Ingresa un número válido")

botonf = tk.Button(ventana, text="Convertir a Farenheit", command=convertirafarenheit)
botonf.pack(pady=20)

def convertiracelsius():
    valor = entrada_grados.get()           
    try:
        celsius = (float(valor) - 32) * 5 / 9
        print(celsius)
    except ValueError:
        print("Ingresa un número válido")

botonc = tk.Button(ventana, text="Convertir a celsius", command=convertiracelsius)
botonc.pack(pady=20)
ventana.mainloop()