import tkinter
from tkinter import *
from tkinter import ttk, messagebox

root = tkinter.Tk()
root.title("Interés compuesto y amortización francesa")
root.configure(bg = "#7cb0ff")

root.geometry("1000x1000")
root.resizable(0,0)

tasa_mensual = DoubleVar()
tipo_prestamo = StringVar()
tipo_prestamo.set("No seleccionado")
DTI_message = StringVar()
DTI_message.set(" ")
origen_credito = StringVar(value="banco")

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

Label(root, text="Origen del crédito:", bg="#7cb0ff", font=('Verdana', 10)).pack()
combo_origen = ttk.Combobox(root, values=["banco", "seguro"], state="readonly", textvariable=origen_credito, width=10)
combo_origen.pack(pady=5)

def actualizar_tipo(event):
    tipo = combo_prestamos.get()
    tasa = tipos_de_prestamo[tipo]
    tasa_mensual.set(tasa/12)
    tipo_prestamo.set(f"{tipo} ({tasa*100:.2f}% mensual)")

combo_prestamos.bind("<<ComboboxSelected>>", actualizar_tipo)

def calcular_DTI():
    DTI = (float(entry_gastos_mensuales.get()) / float(entry_ingreso_mensual.get())) * 100

from tkinter import messagebox

def calcularDTI_con_mensaje():
    try:
        gastos = float(entry_gastos_mensuales.get())
        ingresos = float(entry_ingreso_mensual.get())

        if ingresos == 0:
            messagebox.showerror("Error", "Los ingresos mensuales no pueden ser 0.")
            return

        DTI = (gastos / ingresos) * 100
        DTI_redondeado = round(DTI, 2)

        if DTI < 20:
            mensaje = "Tienes un BAJO riesgo financiero, puedes aplicar a un préstamo sin problema."
        elif DTI < 36:
            mensaje = "Tienes un MEDIO riesgo financiero, puedes aplicar a un préstamo moderado."
        elif DTI <= 43:
            mensaje = "Tienes un ALTO riesgo financiero, calificas para préstamos pequeños."
        else:
            mensaje = "Tienes un CRÍTICO riesgo financiero, no puedes aplicar a un préstamo con facilidad."

        mensaje += f"\nDTI (Debt-to-Income Ratio): {DTI_redondeado}%"
        messagebox.showinfo("Evaluación Financiera", mensaje)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos en ingresos y gastos.")


def calcular_amortizacion_francesa():
    try:
        monto = float(entry_monto_prestamo.get())
        plazo_anios = int(entry_plazo_pago.get())
        tasa = tasa_mensual.get()
        origen = origen_credito.get()

        if tasa == 0:
            raise ValueError("Debe seleccionar un tipo de préstamo")

        n = plazo_anios * 12
        i = tasa
        cuota = monto * (i * (1 + i)**n) / ((1 + i)**n - 1)

        for item in tabla.get_children():
            tabla.delete(item)

        capital_restante = monto
        intereses_acumulados = 0
        capital_amort_acumulado = 0
        
        for mes in range(1, n + 1):
            interes_mes = capital_restante * i
            amortizacion = cuota - interes_mes
            capital_restante -= amortizacion
            intereses_acumulados += interes_mes
            capital_amort_acumulado += amortizacion

            seguro = round(capital_restante * 0.006, 2) if origen == "seguro" else 0.0

            tabla.insert("", "end", values=(
                mes,
                f"{cuota:.2f}",
                f"{interes_mes:.2f}",
                f"{amortizacion:.2f}",
                f"{max(capital_restante, 0):.2f}",
                f"{intereses_acumulados:.2f}",
                f"{seguro:.2f}",
                f"{capital_amort_acumulado:.2f}"
            ))

    except Exception as e:
        messagebox.showerror("Error", f"Error en los datos: {e}")

    calcularDTI_con_mensaje()    

columnas = ("Mes", "Cuota", "Interés", "Amortización", "Capital restante", "Intereses acumulados", "Seguro", "Cap. amort. acumulado")
tabla = ttk.Treeview(root, columns=columnas, show="headings", height=20)
tabla.pack(pady=10)

for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, anchor="center", width=120)

boton_calcular = Button(root, text="Calcular amortización", command=calcular_amortizacion_francesa)
boton_calcular.pack(pady=10)

root.mainloop()