from tkinter import messagebox
class Logica:
    def __init__(self):
        self.__correo="alan@gmail.com"
        self.__contra="a1b2c3d4"
    def iniciarsesion(self,correo,contra):
        if (correo == ""):
            messagebox.showerror("Error","Falto llenar el Correo Electronico")
        elif (contra == ""):
            messagebox.showerror("Error","Falto llenar el campo Contraseña")
        else:
            if (correo == self.__correo and contra==self.__contra):
                messagebox.showinfo("Felicidades","Has iniciado correctamente la sesion")
            else:
                messagebox.showerror("Error","Los datos no son validos")
        