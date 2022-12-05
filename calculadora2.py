import tkinter 


ventana = tkinter.Tk()
ventana.title("Calculadora")
ventana.geometry("+480+180")
ventana.iconbitmap(r"C:\Users\Admin\Desktop\recursos\icono.ico")

def Sumar():
    try:
        valor1 = e_valor1.get()
        valor2 = e_valor2.get()
        label_resultado.grid(row= 7, column=0, columnspan=2) 

        if valor1 == "" or valor2 == "":
          label_resultado["text"] ="¡Faltan valores para sumar¡"
          messagebox.showwarmimg("Error", "Faltan errores para sumar")
        else:
         resultado = int(valor1) + int(valor2)
         label_resultado["text"] = resultado
    except:
         messagebox.showerror("Error", "Error, valores no válidos")

def Resta():
    try:
        valor1 = e_valor1.get()
        valor2 = e_valor2.get()
        label_resultado.grid(row= 7, column=0, columnspan=2) 

        if valor1 == "" or valor2 == "":
          label_resultado["text"] ="¡Faltan valores para restar¡"
          messagebox.showwarmimg("Error", "Faltan errores para restar")
        else:
         resultado = int(valor1) - int(valor2)
         label_resultado["text"] = resultado
    except:
         messagebox.showerror("Error", "Error, valores no válidos")

def Multiplica():
    try:
        valor1 = e_valor1.get()
        valor2 = e_valor2.get()
        label_resultado.grid(row= 7, column=0, columnspan=2) 

        if valor1 == "" or valor2 == "":
          label_resultado["text"] ="¡Faltan valores para multiplicar¡"
          messagebox.showwarmimg("Error", "Faltan errores para multiplicar")
        else:
         resultado = int(valor1) * int(valor2)
         label_resultado["text"] = resultado
    except:
         messagebox.showerror("Error", "Error, valores no válidos")

def Divide():
    try:
        valor1 = e_valor1.get()
        valor2 = e_valor2.get()
        label_resultado.grid(row= 7, column=0, columnspan=2) 

        if valor1 == "" or valor2 == "":
          label_resultado["text"] ="¡Faltan valores para dividir¡"
          messagebox.showwarmimg("Error", "Faltan errores para dividir")
        else:
         resultado = int(valor1) / int(valor2)
         label_resultado["text"] = resultado
    except:
         messagebox.showerror("Error", "Error, valores no válidos")

def Potenciar():
    try:
        valor1 = e_valor1.get()
        valor2 = e_valor2.get()
        label_resultado.grid(row= 7, column=0, columnspan=2) 

        if valor1 == "" or valor2 == "":
          label_resultado["text"] ="¡Faltan valores para potenciar¡"
          messagebox.showwarmimg("Error", "Faltan errores para potenciar")
        else:
         resultado = int(valor1) ** int(valor2)
         label_resultado["text"] = resultado
    except:
         messagebox.showerror("Error", "Error, valores no válidos")

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)
ventana.columnconfigure(3, weight=1)
ventana.columnconfigure(4, weight=1)
ventana.columnconfigure(5, weight=1)
ventana.columnconfigure(6, weight=1)

label_titulo = tkinter.Label(ventana, text="calculadora", font="arial 25")

label_valor1 = tkinter.Label(ventana, text="Valor 1", font="arial 12")
label_valor2 = tkinter.Label(ventana, text="Valor 2", font="arial 12")

e_valor1 = tkinter.Entry(ventana, font="arial 15")
e_valor2 = tkinter.Entry(ventana, font="arial 15")

button_suma = tkinter.Button(ventana, text="Suma", bg="orange", fg="black", font="arial 12", width=10, command=lambda: Sumar())
button_resta = tkinter.Button(ventana, text="Resta", bg="orange", fg="black", font="arial 12", width=10, command=Resta)
button_mul = tkinter.Button(ventana, text="Multiplica", bg="orange", fg="black", font="arial 12", width=10, command=Multiplica)
button_div = tkinter.Button(ventana, text="Divide", bg="orange", fg="black", font="arial 12", width=10, command=Divide)
button_potencia = tkinter.Button(ventana, text="potencia", bg="orange", fg="black", font="arial 12", width=10, command=Potenciar)

label_titulo.grid(row=0, column=0, columnspan=2, pady=8)

label_valor1.grid(row=1, column=0, pady=8)
label_valor2.grid(row=2, column=0, pady=8)

e_valor1.grid(row=1, column=1)
e_valor2.grid(row=2, column=1)

button_suma.grid(row=3, column=0, pady=8, columnspan=2)
button_resta.grid(row=4, column=0, pady=8, columnspan=2)
button_mul.grid(row=5, column=0, pady=8, columnspan=2)
button_div.grid(row=6, column=0, pady=8, columnspan=2)
button_potencia.grid(row=7, column=0, pady=8, columnspan=2)

label_resultado = tkinter.Label(ventana)

ventana.mainloop()