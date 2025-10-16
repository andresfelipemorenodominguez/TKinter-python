import tkinter as tk  # Importa la librería tkinter para interfaces gráficas
from tkinter import messagebox  # Importa messagebox para mostrar mensajes emergentes

# Crea la ventana principal de la aplicación
root = tk.Tk()
root.title("Lista de Tareas")  # Establece el título de la ventana

# Crea una etiqueta que indica al usuario que escriba una tarea
tk.Label(root, text="Escribe una tarea:").grid(row=0, column=0, padx=10, pady=5)

# Crea un campo de entrada de texto para que el usuario escriba la tarea
entrada = tk.Entry(root, width=30)
entrada.grid(row=0, column=1, padx=10, pady=5)

# Crea un Listbox para mostrar la lista de tareas agregadas
lista = tk.Listbox(root, width=45, height=10)
lista.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Función para añadir una nueva tarea a la lista
def añadir_tarea():
    texto = entrada.get().strip()  # Obtiene el texto ingresado y elimina espacios

    if texto:  # Si el campo no está vacío
        lista.insert(tk.END, texto)  # Inserta la tarea al final de la lista
        entrada.delete(0, tk.END)  # Limpia el campo de entrada
    else:  # Si el campo está vacío
        messagebox.showwarning("Atención", "Escribe una tarea antes de agregar")  # Muestra advertencia

# Función para borrar la tarea seleccionada de la lista
def borrar_tarea():
    indice = lista.curselection()  # Obtiene el índice de la tarea seleccionada

    if indice:  # Si hay una tarea seleccionada
        lista.delete(indice)  # Elimina la tarea seleccionada
    else:  # Si no hay ninguna tarea seleccionada
        messagebox.showinfo("Aviso", "Selecciona una tarea para eliminar")  # Muestra aviso

# Crea el botón para añadir tareas y lo coloca en la ventana
tk.Button(root, text="Añadir", command=añadir_tarea).grid(row=2, column=0, pady=10)
# Crea el botón para borrar tareas y lo coloca en la ventana
tk.Button(root, text="Borrar", command=borrar_tarea).grid(row=2, column=1, pady=10)

# Inicia el bucle principal de la aplicación para mostrar la ventana
root.mainloop()