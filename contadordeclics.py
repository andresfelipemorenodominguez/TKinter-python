import tkinter as tk  # Importa el módulo tkinter para crear interfaces gráficas

ventana = tk.Tk()  # Crea la ventana principal de la aplicación
ventana.title("Contador de Clics")  # Establece el título de la ventana

contador = 0  # Inicializa la variable contador en 0

label_contador = tk.Label(ventana, text=f"Clics: {contador}", font=("Arial", 14))  # Crea una etiqueta para mostrar el número de clics
label_contador.pack(pady=10)  # Muestra la etiqueta y agrega un espacio vertical de 10 píxeles

def contar():  # Define la función que se ejecuta al hacer clic en el botón
    global contador  # Indica que se usará la variable global contador
    contador += 1  # Incrementa el contador en 1
    label_contador.config(text=f"Clics: {contador}")  # Actualiza el texto de la etiqueta con el nuevo valor

boton = tk.Button(ventana, text="Haz clic aquí", command=contar, font=("Arial", 12))  # Crea un botón que llama a la función contar al hacer clic
boton.pack(pady=10)  # Muestra el botón y agrega un espacio vertical de 10 píxeles

ventana.mainloop()  # Inicia el bucle principal de la aplicación para mostrar la ventana