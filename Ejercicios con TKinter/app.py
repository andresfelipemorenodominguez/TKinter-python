
# Importa el módulo tkinter y lo renombra como tk
import tkinter as tk


# Función que se ejecuta al presionar un botón numérico
def click_boton(nuumero):                       
    actual = entrada.get()  # Obtiene el valor actual de la entrada
    entrada.delete(0, tk.END)  # Borra el contenido actual
    entrada.insert(0, actual + str(nuumero))  # Inserta el nuevo número al final


# Función para borrar el contenido de la entrada
def borrar():
    entrada.delete(0, tk.END)


# Función para calcular el resultado de la expresión ingresada
def calcular():
    try:
        resultado = eval(entrada.get())  # Evalúa la expresión matemática
        entrada.delete(0, tk.END)  # Borra la entrada
        entrada.insert(0, str(resultado))  # Muestra el resultado
    except:
        entrada.delete(0, tk.END)  # Borra la entrada en caso de error
        entrada.insert(0, "Error")  # Muestra mensaje de error

ventana = tk.Tk()  # Crea la ventana principal
ventana.title("Calculadora")  # Título de la ventana
ventana.geometry("300x400")  # Tamaño de la ventana

entrada = tk.Entry(ventana, width=20, font=("Arial", 18),justify="right")  # Campo de entrada para la calculadora
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Posiciona la entrada en la cuadrícula  

botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
] # Lista de botones con sus posiciones

# Crear los botones en la ventana
for (texto, fila, columna) in botones:
    if texto == 'C':
        accion = borrar
    else:
        accion = lambda x=texto: click_boton(x)
    tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 16), command=accion).grid(row=fila, column=columna, padx=5, pady=5)

# Botón de igual (=)
tk.Button(ventana, text='=', width=22, height=2, font=("Arial", 16), command=calcular).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

ventana.mainloop()
