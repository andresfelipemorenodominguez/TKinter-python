import tkinter as tk  # Importa el módulo tkinter para crear interfaces gráficas

ventana = tk.Tk()  # Crea la ventana principal
ventana.title("Conversor de Temperatura")  # Establece el título de la ventana
ventana.geometry("300x400")  # Define el tamaño de la ventana (ancho x alto)

grados = tk.Label(ventana, text="Ingresa un valor:")  # Crea una etiqueta para pedir el valor al usuario
grados.pack(pady=5)  # Muestra la etiqueta y agrega un espacio vertical de 5 píxeles
entrada_grados = tk.Entry(ventana)  # Crea un campo de entrada para que el usuario escriba el valor
entrada_grados.pack(pady=5)  # Muestra el campo de entrada y agrega un espacio vertical de 5 píxeles

def convertirafarenheit():  # Define la función para convertir de Celsius a Fahrenheit
    valor = entrada_grados.get()  # Obtiene el valor ingresado por el usuario
    try:
        farenheit = float(valor) * 9 / 5 + 32  # Realiza la conversión a Fahrenheit
        print(farenheit)  # Imprime el resultado en consola
    except ValueError:
        print("Ingresa un número válido")  # Muestra un mensaje si el valor no es numérico

botonf = tk.Button(ventana, text="Convertir a Farenheit", command=convertirafarenheit)  # Crea el botón para convertir a Fahrenheit
botonf.pack(pady=20)  # Muestra el botón y agrega un espacio vertical de 20 píxeles

def convertiracelsius():  # Define la función para convertir de Fahrenheit a Celsius
    valor = entrada_grados.get()  # Obtiene el valor ingresado por el usuario
    try:
        celsius = (float(valor) - 32) * 5 / 9  # Realiza la conversión a Celsius
        print(celsius)  # Imprime el resultado en consola
    except ValueError:
        print("Ingresa un número válido")  # Muestra un mensaje si el valor no es numérico

botonc = tk.Button(ventana, text="Convertir a celsius", command=convertiracelsius)  # Crea el botón para convertir a Celsius
botonc.pack(pady=20)  # Muestra el botón y agrega un espacio vertical de 20 píxeles

ventana.mainloop()  # Inicia el bucle principal de la aplicación para mostrar la ventana