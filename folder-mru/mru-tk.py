import tkinter as tk

def function_click():
    velocidad = float(entry_velocidad.get())
    tiempo = float(entry_tiempo.get())
    distancia = velocidad*tiempo
    labelresult.configure(text=f"resultado: {distancia}")

root = tk.Tk() 
root.title("Python-TKinter")
root.resizable(0, 0)
root.minsize( 1000, 700)
# elements
# label
labelresult=tk.Label(root, text="RESULTADO:")
final = tk.Label(root, text="DISTANCIA RECORRIDA")
primero = tk.Label(root, text="VELOCIDAD:")
segundo = tk.Label(root, text="TIEMPO:")
# agregar una caja de texto
partidos_ganados = tk.StringVar()

# textbox
text_velocidad = tk.StringVar()
text_tiempo = tk.StringVar()

# entry
entry_velocidad = tk.Entry(root,width=20,textvariable=text_velocidad)
entry_tiempo = tk.Entry(root,width=20,textvariable=text_tiempo)

# boton
button=tk.Button(root,text="calcular",command=function_click)

# position
final.grid(column=6, row=2)
primero.grid(column=1, row=2)
segundo.grid(column=3, row=2)
entry_velocidad.grid(column=2, row=2)
entry_tiempo.grid(column=4, row=2)
labelresult.grid(column=0, row=0)
button.grid(column=0, row=1)


root.mainloop()
