import tkinter
from tkinter import *

root = tkinter.Tk()
root.title("Interés compuesto y amortización francesa")
root.configure(bg = "#7cb0ff")

root.geometry("600x400")
root.resizable(0,0)

TITLE=Label(root,text="SIMULACIÓN DE PRÉSTAMO BANCARIO",bg="#7cb0ff",font=('Arial black',15))
TITLE.pack(pady=25)

tkinter.Label(root, text="Ingreso mensual:",bg="#7cb0ff",font=('Verdana',10)).pack()
entry_ingreso_mensual = tkinter.Entry(root)
entry_ingreso_mensual.pack(pady=10)

tkinter.Label(root, text="Gastos mensuales:",bg="#7cb0ff",font=('Verdana',10)).pack()
entry_gastos_mensuales = tkinter.Entry(root)
entry_gastos_mensuales.pack(pady=10)

tkinter.Label(root, text="Monto solicitado del préstamo:",bg="#7cb0ff",font=('Verdana',10)).pack()
entry_monto_prestamo = tkinter.Entry(root)
entry_monto_prestamo.pack(pady=10)

tkinter.Label(root, text="Plazo de pago (en años):",bg="#7cb0ff",font=('Verdana',10)).pack()
entry_plazo_pago = tkinter.Entry(root)
entry_plazo_pago.pack(pady=10)

root.mainloop()