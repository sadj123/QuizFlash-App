from tkinter import *
from tkinter import messagebox

root=Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Juan","Procesador de textos versión 2018")    

def avisoLicencia():
    messagebox.showwarning("Licencia","Producto bajo licencia GNU")
    
def salirAplicacion():
#    valor = messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
    valor = messagebox.askokcancel("Salir","¿Deseas salir de la aplicación?")
    if valor == True:
        root.destroy()
    
def cerrarDocumento():
     valor = messagebox.askretrycancel("Reintentar","No es posible cerrar. Documento bloqueado")
     if valor == False:
        root.destroy()

barramenu = Menu(root)
root.config(menu=barramenu, width=300, height=300)

archivoMenu=Menu(barramenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)


archivoEdicion=Menu(barramenu)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barramenu)

archivAyuda=Menu(barramenu)
archivAyuda.add_command(label="Licencia", command=avisoLicencia)
archivAyuda.add_command(label="Acerca de....", command=infoAdicional)

barramenu.add_cascade(label="Archivo",menu=archivoMenu)
barramenu.add_cascade(label="Edición",menu=archivoEdicion)
barramenu.add_cascade(label="Herramientas",menu=archivoHerramientas)
barramenu.add_cascade(label="Ayuda",menu=archivAyuda)


root.mainloop()