
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