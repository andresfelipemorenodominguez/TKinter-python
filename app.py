import tkinter as tk

def click_boton(nuumero):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + str(nuumero))

def borrar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")