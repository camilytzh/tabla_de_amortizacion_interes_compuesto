import tkinter
from tkinter import *
from tkinter import ttk, messagebox

root = tkinter.Tk()
root.title("Interés compuesto y amortización francesa")
root.configure(bg = "#7cb0ff")

root.geometry("600x400")
root.resizable(0,0)

tasa_mensual = DoubleVar()
tipo_prestamo = StringVar()
tipo_prestamo.set("No seleccionado")

tipos_de_prestamo = {
    "Productivo Corporativo": 0.0850,
    "Productivo Empresarial": 0.1055,
    "Productivo PYMES": 0.1062,
    "Consumo": 0.1598,
    "Educativo": 0.0891,
    "Educativo Social": 0.0549,
    "Vivienda de Interés Público": 0.0499,
    "Vivienda de Interés Social": 0.0498,
    "Inmobiliario": 0.1036,
    "Microcrédito Minorista": 0.2088,
    "Microcrédito de Acumulación Simple": 0.2124,
    "Microcrédito de Acumulación Ampliada": 0.1875,
    "Inversión Pública": 0.0883
}

TITLE=Label(root,text="SIMULACIÓN DE PRÉSTAMO BANCARIO",bg="#7cb0ff",font=('Arial black',15))
TITLE.pack(pady=25)

tkinter.Label(root, text="Ingreso mensual:",bg="#7cb0ff",font=('Verdana',10)).pack()
entry_ingreso_mensual = tkinter.Entry(root)
entry_ingreso_mensual.pack(pady=5)

tkinter.Label(root, text="Gastos mensuales:",bg="#7cb0ff",font=('Verdana',10)).pack()
entry_gastos_mensuales = tkinter.Entry(root)
entry_gastos_mensuales.pack(pady=5)

tkinter.Label(root, text="Monto solicitado del préstamo:",bg="#7cb0ff",font=('Verdana',10)).pack()
entry_monto_prestamo = tkinter.Entry(root)
entry_monto_prestamo.pack(pady=5)

tkinter.Label(root, text="Plazo de pago (en años):",bg="#7cb0ff",font=('Verdana',10)).pack()
entry_plazo_pago = tkinter.Entry(root)
entry_plazo_pago.pack(pady=5)

Label(root, text="Seleccione el tipo de préstamo:", bg="#7cb0ff", font=('Verdana', 10)).pack(pady=(5, 5))

combo_prestamos = ttk.Combobox(root, values=list(tipos_de_prestamo.keys()), state="readonly", width=20)
combo_prestamos.pack()

label_seleccion = Label(root, textvariable=tipo_prestamo, bg="#7cb0ff", font=('Verdana', 10, 'italic'))
label_seleccion.pack(pady=5)

def actualizar_tipo(event):
    tipo = combo_prestamos.get()
    tasa = tipos_de_prestamo[tipo]
    tasa_mensual.set(tasa)
    tipo_prestamo.set(f"{tipo} ({tasa*100:.2f}% mensual)")

combo_prestamos.bind("<<ComboboxSelected>>", actualizar_tipo)

root.mainloop()

DTI = 0

def calcularDTI(gastos_mensuales, ingresos_mensuales):
    DTI = (float(gastos_mensuales) / float(ingresos_mensuales)) * 100
    if DTI >= 0 or DTI <= 35:
        print("Tienes un BAJO riesgo financiero, puedes aplicar a un préstamo sin problema!")
    elif DTI >= 36 or DTI <= 43:
        print("Tienes un MEDIO riesgo financiero, puedes aplicar a un préstamo moderado.")
    elif DTI >= 44 or DTI <= 50:
        print("Tienes un ALTO riesgo financiero, calificas para préstamos pequeños.")
    else:
        print("Tienes un CRITICO riesgo financiero, no puedes aplicar a un préstamo con facilidad.")    
    print("DTI(Debt-to-Income Ratio): " + DTI + "%")