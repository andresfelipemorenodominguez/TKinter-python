import tkinter as tk  # Importa el módulo tkinter para crear interfaces gráficas

ventana = tk.Tk()  # Crea la ventana principal de la aplicación
ventana.title("Registro de Usuarios")  # Establece el título de la ventana
ventana.geometry("300x400")  # Define el tamaño de la ventana (ancho x alto)

nombre = tk.Label(ventana, text="Nombre:")  # Crea una etiqueta que dice "Nombre:"
nombre.pack(pady=10)  # Muestra la etiqueta y agrega un espacio vertical de 10 píxeles
entrada_nombre = tk.Entry(ventana)  # Crea un campo de entrada para el nombre
entrada_nombre.pack(pady=5)  # Muestra el campo de entrada y agrega un espacio vertical de 5 píxeles

edad = tk.Label(ventana, text="Edad:")  # Crea una etiqueta que dice "Edad:"
edad.pack(pady=10)  # Muestra la etiqueta y agrega un espacio vertical de 10 píxeles
entrada_edad = tk.Entry(ventana)  # Crea un campo de entrada para la edad
entrada_edad.pack(pady=5)  # Muestra el campo de entrada y agrega un espacio vertical de 5 píxeles

correo = tk.Label(ventana, text="Correo Electrónico:")  # Crea una etiqueta que dice "Correo Electrónico:"
correo.pack(pady=10)  # Muestra la etiqueta y agrega un espacio vertical de 10 píxeles
entrada_entrada = tk.Entry(ventana)  # Crea un campo de entrada para el correo electrónico
entrada_entrada.pack(pady=5)  # Muestra el campo de entrada y agrega un espacio vertical de 5 píxeles

def MostrarDatos():  # Define una función para mostrar los datos ingresados
    print("Nombre:", entrada_nombre.get())  # Imprime el nombre ingresado en consola
    print("Edad:", entrada_edad.get())  # Imprime la edad ingresada en consola
    print("Nombre:", entrada_entrada.get())  # Imprime el correo ingresado en consola (debería decir "Correo:")

boton = tk.Button(ventana, text="Guardar", command=MostrarDatos)  # Crea un botón que ejecuta MostrarDatos al hacer clic
boton.pack(pady=20)  # Muestra el botón y agrega un espacio vertical de 20 píxeles

ventana.mainloop()  # Inicia el bucle principal de la aplicación para mostrar la ventana