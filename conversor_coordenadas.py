import tkinter as tk
from tkinter import ttk

# Función: DD a DMS
def dd_a_dms():
    try:
        dd = float(entry_dd.get())
        grados = int(dd)
        minutos_dec = abs(dd - grados) * 60
        minutos = int(minutos_dec)
        segundos = (minutos_dec - minutos) * 60
        resultado_dms.config(text=f"{grados}° {minutos}' {segundos:.2f}\"")
    except:
        resultado_dms.config(text="Valor no válido")

# Función: DMS a DD
def dms_a_dd():
    try:
        grados = int(entry_g.get())
        minutos = int(entry_m.get())
        segundos = float(entry_s.get())
        dd = grados + minutos/60 + segundos/3600
        resultado_dd.config(text=f"{dd:.6f}")
    except:
        resultado_dd.config(text="Valor no válido")

# Crear ventana
ventana = tk.Tk()
ventana.title("Conversor DD <-> DMS por Saiyajin2juan")
ventana.geometry("400x300")

# Sección DD a DMS
tk.Label(ventana, text="Grados Decimales (DD):").pack()
entry_dd = tk.Entry(ventana)
entry_dd.pack()
tk.Button(ventana, text="Convertir a DMS", command=dd_a_dms).pack()
resultado_dms = tk.Label(ventana, text="")
resultado_dms.pack()

# Separador
ttk.Separator(ventana, orient='horizontal').pack(fill='x', pady=10)

# Sección DMS a DD
tk.Label(ventana, text="Grados (°):").pack()
entry_g = tk.Entry(ventana)
entry_g.pack()
tk.Label(ventana, text="Minutos (')").pack()
entry_m = tk.Entry(ventana)
entry_m.pack()
tk.Label(ventana, text='Segundos (")').pack()
entry_s = tk.Entry(ventana)
entry_s.pack()
tk.Button(ventana, text="Convertir a DD", command=dms_a_dd).pack()
resultado_dd = tk.Label(ventana, text="")
resultado_dd.pack()

ventana.mainloop()
