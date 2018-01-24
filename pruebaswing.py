#!/usr/local/bin/jython
# -*- coding: utf-8 -*-
#SE IMPORTAN LAS BIBLIOTECAS GRAFICAS DE SWING
#EL EJEMPLO SOLO CREA UNA VENTANA SIMPLE
from javax.swing import JFrame


class Example(JFrame):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()
#en esta funcion se definen las propiedades de la ventana
    def initUI(self):

        self.setTitle("VENTANA SIMPLE EN JYTHON")
        self.setSize(250, 200)
        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.setLocationRelativeTo(None)
        self.setVisible(True)


if __name__ == '__main__':
    Example()
