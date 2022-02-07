from tkinter import *     #FALTA GUARDAR EL TEXT
from io import *           


raiz=Tk()
raiz.title("Datos de mis apps")
raiz.config(bg="paleturquoise", bd=30, relief="groove", cursor="hand2")

frame=Frame()
frame.pack(side="top",fill="both",expand="True")

frame.config(bg="plum",width=200,height=200, bd=20, relief="groove")

#---------------------algunas funciones---------------------------------
#def vaciarpass():
	#vaciarcontraseña.set("")

#vaciarcontraseña=StringVar()




#-------------------datos planilla--------------------------

labeltitulo=Label(frame,text="Datos de mis apps",bg="white",fg="mediumturquoise",width=37,height=2,justify="center")
#labelnombre.pack()
labeltitulo.grid(row=1,column=0,padx=3,pady=3,sticky="E", columnspan=2)


labelapp=Label(frame,text="App:",bg="white",fg="mediumturquoise",width=13,height=2,justify="right")
#labelnombre.pack()
labelapp.grid(row=2,column=0,padx=3,pady=3,sticky="E")

entryapp=Entry(frame,width=30,fg="mediumturquoise")
entryapp.grid(row=2,column=1,padx=3,pady=3,sticky="W")


labelnombreusuario=Label(frame,text="Usuario:",bg="white",fg="mediumturquoise",width=13,height=2,justify="right")
#labelapellido.pack()
labelnombreusuario.grid(row=3,column=0,padx=3,pady=3,sticky="E")


entrynombreusuario=Entry(frame,width=30,fg="mediumturquoise")
entrynombreusuario.grid(row=3,column=1,padx=3,pady=3,sticky="W")



labelcontraseñaapp=Label(frame,text="Contraseña:",bg="white",fg="mediumturquoise",width=13,height=2,justify="right")
#labeldirec.pack()
labelcontraseñaapp.grid(row=4,column=0,padx=3,pady=3,sticky="E")

entrycontraseñaapp=Entry(frame,width=30,fg="mediumturquoise")
entrycontraseñaapp.grid(row=4,column=1,padx=3,pady=3,sticky="W")


labelemail=Label(frame,text="Email:",bg="white",fg="mediumturquoise",width=13,height=2,justify="right")
#labelemail.pack()
labelemail.grid(row=5,column=0,padx=3,pady=3,sticky="E")

entryemail=Entry(frame,width=30,fg="mediumturquoise")
entryemail.grid(row=5,column=1,padx=3,pady=3,sticky="W")

labeldatos=Label(frame,text="Otros datos:",bg="white",fg="mediumturquoise",width=13,height=2,justify="right")
labeldatos.grid(row=6,column=0,padx=3,pady=3,sticky="NE")

textodatos=Text(frame,bg="white",fg="mediumturquoise",width=23,height=10)
textodatos.grid(row=6,column=1,padx=3,pady=3,sticky="W")


scrolldatos=Scrollbar(frame,command=textodatos.yview)
scrolldatos.grid(row=6,column=2,padx=3,pady=3,sticky="nsew")
textodatos.config(yscrollcommand=scrolldatos.set)

labelpass=Label(frame,text="Contraseña para\nguardar datos:",bg="white",fg="mediumturquoise",width=13,height=2,justify="right")
#labelpass.pack()
labelpass.grid(row=7,column=0,padx=3,pady=3,sticky="E")

entrypass=Entry(frame,width=30,fg="mediumturquoise")#,textvariable=vaciarcontraseña)
entrypass.config(show="$")
entrypass.grid(row=7,column=1,padx=3,pady=3,sticky="W")

#-----------------------botones------------------------------------------------------------
#def vaciarpass():
	#vaciarpass.set("")

#vaciarpass=StringVar()

def contraseña():
	contraseña="mdz10122001"
	passintroducida=entrypass.get()

	if passintroducida==contraseña:
		ejecutar()

	else:
		labelpassincorrecta=Label(frame,text="Contraseña incorrecta",bg="white",fg="mediumturquoise",width=40,height=2,justify="center")
		#labelpass.pack()
		labelpassincorrecta.grid(row=10,column=0,padx=3,pady=3,sticky="W",columnspan=2)
		labelpass.grid(row=12,column=0,padx=3,pady=3,sticky="E")
		entrypass.grid(row=12,column=1,padx=3,pady=3,sticky="E")
		#vaciarpass()
		#botoninfo.grid(row=12,column=1,padx=3,pady=3,sticky="E")
		#labelterminado.grid(row=13,column=3,padx=3,pady=3,sticky="E")

def confirmar():
	
	botoninfo=Button(frame,text="Confirmar",command=contraseña)
	botoninfo.grid(row=13,column=1,padx=3,pady=3,sticky="W")
	

def ejecutar():	
	#posicion=0
	nombre=entryapp.get()
	#nombre.append(entrynombre.get())
	apellido=entrynombreusuario.get()
	#apellido.append(entryapellido.get())
	direccion=entrycontraseñaapp.get()
	#direccion.append(entrydirec.get())
	email=entryemail.get()
	#email.append(entryemail.get())
	#otrosdatos=textodatos.get()
	datos="\nNombre: "+nombre+"\nApellido: "+apellido+"\nDirección: "+direccion+"\nEmail: "+email#+"\nOtros Datos: "+otrosdatos
	#datos=""
	
	
	archext=open("zzdatos_planilla.txt","a")
	archext.write(datos)
	archext.close()

	labelterminado=Label(frame,text="Ya se guardaron sus datos",bg="white",fg="mediumturquoise",width=40,height=2,justify="center")
	#labelpass.pack()
	labelterminado.grid(row=14,column=0,padx=3,pady=3,sticky="W",columnspan=2)
	#posicion+=1
	
	#while posicion>1:
		#nombre.append(entrynombre.get())
		#apellido.append(entryapellido.get())
		#direccion.append(entrydirec.get())
		#email.append(entryemail.get())

		#posicion+=1


	print(datos)




def guardar():	
	labelparaconfirmar=Label(frame,text="Si está seguro/a de guardar\nesta información, presione confirmar",bg="white",fg="mediumturquoise",width=40,height=2,justify="center")
	labelparaconfirmar.grid(row=9,column=0,padx=3,pady=3,sticky="W",columnspan=2)
	#contraseña()
	confirmar()
	
botonconfirmar=Button(frame,text="Guardar",command=guardar)
botonconfirmar.grid(row=8,column=1,padx=3,pady=3,sticky="W")
	
#------------------------------
	



raiz.mainloop()