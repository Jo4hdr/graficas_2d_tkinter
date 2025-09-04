from tkinter import *

# --------------------
# Ventana principal
# --------------------
ventana = Tk()
ventana.title("Tren con Canvas - Johan")
ventana.geometry("750x500")
ventana.resizable(False, False)
ventana.config(bg="white")

# --------------------
# Lienzo
# --------------------
c = Canvas(ventana, width=730, height=480, bg="white")
c.pack(pady=10)

# --------------------
# Dibujo del tren
# --------------------

# Parte trasera redonda
c.create_oval(120, 200, 190, 320, fill="dimgray", outline="black", width=2)

# Vagón principal
c.create_rectangle(190, 200, 450, 320, fill="lightgray", outline="black", width=2)

# Ventana (cuadro donde va la cara)
c.create_rectangle(330, 120, 450, 200, fill="white", outline="black", width=2)

# Carita en la ventana
c.create_oval(355, 135, 425, 195, fill="yellow", outline="black")
c.create_oval(370, 150, 380, 160, fill="black")  # ojo izquierdo
c.create_oval(400, 150, 410, 160, fill="black")  # ojo derecho
c.create_oval(385, 170, 395, 185, fill="red")    # boca

# cosa arriba
c.create_rectangle(220, 140, 260, 200, fill="grey", outline="black", width=2)
c.create_rectangle(210, 100, 270, 140, fill="dimgray", outline="black", width=2)

# Techo
c.create_rectangle(300, 80, 480, 120, fill="dimgray", outline="black", width=2)

# Texto en el vagón
c.create_text(320, 260, text="Johan Fiallo", font=("Arial", 20, "bold"))

# Ruedas
c.create_oval(200, 300, 260, 360, fill="darkgray", outline="black", width=2)
c.create_oval(280, 300, 340, 360, fill="darkgray", outline="black", width=2)
c.create_oval(360, 300, 420, 360, fill="darkgray", outline="black", width=2)


#  coso de ruedas
c.create_rectangle(230, 330, 310, 340, fill="black")
c.create_rectangle(310, 330, 390, 340, fill="black")

# --------------------
# Ejecutar ventana
# --------------------
ventana.mainloop()

