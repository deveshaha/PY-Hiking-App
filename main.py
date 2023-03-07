import tkinter as tk
import tkinter.ttk as ttk

ventana = tk.Tk()
ventana.title("Agencia de Viajes")


lbl_viajes = tk.Label(ventana, text="Viajes de Senderismo", font=("Arial", 20))
lbl_viajes.pack()

img_logo = tk.PhotoImage(file="res/hiking.png")
img_logo = img_logo.subsample(2,2)
lbl_logo = tk.Label(ventana, image=img_logo)
lbl_logo.pack()

frame_opciones = tk.Frame(ventana)
frame_opciones.pack()

def obtener_seleccion(var):
    return var.get()

opcion = tk.StringVar()
opcion.set("Monte Abantos")
rb_abantos = tk.Radiobutton(frame_opciones, text="Monte Abantos", variable=opcion, value="Monte Abantos", command=obtener_seleccion)
rb_abantos.grid(row=0, column=0)
rb_pedriza = tk.Radiobutton(frame_opciones, text="La Pedriza", variable=opcion, value="La Pedriza", command=obtener_seleccion)
rb_pedriza.grid(row=0, column=1)
rb_dehesas = tk.Radiobutton(frame_opciones, text="Las Dehesas de Cercedilla", variable=opcion, value="Las Dehesas de Cercedilla", command=obtener_seleccion)
rb_dehesas.grid(row=1, column=0)
rb_cabrera = tk.Radiobutton(frame_opciones, text="La Cabrera-Pico de la Miel", variable=opcion, value="La Cabrera-Pico de la Miel", command=obtener_seleccion)
rb_cabrera.grid(row=1, column=1)

espacio = tk.Label(ventana, text=" ")
espacio.pack()

accesorios_frame = tk.Frame(ventana)
accesorios_frame.pack()

mochila_var = tk.BooleanVar()
mochila_cb = tk.Checkbutton(accesorios_frame, text="Mochila", variable=mochila_var)
mochila_cb.pack(side=tk.LEFT, padx=10)

linterna_var = tk.BooleanVar()
linterna_cb = tk.Checkbutton(accesorios_frame, text="Linterna", variable=linterna_var)
linterna_cb.pack(side=tk.LEFT, padx=10)

gps_var = tk.BooleanVar()
gps_cb = tk.Checkbutton(accesorios_frame, text="GPS", variable=gps_var)
gps_cb.pack(side=tk.LEFT, padx=10)

mapa_var = tk.BooleanVar()
mapa_cb = tk.Checkbutton(accesorios_frame, text="Mapa", variable=mapa_var)
mapa_cb.pack(side=tk.LEFT, padx=10)

equipo_frame = tk.Frame(ventana)
equipo_frame.pack()

prismaticos_var = tk.BooleanVar()
prismaticos_cb = tk.Checkbutton(equipo_frame, text="Prismáticos", variable=prismaticos_var)
prismaticos_cb.pack(side=tk.LEFT, padx=10)

cantimplora_var = tk.BooleanVar()
cantimplora_cb = tk.Checkbutton(equipo_frame, text="Cantimplora", variable=cantimplora_var)
cantimplora_cb.pack(side=tk.LEFT, padx=10)

botiquin_var = tk.BooleanVar()
botiquin_cb = tk.Checkbutton(equipo_frame, text="Botiquín", variable=botiquin_var)
botiquin_cb.pack(side=tk.LEFT, padx=10)

crema_var = tk.BooleanVar()
crema_cb = tk.Checkbutton(equipo_frame, text="Crema Solar", variable=crema_var)
crema_cb.pack(side=tk.LEFT, padx=10)

datos_frame = tk.Frame(ventana)
datos_frame.pack(pady=15)

lbl_nombre = tk.Label(datos_frame, text="Nombre")
lbl_nombre.grid(row=0, column=0)
frm_nombre = tk.Entry(datos_frame)
frm_nombre.grid(row=0, column=1)

lbl_apellidos = tk.Label(datos_frame, text="Apellidos")
lbl_apellidos.grid(row=0, column=2)
frm_apellidos = tk.Entry(datos_frame)
frm_apellidos.grid(row=0, column=3)

lbl_telefono = tk.Label(datos_frame, text="Teléfono")
lbl_telefono.grid(row=1, column=0, pady=10, padx=10)
frm_telefono = tk.Entry(datos_frame)
frm_telefono.grid(row=1, column=1, pady=5, padx=10)

lbl_email = tk.Label(datos_frame, text="Email")
lbl_email.grid(row=1, column=2)
frm_email = tk.Entry(datos_frame)
frm_email.grid(row=1, column=3)


poblaciones = ["Madrid", "Alcobendas", "San Sebastián de los Reyes", "Algete", "Pozuelo", "Las Rozas", "Majadahonda", "Móstoles", "Alcorcón", "Boadilla del Monte", "Villaviciosa de Odón"]
opc_poblacion = tk.StringVar()
opc_poblacion.set(poblaciones[0])
cmbx_poblacion = ttk.Combobox(textvariable=opc_poblacion, values=poblaciones)
cmbx_poblacion.pack(pady=10)

frm_lista = tk.Listbox(ventana)
scrollbar = tk.Scrollbar(ventana, orient="vertical")
scrollbar.config(command=frm_lista.yview)
scrollbar.pack(side="right", fill="y")
frm_lista.config(yscrollcommand=scrollbar.set)
frm_lista.config(width=50, height=10)
frm_lista.pack()


def enviar_solicitud():
    nombre = frm_nombre.get()
    apellidos = frm_apellidos.get()
    telefono = frm_telefono.get()
    email = frm_email.get()
    poblacion = opc_poblacion.get()
    excursiones = obtener_seleccion(opcion)
    accesorios = ""
    if mochila_var.get():
        accesorios += "Mochila, "
    if linterna_var.get():
        accesorios += "Linterna, "
    if gps_var.get():
        accesorios += "GPS, "
    if mapa_var.get():
        accesorios += "Mapa, "
    equipo = ""
    if prismaticos_var.get():
        equipo += "Prismáticos, "
    if cantimplora_var.get():
        equipo += "Cantimplora, "
    if botiquin_var.get():
        equipo += "Botiquín, "
    if crema_var.get():
        equipo += "Crema Solar, "
    frm_lista.insert(tk.END, f"Nombre: {nombre} {apellidos}")
    frm_lista.insert(tk.END, f"Teléfono: {telefono}")
    frm_lista.insert(tk.END, f"Email: {email}")
    frm_lista.insert(tk.END, f"Población: {poblacion}")
    frm_lista.insert(tk.END, f"Excursión: {excursiones}")
    frm_lista.insert(tk.END, f"Accesorios: {accesorios}")
    frm_lista.insert(tk.END, f"Equipo: {equipo}")

boton_enviar = tk.Button(ventana, text="Enviar solicitud", command=enviar_solicitud)
boton_enviar.pack(pady=5)

ventana.mainloop()