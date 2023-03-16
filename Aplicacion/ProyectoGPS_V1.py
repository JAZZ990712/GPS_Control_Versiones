#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter
from tkinter import *
from PIL import Image, ImageTk
import cv2
import imutils
from tkinter import ttk
from tkinter import messagebox

video = None

casc = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(casc)

def video_stream():
    global video
    video = cv2.VideoCapture(0)
    iniciar()

def iniciar():
    global video
    ret, frame = video.read()
    if ret == True:
        etiq_de_video.place(x=10, y=20)
        frame = imutils.resize(frame, width=300)
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30,30)
            #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), ((x+w),(y+h)) ,
                         (0, 255, 0), 2)
        img = Image.fromarray(frame)
        image = ImageTk.PhotoImage(image= img)
        etiq_de_video.configure(image = image)
        etiq_de_video.image = image
        etiq_de_video.after(10, iniciar)   

        
def quitar():
    global video
    etiq_de_video.place_forget()
    video.release()
    
def meter(nombre, precio, cantidad):
    tv.insert("", END, nombre, precio, cantidad)
    
def agregar():
    
    tkinter.messagebox.showinfo("Se agrego al carrito", "El articulo ha sido agregado para la compra")
    
def comprar():
    tkinter.messagebox.showinfo("Se realizo la compra", "Usted ha comprado los productos")
    
def eliminar():
    tkinter.messagebox.showinfo("Elimino del carrito", "Elimino un articulo de su carrito, no deseado")
    
    
ventana = tkinter.Tk()
ventana.geometry("800x600")
ventana.title("Tienda")
ventana.resizable(width = False, height = False)
imgBoton1 = PhotoImage(file = "Encendido3.png")
imgBoton2 = PhotoImage(file = "Apagar2.png")
imgBoton3 = PhotoImage(file = "Agregar2.png")
imgBoton4 = PhotoImage(file = "Comprar2.png")
imgBoton5 = PhotoImage(file = "eliminar2.png")
fondo = tkinter.PhotoImage(file="fondo.png")
fondo1 = tkinter.Label(ventana, image = fondo)

tv = ttk.Treeview(ventana, columns=("col1", "col2"))

tv.column("#0", width=260)
tv.column("col1", width=260, anchor= CENTER )
tv.column("col2", width=260, anchor= CENTER )

tv.heading("#0", text= "Productos", anchor= CENTER )
tv.heading("col1", text= "Precios", anchor= CENTER )
tv.heading("col2", text= "Cantidad", anchor= CENTER )

tv.insert("",END, text="Leche", values=("25","5"))
tv.insert("",END, text="Queso", values=("35","10"))
tv.insert("",END, text="Pan", values=("15","8"))


Encender = tkinter.Button(ventana, text="Encender", cursor = "hand2", command = video_stream, width=8, height=3)
Apagar = tkinter.Button(ventana, text="Apagar", cursor = "hand2", command = quitar, width=8, height=3)
Agregar = tkinter.Button(ventana, text="Agregar", cursor = "hand2", command = agregar, width=8, height=3)
Comprar = tkinter.Button(ventana, text="Comprar", cursor = "hand2", command = comprar, width=8, height=3)
Eliminar = tkinter.Button(ventana, text="Eliminar", cursor = "hand2", command = eliminar, width=8, height=3)

#productos = tkinter.Button(ventana, text="Meter", cursor ="hand2", command = meter, width=10, height=2)


lblCarro = tkinter.Label(ventana, text= "Carrito de compras").place(x=550, y= 20)
lstCarro = tkinter.Listbox(ventana, width=40)

lstCarro.insert(END,"Leche")
lstCarro.insert(END,"Queso")
lstCarro.insert(END,"Pan")

etiq_de_video = tkinter.Label(ventana, bg= "black")
etiq_de_video.place(x=10, y= 20)

#producto
Encender.place(x=425, y=40)
Apagar.place(x=425, y= 90)
Agregar.place(x=425, y= 140)
Eliminar.place(x=425, y= 190)
Comprar.place(x=425, y= 240)

lstCarro.place(x=550, y=50)
tv.place(x=10, y = 300)




ventana.mainloop()


# In[1]:


print("HOla MunDo")


# In[ ]:




