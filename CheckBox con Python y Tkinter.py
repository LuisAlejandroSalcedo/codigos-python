"""
Lo primero que haremos sera importar el modulo tkinter, al cual nos referiremos al el como tk, eso lo asignamos con "as"
"""
import tkinter as tk

"""
Listo, ya tenemos acceso a los metodos de tkinter, lo siguiente que haremos sera crear una clase a la cual
llamare "Applicaction", nuestra clase "Application", heredara metodos y caracteristicas de la clase "Frame" de tkinter, si no etas
familiarizado con la programación orientada a objetos, te sugiero que leas un poco al respecto.
"""
class Application(tk.Frame):
   
    """
    Como siempre, definimos nuestro método __init__, el cual pedirá un argumento llamado "main_window".
    Luego de esto empezamos a crear nuestra ventana, con sus respectivas características.
    """
    def __init__(self, main_window):
        super().__init__(main_window)

        #Definimos el titulo de main_window (Nuestra ventana principal), para esto usamos "title".
        main_window.title("Checkbox con Python y Tkinter")
        
        #Definimos el tamaño de nuestra ventana principal.
        #Le proporcionamos 2 argumentos los cuales son, la anchura y altura de la ventana, esto lo logramos con el metodo place
        self.place(width=300, height=200)

        """
        Ya que hallamos especificado las caracteristicas basicas de nuestra ventana principal,
        procederemos a la creacion de nuestro checkbox.
        """

        """
        Para poder obtener acceso al estado de un checkbox (lo cual es justamente lo que queremos, ya que vamos a mostrarlo en pantalla) 
        primero es necesario crear una variable que pueda almacenar su valor.
        Utilizamos tk.BooleanVar, que representará el estado “activado” como True y “desactivado” como False.
        """
        self.value = tk.BooleanVar(self)

        """Creamos la intacncia del objeto Checkbutton del modulo tkinter, el cual le asignaremos 3 argumentos,
            los cuales son, text (text del chcekbutton), variable (Variable en la cual guardaremos su estado booleano) y
            command (funcion que se llamara al hacer click sobre el checkbutton).
        """
        self.checkbox = tk.Checkbutton(self,
            text="Interruptor",
            variable=self.value,
            command=self.clicked)

        """
        Listo, tenemos nuestro checkbutton preparado, ahora nos falta colocarlo en
        una posicion determinada, eso lo logramos con place, pasandole como argumento su posicion en el eje x,
        y en el eje y.
        """
        self.checkbox.place(x=40, y=70)
        
    
    """
    Si se fijaron, en el argumento command del checkbutton colocamos una funcion llamada clicked, la cual no existe,
    pero ahora la definiremos, esta funcion simplemente nos mostra el valor del checkbutton en la consola, veamos como se hace.
    """
    def clicked(self):
        print(self.value.get())

"""
Muy bien, nuestra clase Application ya esta lista para la accion, fuera de nuestra clase crearemos la intancia del objeto Tk,
creamos una variable llamada app la cual contendra la clase Application y le pasaremos el objeto Tk, luego con ayuda del
metodo mainloop haremos que la ventana salga en pantalla, veamos como queda.
"""
main_window = tk.Tk()
app = Application(main_window)
app.mainloop()

#Codigo de Luis Alejandro, visita nuestra pagina web: www.pythondiario.com