import math
import os
from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename

guardarArchivo = ''
titulo = ''
textoGuardado = ''
colorTitulo = ''
tamanioFuenteTitulo = 0



class Principal:
    import math

    def __init__(self):
        self.contadorOperadorSuma = 0
        self.estado = 1
        self.estadoSuma = 'SUMA'
        self.estadoSuma = 0
        self.primerNumeroSuma = ''
        self.numeroSuma1 = 0.0
        self.almacenoPrimeroNumero = 0.0
        self.numeroEntrada = False
        self.almacenandoNumeros = False
        self.banderaSuma = False
        self.banderaResta = False
        self.banderaMultiplicacion = False
        self.banderaDivision = False
        self.banderaPotencia = False
        self.banderaRaiz = False
        self.banderaInverso = False
        self.banderaSeno = False
        self.banderaCoseno = False
        self.banderaTangente = False
        self.banderaModulo = False
        self.banderaNumeroSeSuma = False
        self.banderaNumeroSeResta = False
        self.banderaNumeroSeDivide = False
        self.banderaNumeroSeMultiplica = False
        self.banderaNumeroSeEleva = False
        self.banderaNumeroSeRaiz = False
        self.banderaNumeroSeInverso = False
        self.banderaNumeroSeSeno = False
        self.banderaNumeroSeCoseno = False
        self.banderaNumeroSeTangente = False
        self.banderaNumeroSeModulo = False
        self.almacenoValorSeno = 0.0
        self.resultadoFinal = 0.0
        self.contadorOperador = 0
        self.contadorOperadorResta = 0
        self.contadorOperadorDivision = 0
        self.contadorOperadorPotencia = 0
        self.contadorOperadorRaiz = 0
        self.contadorOperadorInverso = 0
        self.contadorOperadorSeno = 0
        self.contadorOperadorCoseno = 0
        self.contadorOperadorTangete = 0
        self.contadorOperadorModulo = 0
        self.modulo = 0.0
        self.modulo2 = 0.0
        self.titulo = ''
        self.textoGuardado = ''
        self.tamanioFuente = ''

    def ReiniciarContadores(self):

        self.contadorOperadorSuma = 1
        self.contadorOperadorResta = 1
        self.contadorOperadorDivision = 1
        self.contadorOperadorPotencia = 1
        self.contadorOperadorRaiz = 1
        self.contadorOperadorInverso = 1
        self.contadorOperadorSeno = 1
        self.contadorOperadorCoseno = 1
        self.contadorOperadorTangete = 1
        self.contadorOperadorModulo = 1

    def Abrir(self):

        try:
            archivo = filedialog.askopenfilename(initialdir=os.getcwd(), title='Selecione archivo',
                                                 filetype=(('txt files', '*.txt*'), ('txt files', '*.txt*')))
            global guardarArchivo
            guardarArchivo = archivo

            my_archivo = open(archivo, "r", encoding="utf8")
            contenido = my_archivo.read()
            my_text.insert(END, contenido)


        except IOError:
            messagebox.showerror('ERROR', 'ERROR EN LA CARGA DEL ARCHIVO')


    def lecturaPrueba2(self):

        with open(guardarArchivo, encoding="utf8") as f:
            juntar = ''
            juntarTodo = ''
            while True:
                c = f.read(1)
                juntar += c
                juntarSinSaltos = juntar
                juntarTodo += c
                if self.estado == 1:
                    if c == '<':
                        self.estado = 2
                        print('Abriendo etiqueta')
                    elif c == '\n':
                        self.estado = 1
                        print('Salto de linea, se regrea a estado 1')
                    elif c == ' ':
                        print('Esto es un espacio de los numeros')
                        self.estado = 3
                    elif c == '/':
                        print('Cerrando etiqueta')
                        # break
                elif self.estado == 2:
                    if str.isalpha(c):
                        self.estado = 2

                    if juntar == '\n<Funcion':
                        print('Esta es una funcion')
                        print(f'{juntar}')
                        self.estado = 4

                    if juntar == '\n</Funcion>':
                        print('Finaliza lectura de Estilo')
                        print(f'{juntar}')
                        juntar = ''
                        self.estado = 1


                    elif c == ' ':
                        juntar = ''
                        self.estado = 2

                    elif c == '>' or '=':
                        if juntar == '<Tipo>':
                            print('Esto es una etiqueta Tipo')
                            print(juntar)
                            print(f'Esto es {juntar}')
                            juntar = ''
                            self.estado = 1

                        elif juntar == '<Texto>':
                            print('Esto es una etiqueta Texto')
                            print(juntar)
                            print(f'Esto es {juntar}')
                            juntar = ''
                            self.estado = 4

                        elif juntar == '\n</Texto>':
                            print('Finaliza etiqueta Texto')
                            print(juntar)
                            print(f'Esto es {juntar}')
                            juntar = ''
                            self.estado = 1

                        elif juntar == '\n<Titulo>':
                            print('Esto es una etiqueta Titulo')
                            print(juntar)
                            print(f'Esto es {juntar}')
                            juntar = ''
                            self.estado = 4

                        elif juntar == '</Titulo>':
                            print('Finaliza etiqueta Titulo')
                            print(juntar)
                            print(f'Esto es {juntar}')
                            juntar = ''
                            self.estado = 1

                        elif juntar == '\n<Descripcion>':
                            print('Esto es una etiqueta Descripcion')
                            print(juntar)
                            print(f'Esto es {juntar}')
                            # my_text2.insert(END, self.textoGuardado)
                            juntar = ''
                            self.estado = 4

                        elif juntar == '</Descripcion>':
                            print('Finaliza etiqueta Descripcion')
                            print(juntar)
                            print(f'Esto es {juntar}')
                            juntar = ''
                            self.estado = 1

                        elif juntar == '\n<Contenido>':
                            print('Esto es una etiqueta CONTENIDO')
                            print(juntar)
                            print(f'Creando archivo de texto donde se guardarán las operaciones')
                            # my_text2.insert(END, juntar)
                            juntar = ''
                            self.estado = 4

                        elif juntar == '</Contenido>':
                            print('Esto es una etiqueta CONTENIDO')
                            print(juntar)
                            print(f'Finaliza etiqueta Contenido')
                            juntar = ''
                            self.estado = 1

                        elif juntar == '\n\n\n<Estilo>':
                            print('Esta es un Estilo')
                            print(f'{juntar}')
                            juntar = ''
                            self.estado = 4

                        elif juntar == '\n</Estilo>':
                            print('Finaliza la seleccion de estilos')
                            print(f'{juntar}')
                            juntar = ''
                            self.estado = 1



                        elif juntar == '\n<Operacion=':
                            print('Esto es una Operacion')
                            print(juntar)
                            juntar = ''
                            self.numeroEntrada = False
                            my_text2.insert(END, '\n----------------------Se Realizará una Operación----------------------')
                            if self.primerNumeroSuma == '':
                                self.primerNumeroSuma = ''
                                self.banderaSuma = False
                                self.banderaResta = False
                                self.banderaMultiplicacion = False
                                self.banderaDivision = False
                                self.banderaPotencia = False
                                self.banderaRaiz = False
                                self.banderaInverso = False
                                # self.banderaSeno = False
                                # self.banderaCoseno = False
                                # self.banderaTangente = False
                                self.banderaModulo = False
                                # self.banderaNumeroSeSuma = False

                            self.estado = 2

                        elif juntar == '\n</Operacion>':
                            print('Finaliza una operacion')
                            print(juntar)
                            juntar = ''
                            self.estado = 1
                            self.resultadoFinal = 0
                            self.contadorOperador = 0
                            my_text2.insert(END, '\n----------------------Se Finalizó una Operación--------------------------\n')
                            if self.banderaSuma == True:
                                self.almacenoPrimeroNumero = 0.0
                                self.banderaSuma = False
                                self.numeroEntrada = False
                                self.banderaNumeroSeSuma = False
                            if self.banderaResta == True:
                                self.almacenoPrimeroNumero = 0.0
                                self.banderaResta = False
                                self.numeroEntrada = False
                                self.banderaNumeroSeResta = False
                            if self.banderaMultiplicacion == True:
                                self.almacenoPrimeroNumero = 0.0
                                self.banderaMultiplicacion = False
                                self.numeroEntrada = False
                                self.banderaNumeroSeMultiplica = False
                            if self.banderaDivision == True:
                                self.almacenoPrimeroNumero = 0.0
                                self.banderaDivision = False
                                self.numeroEntrada = False
                                self.banderaNumeroSeDivide = False
                            if self.banderaPotencia == True:
                                self.almacenoPrimeroNumero = 0.0
                                self.banderaPotencia = False
                                self.banderaNumeroSeEleva = False
                                self.numeroEntrada = False
                            if self.banderaRaiz == True:
                                self.almacenoPrimeroNumero = 0.0
                                self.banderaRaiz = False
                                self.banderaNumeroSeRaiz = False
                                self.numeroEntrada = False
                            if self.banderaInverso == True:
                                self.almacenoPrimeroNumero = 0.0
                                self.banderaInverso = False
                                self.banderaNumeroSeInverso = False
                                self.numeroEntrada = False
                            if self.banderaSeno == True:
                                self.almacenoPrimeroNumero = 0.0
                                self.banderaSeno = False
                                self.banderaNumeroSeSeno = False
                                self.numeroEntrada = False
                            if self.banderaCoseno == True:
                                self.almacenoPrimeroNumero = 0.0
                                self.banderaCoseno = False
                                self.banderaNumeroSeCoseno = False
                                self.numeroEntrada = False
                            if self.banderaTangente == True:
                                self.almacenoPrimeroNumero = 0.0
                                self.banderaTangente = False
                                self.banderaNumeroSeTangente = False
                                self.numeroEntrada = False
                            if self.banderaModulo == True:
                                self.almacenoPrimeroNumero = 0.0
                                self.banderaModulo = False
                                self.banderaNumeroSeModulo = False
                                self.numeroEntrada = False


                        elif juntar == 'SUMA>':
                            print('Esto es una SUMA')
                            juntar = ''
                            self.banderaSuma = True
                            self.contadorOperadorSuma += 1
                            # my_text2.insert(END, '\nSe Realizara una Suma')

                        elif juntar == 'RESTA>':
                            print('Esto es una RESTA')
                            juntar = ''
                            self.banderaResta = True
                            self.contadorOperadorResta += 1
                            # my_text2.insert(END, '\nSe Realizara una Resta')

                        elif juntar == 'MULTIPLICACION>':
                            print('Esto es una MULTIPLICACION')
                            juntar = ''
                            self.banderaMultiplicacion = True
                            self.contadorOperador += 1
                            # my_text2.insert(END, '\nSe Realizara una Multiplicación')

                        elif juntar == 'DIVISION>':
                            print('Esto es una DIVISION')
                            juntar = ''
                            self.banderaDivision = True
                            self.contadorOperadorDivision += 1
                            # my_text2.insert(END, '\nSe Realizará una División')

                        elif juntar == 'POTENCIA>':
                            print('Esto es una POTENCIA')
                            juntar = ''
                            self.banderaPotencia = True
                            self.contadorOperadorPotencia += 1
                            # my_text2.insert(END, '\nSe Realizará una Potencia')

                        elif juntar == 'RAIZ>':
                            print('Esto es una RAIZ')
                            juntar = ''
                            self.banderaRaiz = True
                            self.contadorOperadorRaiz += 1

                        elif juntar == 'INVERSO>':
                            print('Esto es una RAIZ')
                            juntar = ''
                            self.banderaInverso = True
                            self.contadorOperadorInverso += 1


                        elif juntar == 'SENO>':
                            print('Esto es SENO')
                            juntar = ''
                            self.banderaSeno = True
                            self.contadorOperadorSeno += 1

                        elif juntar == 'COSENO>':
                            print('Esto es COSENO')
                            juntar = ''
                            self.banderaCoseno = True
                            self.contadorOperadorCoseno += 1

                        elif juntar == 'TANGENTE>':
                            print('Esto es TANGENTE')
                            juntar = ''
                            self.banderaTangente = True
                            self.contadorOperadorTangete += 1

                        elif juntar == 'MODULO>':
                            print('Esto es MODULO')
                            juntar = ''
                            self.banderaModulo = True
                            self.contadorOperadorModulo += 1

                        elif juntar == '\n<Numero>':
                            print('Esto es un Numero')
                            print(juntar)
                            juntar = ''
                            self.estado = 1

                        elif juntar == '\n</Tipo>':
                            print('Finaliza la etiqueta Tipo')
                            print(juntar)
                            juntar = ''
                            self.estado = 1
                            self.contadorOperador = 0
                            self.contadorOperadorResta = 0
                            self.contadorOperadorDivision = 0
                            self.contadorOperadorPotencia = 0
                            self.contadorOperadorRaiz = 0
                            self.contadorOperadorInverso = 0
                            self.contadorOperadorSeno = 0
                            self.contadorOperadorCoseno = 0
                            self.contadorOperadorTangete = 0
                            self.contadorOperadorModulo = 0
                            my_text2.insert(END, '\nFinalizó la lectura')
                            return

                        elif juntar == '</Numero>':
                            print('Cerrando Etiqueta Numero')
                            print(juntar)
                            juntar = ''
                            self.estado = 1

#TODO LAS OPERACIONES DE SUMA

                            if self.banderaSuma == True:
                                if self.numeroEntrada == False:
                                    self.almacenoPrimeroNumero = float(self.primerNumeroSuma)
                                    my_text2.insert(END, f'\n\nSe sumarán: \n\n {self.almacenoPrimeroNumero}')
                                    if self.resultadoFinal == False:
                                        self.resultadoFinal = self.almacenoPrimeroNumero
                                        print(f'Guardo el numero {self.resultadoFinal}')
                                    self.primerNumeroSuma = ''
                                    self.numeroEntrada = True
                                    self.banderaNumeroSeSuma = True

                                elif self.numeroEntrada == True:
                                    my_text2.insert(END, f' + {self.primerNumeroSuma}')
                                    self.almacenoPrimeroNumero += float(self.primerNumeroSuma)
                                    print('El Resultado de la SUMA es:', self.almacenoPrimeroNumero)
                                    my_text2.insert(END, f' = {self.almacenoPrimeroNumero}')
                                    my_text2.insert(END, f'\n {self.almacenoPrimeroNumero}')
                                    self.primerNumeroSuma = ''
                                    if self.banderaNumeroSeResta == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} - {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal -= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeResta = False
                                    if self.banderaNumeroSeSuma == True and self.contadorOperadorSuma > 2:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal += self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.banderaNumeroSeSuma = False
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                    if self.banderaNumeroSeDivide == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} / {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero /= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeDivide = False
                                    if self.banderaNumeroSeMultiplica == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} * {self.resultadoFinal}\n')
                                        self.resultadoFinal *= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeMultiplica = False
                                    if self.banderaNumeroSeEleva == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} ^ {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero **= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeEleva = False
                                    if self.banderaNumeroSeRaiz == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        suRaiz2 = pow(self.resultadoFinal, 0.5) + self.almacenoPrimeroNumero
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suRaiz2}\n')
                                        print(f'EL RESULTADO FINAL ES {suRaiz2}')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeRaiz = False
                                    if self.banderaNumeroSeInverso == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} invert {self.almacenoPrimeroNumero}\n')
                                        res2 = pow(self.resultadoFinal, -1, int(self.almacenoPrimeroNumero))
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {res2}\n')
                                        print('El Resultado del Inverso es:', res2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeInverso = False
                                    if self.banderaSeno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Seno de {self.almacenoPrimeroNumero}\n')
                                        suSeno2 = math.sin(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suSeno2} en radianes\n')
                                        print('Su valor de Seno es:', suSeno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeSeno = False
                                    if self.banderaCoseno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Coseno de {self.almacenoPrimeroNumero}\n')
                                        suCoseno2 = math.cos(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suCoseno2} en radianes\n')
                                        print('Su valor de Coseno es:', suCoseno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeCoseno = False
                                    if self.banderaTangente == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Tangente de {self.almacenoPrimeroNumero}\n')
                                        suTangente2 = math.tan(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suTangente2} en radianes\n')
                                        print('Su valor de Tangente es:', suTangente2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeTangente = False
                                    if self.banderaNumeroSeModulo == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Modulo de {self.resultadoFinal} % {self.almacenoPrimeroNumero}\n')
                                        self.modulo2 = self.resultadoFinal % float(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.modulo2}\n')
                                        print('El Resultado de la MODULO es:', self.modulo2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeModulo = False
#TODO LAS OPERACIONES DE RESTA

                            if self.banderaResta == True:
                                if self.numeroEntrada == False:
                                    self.almacenoPrimeroNumero = float(self.primerNumeroSuma)
                                    my_text2.insert(END, f'\n\nSe Restarán: \n\n {self.almacenoPrimeroNumero}')
                                    print(f'Este es el primero numero a restar {self.almacenoPrimeroNumero}')
                                    if self.resultadoFinal == False:
                                        self.resultadoFinal = self.almacenoPrimeroNumero
                                    self.primerNumeroSuma = ''
                                    self.numeroEntrada = True
                                    self.banderaNumeroSeResta = True

                                elif self.numeroEntrada == True:
                                    my_text2.insert(END, f' - {self.primerNumeroSuma}')
                                    self.almacenoPrimeroNumero -= float(self.primerNumeroSuma)
                                    print('El Resultado de la RESTA es:', self.almacenoPrimeroNumero)
                                    my_text2.insert(END, f' = {self.almacenoPrimeroNumero}')
                                    my_text2.insert(END, f'\n {self.almacenoPrimeroNumero}')
                                    self.primerNumeroSuma = ''
                                    if self.banderaNumeroSeResta == True and self.contadorOperadorResta > 2:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} - {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal -= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeResta = False
                                    if self.banderaNumeroSeSuma == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal += self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeSuma = False
                                    if self.banderaNumeroSeDivide == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} / {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero /= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeDivide = False
                                    if self.banderaNumeroSeMultiplica == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} * {self.resultadoFinal}\n')
                                        self.resultadoFinal *= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeMultiplica = False
                                    if self.banderaNumeroSeEleva == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} ^ {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero **= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeEleva = False
                                    if self.banderaNumeroSeRaiz == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        suRaiz2 = pow(self.resultadoFinal, 0.5) + self.almacenoPrimeroNumero
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suRaiz2}\n')
                                        print(f'EL RESULTADO FINAL ES {suRaiz2}')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeRaiz = False
                                    if self.banderaNumeroSeInverso == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} invert {self.almacenoPrimeroNumero}\n')
                                        res2 = pow(self.resultadoFinal, -1, int(self.almacenoPrimeroNumero))
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {res2}\n')
                                        print('El Resultado del Inverso es:', res2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeInverso = False
                                    if self.banderaSeno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Seno de {self.almacenoPrimeroNumero}\n')
                                        suSeno2 = math.sin(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suSeno2} en radianes\n')
                                        print('Su valor de Seno es:', suSeno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeSeno = False
                                    if self.banderaCoseno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Coseno de {self.almacenoPrimeroNumero}\n')
                                        suCoseno2 = math.cos(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suCoseno2} en radianes\n')
                                        print('Su valor de Coseno es:', suCoseno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeCoseno = False
                                    if self.banderaTangente == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Tangente de {self.almacenoPrimeroNumero}\n')
                                        suTangente2 = math.tan(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suTangente2} en radianes\n')
                                        print('Su valor de Tangente es:', suTangente2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeTangente = False
                                    if self.banderaNumeroSeModulo == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Modulo de {self.resultadoFinal} % {self.almacenoPrimeroNumero}\n')
                                        self.modulo2 = self.resultadoFinal % float(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.modulo2}\n')
                                        print('El Resultado de la MODULO es:', self.modulo2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeModulo = False
#TODO LAS OPERACIONES DE MULTIPLICACION

                            if self.banderaMultiplicacion == True:
                                if self.numeroEntrada == False:
                                    self.almacenoPrimeroNumero = float(self.primerNumeroSuma)
                                    my_text2.insert(END, f'\n\nSe Multiplicarán: \n\n {self.almacenoPrimeroNumero}')
                                    print(f'Este es el primero numero a multiplicar {self.almacenoPrimeroNumero}')
                                    if self.resultadoFinal == False:
                                        self.resultadoFinal = self.almacenoPrimeroNumero
                                        print(f'Guardo el numero {self.resultadoFinal}')
                                    self.primerNumeroSuma = ''
                                    self.numeroEntrada = True
                                    self.banderaNumeroSeMultiplica = True

                                elif self.numeroEntrada == True:
                                    my_text2.insert(END, f' * {self.primerNumeroSuma}')
                                    self.almacenoPrimeroNumero *= float(self.primerNumeroSuma)
                                    print('El Resultado de la MULTIPLICACION es:', self.almacenoPrimeroNumero)
                                    my_text2.insert(END, f' = {self.almacenoPrimeroNumero}')
                                    my_text2.insert(END, f'\n {self.almacenoPrimeroNumero}\n')
                                    self.primerNumeroSuma = ''
                                    if self.banderaNumeroSeSuma == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal += self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeSuma = False
                                    if self.banderaNumeroSeResta == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} - {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal -= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeResta = False
                                    if self.banderaNumeroSeDivide == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} / {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero /= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeDivide = False
                                    if self.banderaNumeroSeMultiplica == True and self.contadorOperador >= 2:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} * {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal *= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeMultiplica = False
                                    if self.banderaNumeroSeEleva == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} ^ {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero **= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeEleva = False
                                    if self.banderaNumeroSeRaiz == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        suRaiz2 = pow(self.resultadoFinal, 0.5) + self.almacenoPrimeroNumero
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suRaiz2}\n')
                                        print(f'EL RESULTADO FINAL ES {suRaiz2}')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeRaiz = False
                                    if self.banderaNumeroSeInverso == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} invert {self.almacenoPrimeroNumero}\n')
                                        res2 = pow(self.resultadoFinal, -1, int(self.almacenoPrimeroNumero))
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {res2}\n')
                                        print('El Resultado del Inverso es:', res2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeInverso = False
                                    if self.banderaSeno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Seno de {self.almacenoPrimeroNumero}\n')
                                        suSeno2 = math.sin(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suSeno2} en radianes\n')
                                        print('Su valor de Seno es:', suSeno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeSeno = False
                                    if self.banderaCoseno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Coseno de {self.almacenoPrimeroNumero}\n')
                                        suCoseno2 = math.cos(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suCoseno2} en radianes\n')
                                        print('Su valor de Coseno es:', suCoseno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeCoseno = False
                                    if self.banderaTangente == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Tangente de {self.almacenoPrimeroNumero}\n')
                                        suTangente2 = math.tan(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suTangente2} en radianes\n')
                                        print('Su valor de Tangente es:', suTangente2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeTangente = False
                                    if self.banderaNumeroSeModulo == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Modulo de {self.resultadoFinal} % {self.almacenoPrimeroNumero}\n')
                                        self.modulo2 = self.resultadoFinal % float(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.modulo2}\n')
                                        print('El Resultado de la MODULO es:', self.modulo2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeModulo = False
#TODO LAS OPERACIONES DE DIVISION

                            if self.banderaDivision == True:
                                if self.numeroEntrada == False:
                                    self.almacenoPrimeroNumero = float(self.primerNumeroSuma)
                                    my_text2.insert(END, f'\n\nSe Dividirán: \n\n {self.almacenoPrimeroNumero}')
                                    print(f'Este es el primero numero a dividir {self.almacenoPrimeroNumero}\n')
                                    if self.resultadoFinal == False:
                                        self.resultadoFinal = self.almacenoPrimeroNumero
                                    self.primerNumeroSuma = ''
                                    self.numeroEntrada = True
                                    self.banderaNumeroSeDivide = True

                                elif self.numeroEntrada == True:
                                    my_text2.insert(END, f' / {self.primerNumeroSuma}')
                                    self.almacenoPrimeroNumero /= float(self.primerNumeroSuma)
                                    print('El Resultado de la DIVISION es:', self.almacenoPrimeroNumero)
                                    my_text2.insert(END, f' = {self.almacenoPrimeroNumero}')
                                    my_text2.insert(END, f'\n {self.almacenoPrimeroNumero}\n')
                                    self.primerNumeroSuma = ''
                                    if self.banderaNumeroSeSuma == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal += self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeSuma = False
                                    if self.banderaNumeroSeResta == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} - {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal -= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeResta = False
                                    if self.banderaNumeroSeDivide == True and self.contadorOperadorDivision > 2:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} / {self.almacenoPrimeroNumero}\n')
                                        self.almacenoPrimeroNumero /= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeDivide = False
                                    if self.banderaNumeroSeMultiplica == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} * {self.resultadoFinal}\n')
                                        self.resultadoFinal *= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeMultiplica = False
                                    if self.banderaNumeroSeEleva == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} ^ {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero **= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeEleva = False
                                    if self.banderaNumeroSeRaiz == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        suRaiz2 = pow(self.resultadoFinal, 0.5) + self.almacenoPrimeroNumero
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suRaiz2}\n')
                                        print(f'EL RESULTADO FINAL ES {suRaiz2}')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeRaiz = False
                                    if self.banderaNumeroSeInverso == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} invert {self.almacenoPrimeroNumero}\n')
                                        res2 = pow(self.resultadoFinal, -1, int(self.almacenoPrimeroNumero))
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {res2}\n')
                                        print('El Resultado del Inverso es:', res2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeInverso = False
                                    if self.banderaSeno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Seno de {self.almacenoPrimeroNumero}\n')
                                        suSeno2 = math.sin(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suSeno2} en radianes\n')
                                        print('Su valor de Seno es:', suSeno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeSeno = False
                                    if self.banderaCoseno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Coseno de {self.almacenoPrimeroNumero}\n')
                                        suCoseno2 = math.cos(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suCoseno2} en radianes\n')
                                        print('Su valor de Coseno es:', suCoseno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeCoseno = False
                                    if self.banderaTangente == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Tangente de {self.almacenoPrimeroNumero}\n')
                                        suTangente2 = math.tan(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suTangente2} en radianes\n')
                                        print('Su valor de Tangente es:', suTangente2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeTangente = False
                                    if self.banderaNumeroSeModulo == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Modulo de {self.resultadoFinal} % {self.almacenoPrimeroNumero}\n')
                                        self.modulo2 = self.resultadoFinal % float(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.modulo2}\n')
                                        print('El Resultado de la MODULO es:', self.modulo2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeModulo = False
#TODO LAS OPERACIONES DE POTENCIA

                            if self.banderaPotencia == True:
                                if self.numeroEntrada == False:
                                    self.almacenoPrimeroNumero = float(self.primerNumeroSuma)
                                    my_text2.insert(END, f'\n\nSe Potenciará: \n\n {self.almacenoPrimeroNumero}')
                                    print(f'Este es el numero a potenciar {self.almacenoPrimeroNumero}')
                                    if self.resultadoFinal == False:
                                        self.resultadoFinal = self.almacenoPrimeroNumero
                                    self.primerNumeroSuma = ''
                                    self.numeroEntrada = True
                                    self.banderaNumeroSeEleva = True

                                elif self.numeroEntrada == True:
                                    my_text2.insert(END, f' ^ {self.primerNumeroSuma}')
                                    self.almacenoPrimeroNumero **= float(self.primerNumeroSuma)
                                    print('El Resultado de la POTENCIA es:', self.almacenoPrimeroNumero)
                                    my_text2.insert(END, f' = {self.almacenoPrimeroNumero}')
                                    my_text2.insert(END, f'\n {self.almacenoPrimeroNumero}\n')
                                    self.primerNumeroSuma = ''
                                    if self.banderaNumeroSeSuma == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal += self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeSuma = False
                                    if self.banderaNumeroSeResta == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} - {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal -= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeResta = False
                                    if self.banderaNumeroSeDivide == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} / {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero /= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeDivide = False
                                    if self.banderaNumeroSeMultiplica == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} * {self.resultadoFinal}\n')
                                        self.resultadoFinal *= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeMultiplica = False
                                    if self.banderaNumeroSeEleva == True and self.contadorOperadorPotencia > 2:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} ^ {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero **= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.almacenoPrimeroNumero}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeEleva = False
                                    if self.banderaNumeroSeRaiz == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        suRaiz2 = pow(self.resultadoFinal, 0.5) + self.almacenoPrimeroNumero
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suRaiz2}\n')
                                        print(f'EL RESULTADO FINAL ES {suRaiz2}')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeRaiz = False
                                    if self.banderaNumeroSeInverso == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} invert {self.almacenoPrimeroNumero}\n')
                                        res2 = pow(self.resultadoFinal, -1, int(self.almacenoPrimeroNumero))
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {res2}\n')
                                        print('El Resultado del Inverso es:', res2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeInverso = False
                                    if self.banderaSeno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Seno de {self.almacenoPrimeroNumero}\n')
                                        suSeno2 = math.sin(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suSeno2} en radianes\n')
                                        print('Su valor de Seno es:', suSeno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeSeno = False
                                    if self.banderaCoseno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Coseno de {self.almacenoPrimeroNumero}\n')
                                        suCoseno2 = math.cos(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suCoseno2} en radianes\n')
                                        print('Su valor de Coseno es:', suCoseno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeCoseno = False
                                    if self.banderaTangente == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Tangente de {self.almacenoPrimeroNumero}\n')
                                        suTangente2 = math.tan(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suTangente2} en radianes\n')
                                        print('Su valor de Tangente es:', suTangente2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeTangente = False
                                    if self.banderaNumeroSeModulo == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Modulo de {self.resultadoFinal} % {self.almacenoPrimeroNumero}\n')
                                        self.modulo2 = self.resultadoFinal % float(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.modulo2}\n')
                                        print('El Resultado de la MODULO es:', self.modulo2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeModulo = False
#TODO LO DE RAIZ
                            if self.banderaRaiz == True:
                                if self.numeroEntrada == False:
                                    self.almacenoPrimeroNumero = float(self.primerNumeroSuma)
                                    my_text2.insert(END, f'\n\nSe Sacará Raíz: \n\n Raíz de {self.almacenoPrimeroNumero}')
                                    print(f'Este es el numero a sacar raiz {self.almacenoPrimeroNumero}')
                                    if self.resultadoFinal == False:
                                        self.resultadoFinal = self.almacenoPrimeroNumero
                                    suRaiz = pow(self.almacenoPrimeroNumero, 0.5)
                                    my_text2.insert(END, f' = {suRaiz}')
                                    my_text2.insert(END, f'\n {suRaiz}\n')
                                    print('Su Raiz es:', suRaiz)
                                    self.primerNumeroSuma = ''
                                    self.numeroEntrada = True
                                    self.banderaNumeroSeRaiz = True

                                if self.banderaNumeroSeSuma == True:
                                    my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                    my_text2.insert(END, f'\n {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                    self.resultadoFinal += self.almacenoPrimeroNumero
                                    print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                    my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                    self.contadorOperadorSuma = 1
                                    self.contadorOperadorResta = 1
                                    self.contadorOperadorDivision = 1
                                    self.contadorOperadorPotencia = 1
                                    self.contadorOperadorRaiz = 1
                                    self.contadorOperadorInverso = 1
                                    self.contadorOperadorSeno = 1
                                    self.contadorOperadorCoseno = 1
                                    self.contadorOperadorTangete = 1
                                    self.contadorOperadorModulo = 1
                                    self.banderaNumeroSeSuma = False
                                if self.banderaNumeroSeResta == True:
                                    my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                    my_text2.insert(END, f'\n {self.resultadoFinal} - {self.almacenoPrimeroNumero}\n')
                                    self.resultadoFinal -= self.almacenoPrimeroNumero
                                    print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                    my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                    self.contadorOperadorSuma = 1
                                    self.contadorOperadorResta = 1
                                    self.contadorOperadorDivision = 1
                                    self.contadorOperadorPotencia = 1
                                    self.contadorOperadorRaiz = 1
                                    self.contadorOperadorInverso = 1
                                    self.contadorOperadorSeno = 1
                                    self.contadorOperadorCoseno = 1
                                    self.contadorOperadorTangete = 1
                                    self.contadorOperadorModulo = 1
                                    self.banderaNumeroSeResta = False
                                if self.banderaNumeroSeDivide == True:
                                    my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                    my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} / {self.resultadoFinal}\n')
                                    self.almacenoPrimeroNumero /= self.resultadoFinal
                                    print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                    my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                    self.contadorOperadorSuma = 1
                                    self.contadorOperadorResta = 1
                                    self.contadorOperadorDivision = 1
                                    self.contadorOperadorPotencia = 1
                                    self.contadorOperadorRaiz = 1
                                    self.contadorOperadorInverso = 1
                                    self.contadorOperadorSeno = 1
                                    self.contadorOperadorCoseno = 1
                                    self.contadorOperadorTangete = 1
                                    self.contadorOperadorModulo = 1
                                    self.banderaNumeroSeDivide = False
                                if self.banderaNumeroSeMultiplica == True:
                                    my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                    my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} * {self.resultadoFinal}\n')
                                    self.resultadoFinal *= self.almacenoPrimeroNumero
                                    print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                    my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                    self.contadorOperadorSuma = 1
                                    self.contadorOperadorResta = 1
                                    self.contadorOperadorDivision = 1
                                    self.contadorOperadorPotencia = 1
                                    self.contadorOperadorRaiz = 1
                                    self.contadorOperadorInverso = 1
                                    self.contadorOperadorSeno = 1
                                    self.contadorOperadorCoseno = 1
                                    self.contadorOperadorTangete = 1
                                    self.contadorOperadorModulo = 1
                                    self.banderaNumeroSeMultiplica = False
                                if self.banderaNumeroSeEleva == True:
                                    my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                    my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} ^ {self.resultadoFinal}\n')
                                    self.almacenoPrimeroNumero **= self.resultadoFinal
                                    print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                    my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                    self.contadorOperadorSuma = 1
                                    self.contadorOperadorResta = 1
                                    self.contadorOperadorDivision = 1
                                    self.contadorOperadorPotencia = 1
                                    self.contadorOperadorRaiz = 1
                                    self.contadorOperadorInverso = 1
                                    self.contadorOperadorSeno = 1
                                    self.contadorOperadorCoseno = 1
                                    self.contadorOperadorTangete = 1
                                    self.contadorOperadorModulo = 1
                                    self.banderaNumeroSeEleva = False
                                if self.banderaNumeroSeRaiz == True and self.contadorOperadorRaiz > 2:
                                    my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                    my_text2.insert(END, f'\n Raiz de {suRaiz}')
                                    suRaiz2 = pow(self.resultadoFinal, 0.5)
                                    suRaiz3 = pow(suRaiz2, 0.5)
                                    print(f'EL RESULTADO FINAL DE LA RAIZ ES {suRaiz3}')
                                    my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suRaiz3}\n')
                                    self.contadorOperadorSuma = 1
                                    self.contadorOperadorResta = 1
                                    self.contadorOperadorDivision = 1
                                    self.contadorOperadorPotencia = 1
                                    self.contadorOperadorRaiz = 1
                                    self.contadorOperadorInverso = 1
                                    self.contadorOperadorSeno = 1
                                    self.contadorOperadorCoseno = 1
                                    self.contadorOperadorTangete = 1
                                    self.contadorOperadorModulo = 1
                                    self.banderaNumeroSeRaiz = False
                                if self.banderaNumeroSeInverso == True:
                                    my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                    my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} invert {self.almacenoPrimeroNumero}\n')
                                    res2 = pow(self.resultadoFinal, -1, int(self.almacenoPrimeroNumero))
                                    my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {res2}\n')
                                    print('El Resultado del Inverso es:', res2)
                                    self.contadorOperadorSuma = 1
                                    self.contadorOperadorResta = 1
                                    self.contadorOperadorDivision = 1
                                    self.contadorOperadorPotencia = 1
                                    self.contadorOperadorRaiz = 1
                                    self.contadorOperadorInverso = 1
                                    self.contadorOperadorSeno = 1
                                    self.contadorOperadorCoseno = 1
                                    self.contadorOperadorTangete = 1
                                    self.contadorOperadorModulo = 1
                                    self.primerNumeroSuma = ''
                                    self.banderaNumeroSeInverso = False
                                if self.banderaSeno == True:
                                    my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                    my_text2.insert(END, f'\n Seno de {self.almacenoPrimeroNumero}\n')
                                    suSeno2 = math.sin(self.almacenoPrimeroNumero)
                                    my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suSeno2} en radianes\n')
                                    print('Su valor de Seno es:', suSeno2)
                                    self.contadorOperadorSuma = 1
                                    self.contadorOperadorResta = 1
                                    self.contadorOperadorDivision = 1
                                    self.contadorOperadorPotencia = 1
                                    self.contadorOperadorRaiz = 1
                                    self.contadorOperadorInverso = 1
                                    self.contadorOperadorSeno = 1
                                    self.contadorOperadorCoseno = 1
                                    self.contadorOperadorTangete = 1
                                    self.contadorOperadorModulo = 1
                                    self.primerNumeroSuma = ''
                                    self.banderaNumeroSeSeno = False
                                if self.banderaCoseno == True:
                                    my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                    my_text2.insert(END, f'\n Coseno de {self.almacenoPrimeroNumero}\n')
                                    suCoseno2 = math.cos(self.almacenoPrimeroNumero)
                                    my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suCoseno2} en radianes\n')
                                    print('Su valor de Coseno es:', suCoseno2)
                                    self.contadorOperadorSuma = 1
                                    self.contadorOperadorResta = 1
                                    self.contadorOperadorDivision = 1
                                    self.contadorOperadorPotencia = 1
                                    self.contadorOperadorRaiz = 1
                                    self.contadorOperadorInverso = 1
                                    self.contadorOperadorSeno = 1
                                    self.contadorOperadorCoseno = 1
                                    self.contadorOperadorTangete = 1
                                    self.contadorOperadorModulo = 1
                                    self.primerNumeroSuma = ''
                                    self.banderaNumeroSeCoseno = False
                                if self.banderaTangente == True:
                                    my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                    my_text2.insert(END, f'\n Tangente de {self.almacenoPrimeroNumero}\n')
                                    suTangente2 = math.tan(self.almacenoPrimeroNumero)
                                    my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suTangente2} en radianes\n')
                                    print('Su valor de Tangente es:', suTangente2)
                                    self.contadorOperadorSuma = 1
                                    self.contadorOperadorResta = 1
                                    self.contadorOperadorDivision = 1
                                    self.contadorOperadorPotencia = 1
                                    self.contadorOperadorRaiz = 1
                                    self.contadorOperadorInverso = 1
                                    self.contadorOperadorSeno = 1
                                    self.contadorOperadorCoseno = 1
                                    self.contadorOperadorTangete = 1
                                    self.contadorOperadorModulo = 1
                                    self.primerNumeroSuma = ''
                                    self.banderaNumeroSeTangente = False
                                if self.banderaNumeroSeModulo == True:
                                    my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                    my_text2.insert(END, f'\n Modulo de {self.resultadoFinal} % {self.almacenoPrimeroNumero}\n')
                                    self.modulo2 = self.resultadoFinal % float(self.almacenoPrimeroNumero)
                                    my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.modulo2}\n')
                                    print('El Resultado de la MODULO es:', self.modulo2)
                                    self.contadorOperadorSuma = 1
                                    self.contadorOperadorResta = 1
                                    self.contadorOperadorDivision = 1
                                    self.contadorOperadorPotencia = 1
                                    self.contadorOperadorRaiz = 1
                                    self.contadorOperadorInverso = 1
                                    self.contadorOperadorSeno = 1
                                    self.contadorOperadorCoseno = 1
                                    self.contadorOperadorTangete = 1
                                    self.contadorOperadorModulo = 1
                                    self.banderaNumeroSeModulo = False

#TODO LAS OPERACIONES DE INVERSO

                            if self.banderaInverso == True:
                                if self.numeroEntrada == False:
                                    self.almacenoPrimeroNumero = int(self.primerNumeroSuma)
                                    my_text2.insert(END, f'\n\nSe Invertirá: \n\n {self.almacenoPrimeroNumero}')
                                    print(f'Este es el numero a para inverso {self.almacenoPrimeroNumero}')
                                    if self.resultadoFinal == False:
                                        self.resultadoFinal = self.almacenoPrimeroNumero
                                    self.primerNumeroSuma = ''
                                    self.numeroEntrada = True
                                    self.banderaNumeroSeInverso = True

                                elif self.numeroEntrada == True:
                                    my_text2.insert(END, f' invert {self.primerNumeroSuma}')
                                    res = pow(self.almacenoPrimeroNumero, -1, int(self.primerNumeroSuma))
                                    print('El Resultado del Inverso es:', res)
                                    my_text2.insert(END, f' = {res}')
                                    my_text2.insert(END, f'\n {res}\n')
                                    self.almacenoPrimeroNumero = res
                                    self.primerNumeroSuma = ''
                                    if self.banderaNumeroSeSuma == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal += self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeSuma = False
                                    if self.banderaNumeroSeResta == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} - {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal -= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeResta = False
                                    if self.banderaNumeroSeDivide == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} / {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero /= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeDivide = False
                                    if self.banderaNumeroSeMultiplica == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} * {self.resultadoFinal}\n')
                                        self.resultadoFinal *= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeMultiplica = False
                                    if self.banderaNumeroSeEleva == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} ^ {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero **= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeEleva = False
                                    if self.banderaNumeroSeRaiz == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        suRaiz2 = pow(self.resultadoFinal, 0.5) + self.almacenoPrimeroNumero
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suRaiz2}\n')
                                        print(f'EL RESULTADO FINAL ES {suRaiz2}')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeRaiz = False
                                    if self.banderaNumeroSeInverso == True and self.contadorOperadorInverso > 2:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {res} invert {self.resultadoFinal}\n')
                                        res2 = pow(res, -1, int(self.resultadoFinal))
                                        print(f'EL RESULTADO FINAL ES {res2}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {res2}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeInverso = False
                                    if self.banderaSeno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Seno de {self.almacenoPrimeroNumero}\n')
                                        suSeno2 = math.sin(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suSeno2} en radianes\n')
                                        print('Su valor de Seno es:', suSeno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeSeno = False
                                    if self.banderaCoseno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Coseno de {self.almacenoPrimeroNumero}\n')
                                        suCoseno2 = math.cos(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suCoseno2} en radianes\n')
                                        print('Su valor de Coseno es:', suCoseno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeCoseno = False
                                    if self.banderaTangente == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Tangente de {self.almacenoPrimeroNumero}\n')
                                        suTangente2 = math.tan(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suTangente2} en radianes\n')
                                        print('Su valor de Tangente es:', suTangente2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeTangente = False
                                    if self.banderaNumeroSeModulo == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Modulo de {self.resultadoFinal} % {self.almacenoPrimeroNumero}\n')
                                        self.modulo2 = self.resultadoFinal % float(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.modulo2}\n')
                                        print('El Resultado de la MODULO es:', self.modulo2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeModulo = False

#TODO LAS OPERACIONES DE SENO

                            if self.banderaSeno == True:
                                if self.numeroEntrada == False:
                                    self.almacenoPrimeroNumero = float(self.primerNumeroSuma)
                                    my_text2.insert(END, f'\n\nSe sacará el Seno a: \n\n {self.almacenoPrimeroNumero}')
                                    print(f'Este es el numero a sacar seno {self.almacenoPrimeroNumero}')
                                    if self.resultadoFinal == False:
                                        self.resultadoFinal = self.almacenoPrimeroNumero
                                    suSeno = math.sin(self.almacenoPrimeroNumero)
                                    my_text2.insert(END, f' = {suSeno}')
                                    my_text2.insert(END, f'\n {suSeno} en Radianes\n')
                                    self.almacenoPrimeroNumero = suSeno
                                    self.almacenoValorSeno = suSeno
                                    print('Su valor de Seno es:', suSeno)
                                    self.primerNumeroSuma = ''
                                    self.numeroEntrada = True
                                    self.banderaNumeroSeSeno = True
                                    if self.banderaNumeroSeSuma == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal += self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeSuma = False
                                    if self.banderaNumeroSeResta == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} - {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal -= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeResta = False
                                    if self.banderaNumeroSeDivide == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} / {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero /= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeDivide = False
                                    if self.banderaNumeroSeMultiplica == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} * {self.resultadoFinal}\n')
                                        self.resultadoFinal *= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeMultiplica = False
                                    if self.banderaNumeroSeEleva == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} ^ {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero **= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeEleva = False
                                    if self.banderaNumeroSeRaiz == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        suRaiz2 = pow(self.resultadoFinal, 0.5) + self.almacenoPrimeroNumero
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suRaiz2}\n')
                                        print(f'EL RESULTADO FINAL ES {suRaiz2}')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeRaiz = False
                                    if self.banderaNumeroSeInverso == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} invert {self.almacenoPrimeroNumero}\n')
                                        res2 = pow(self.resultadoFinal, -1, int(self.almacenoPrimeroNumero))
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {res2}\n')
                                        print('El Resultado del Inverso es:', res2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeInverso = False
                                    if self.banderaSeno == True and self.contadorOperadorSeno > 2:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        suSeno2 = math.sin(suSeno)
                                        my_text2.insert(END, f'\n Se volverá a sacar el seno de {suSeno}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO ES = {suSeno2}')
                                        print('Su valor de Seno es:', suSeno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeSeno = False
                                    if self.banderaCoseno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Coseno de {self.almacenoPrimeroNumero}\n')
                                        suCoseno2 = math.cos(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suCoseno2} en radianes\n')
                                        print('Su valor de Coseno es:', suCoseno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeCoseno = False
                                    if self.banderaTangente == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Tangente de {self.almacenoPrimeroNumero}\n')
                                        suTangente2 = math.tan(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suTangente2} en radianes\n')
                                        print('Su valor de Tangente es:', suTangente2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeTangente = False
                                    if self.banderaNumeroSeModulo == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Modulo de {self.resultadoFinal} % {self.almacenoPrimeroNumero}\n')
                                        self.modulo2 = self.resultadoFinal % float(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.modulo2}\n')
                                        print('El Resultado de la MODULO es:', self.modulo2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeModulo = False
#TODO LAS OPERACIONES DE COSENO

                            if self.banderaCoseno == True:
                                if self.numeroEntrada == False:
                                    self.almacenoPrimeroNumero = float(self.primerNumeroSuma)
                                    my_text2.insert(END, f'\n\nSe sacará el Coseno a: \n\n {self.almacenoPrimeroNumero}')
                                    print(f'Este es el numero a sacar coseno {self.almacenoPrimeroNumero}')
                                    if self.resultadoFinal == False:
                                        self.resultadoFinal = self.almacenoPrimeroNumero
                                    suCoseno = math.cos(self.almacenoPrimeroNumero)
                                    my_text2.insert(END, f' = {suCoseno}')
                                    my_text2.insert(END, f'\n {suCoseno} en Radianes\n')
                                    self.almacenoPrimeroNumero = suCoseno
                                    print('Su valor de Coseno es:', suCoseno)
                                    self.primerNumeroSuma = ''
                                    self.numeroEntrada = True
                                    self.banderaNumeroSeCoseno = True
                                    if self.banderaNumeroSeSuma == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal += self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeSuma = False
                                    if self.banderaNumeroSeResta == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} - {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal -= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeResta = False
                                    if self.banderaNumeroSeDivide == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} / {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero /= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeDivide = False
                                    if self.banderaNumeroSeMultiplica == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} * {self.resultadoFinal}\n')
                                        self.resultadoFinal *= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeMultiplica = False
                                    if self.banderaNumeroSeEleva == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} ^ {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero **= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeEleva = False
                                    if self.banderaNumeroSeRaiz == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        suRaiz2 = pow(self.resultadoFinal, 0.5) + self.almacenoPrimeroNumero
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suRaiz2}\n')
                                        print(f'EL RESULTADO FINAL ES {suRaiz2}')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeRaiz = False
                                    if self.banderaNumeroSeInverso == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} invert {self.almacenoPrimeroNumero}\n')
                                        res2 = pow(self.resultadoFinal, -1, int(self.almacenoPrimeroNumero))
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {res2}\n')
                                        print('El Resultado del Inverso es:', res2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeInverso = False
                                    if self.banderaSeno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Seno de {self.almacenoPrimeroNumero}\n')
                                        suSeno2 = math.sin(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suSeno2} en radianes\n')
                                        print('Su valor de Seno es:', suSeno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeSeno = False
                                    if self.banderaCoseno == True and self.contadorOperadorCoseno > 2:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        suCoseno2 = math.cos(suCoseno)
                                        my_text2.insert(END, f'\n Se volverá a sacar el coseno de {suCoseno}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO ES = {suCoseno2}')
                                        print('Su valor de Seno es:', suCoseno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeCoseno = False
                                    if self.banderaTangente == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Tangente de {self.almacenoPrimeroNumero}\n')
                                        suTangente2 = math.tan(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suTangente2} en radianes\n')
                                        print('Su valor de Tangente es:', suTangente2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeTangente = False
                                    if self.banderaNumeroSeModulo == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Modulo de {self.resultadoFinal} % {self.almacenoPrimeroNumero}\n')
                                        self.modulo2 = self.resultadoFinal % float(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.modulo2}\n')
                                        print('El Resultado de la MODULO es:', self.modulo2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeModulo = False

#TODO LAS OPERACIONES DE TANGENTE

                            if self.banderaTangente == True:
                                if self.numeroEntrada == False:
                                    self.almacenoPrimeroNumero = float(self.primerNumeroSuma)
                                    my_text2.insert(END, f'\n\nSe sacará la Tangente a: \n\n {self.almacenoPrimeroNumero}')
                                    print(f'Este es el numero a sacar TANGENTE {self.almacenoPrimeroNumero}')
                                    if self.resultadoFinal == False:
                                        self.resultadoFinal = self.almacenoPrimeroNumero
                                    suTangente = math.tan(self.almacenoPrimeroNumero)
                                    my_text2.insert(END, f' = {suTangente}')
                                    my_text2.insert(END, f'\n {suTangente} en Radianes\n')
                                    self.almacenoPrimeroNumero = suTangente
                                    print('Su valor de Tangente es:', suTangente)
                                    self.primerNumeroSuma = ''
                                    self.numeroEntrada = True
                                    self.banderaNumeroSeTangente = True
                                    if self.banderaNumeroSeSuma == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal += self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeSuma = False
                                    if self.banderaNumeroSeResta == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} - {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal -= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeResta = False
                                    if self.banderaNumeroSeDivide == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} / {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero /= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeDivide = False
                                    if self.banderaNumeroSeMultiplica == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} * {self.resultadoFinal}\n')
                                        self.resultadoFinal *= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeMultiplica = False
                                    if self.banderaNumeroSeEleva == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} ^ {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero **= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeEleva = False
                                    if self.banderaNumeroSeRaiz == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        suRaiz2 = pow(self.resultadoFinal, 0.5) + self.almacenoPrimeroNumero
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suRaiz2}\n')
                                        print(f'EL RESULTADO FINAL ES {suRaiz2}')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeRaiz = False
                                    if self.banderaNumeroSeInverso == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} invert {self.almacenoPrimeroNumero}\n')
                                        res2 = pow(self.resultadoFinal, -1, int(self.almacenoPrimeroNumero))
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {res2}\n')
                                        print('El Resultado del Inverso es:', res2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeInverso = False
                                    if self.banderaSeno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Seno de {self.almacenoPrimeroNumero}\n')
                                        suSeno2 = math.sin(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suSeno2} en radianes\n')
                                        print('Su valor de Seno es:', suSeno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeSeno = False
                                    if self.banderaCoseno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Coseno de {self.almacenoPrimeroNumero}\n')
                                        suCoseno2 = math.cos(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suCoseno2} en radianes\n')
                                        print('Su valor de Coseno es:', suCoseno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeCoseno = False
                                    if self.banderaTangente == True and self.contadorOperadorTangete > 2:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n TANGENTE de {self.almacenoPrimeroNumero}\n')
                                        suTangente2 = math.tan(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suTangente2} en radianes\n')
                                        print('Su valor de tangente es:', suTangente2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeTangente = False
                                    if self.banderaNumeroSeModulo == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Modulo de {self.resultadoFinal} % {self.almacenoPrimeroNumero}\n')
                                        self.modulo2 = self.resultadoFinal % float(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.modulo2}\n')
                                        print('El Resultado de la MODULO es:', self.modulo2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeModulo = False

#TODO LAS OPERACIONES DE MODULO

                            if self.banderaModulo == True:
                                if self.numeroEntrada == False:
                                    self.almacenoPrimeroNumero = float(self.primerNumeroSuma)
                                    my_text2.insert(END, f'\n\nSe sacará Modulo a: \n\n {self.almacenoPrimeroNumero}')
                                    print(f'Este es el numero a Modular {self.almacenoPrimeroNumero}')
                                    if self.resultadoFinal == False:
                                        self.resultadoFinal = self.almacenoPrimeroNumero
                                    self.primerNumeroSuma = ''
                                    self.numeroEntrada = True
                                    self.banderaNumeroSeModulo = True

                                elif self.numeroEntrada == True:
                                    my_text2.insert(END, f' % {self.primerNumeroSuma}')
                                    self.modulo = self.almacenoPrimeroNumero % float(self.primerNumeroSuma)
                                    self.almacenoPrimeroNumero = self.modulo
                                    print('El Resultado de la MODULO es:', self.modulo)
                                    my_text2.insert(END, f' = {self.almacenoPrimeroNumero}')
                                    my_text2.insert(END, f'\n {self.almacenoPrimeroNumero}\n')
                                    self.primerNumeroSuma = ''
                                    if self.banderaNumeroSeSuma == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal += self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeSuma = False
                                    if self.banderaNumeroSeResta == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.resultadoFinal} - {self.almacenoPrimeroNumero}\n')
                                        self.resultadoFinal -= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeResta = False
                                    if self.banderaNumeroSeDivide == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} / {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero /= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeDivide = False
                                    if self.banderaNumeroSeMultiplica == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} * {self.resultadoFinal}\n')
                                        self.resultadoFinal *= self.almacenoPrimeroNumero
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.resultadoFinal}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeMultiplica = False
                                    if self.banderaNumeroSeEleva == True:
                                        my_text2.insert(END, f'\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} ^ {self.resultadoFinal}\n')
                                        self.almacenoPrimeroNumero **= self.resultadoFinal
                                        print(f'EL RESULTADO FINAL ES {self.resultadoFinal}')
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {self.almacenoPrimeroNumero}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeEleva = False
                                    if self.banderaNumeroSeRaiz == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} + {self.almacenoPrimeroNumero}\n')
                                        suRaiz2 = pow(self.resultadoFinal, 0.5) + self.almacenoPrimeroNumero
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suRaiz2}\n')
                                        print(f'EL RESULTADO FINAL ES {suRaiz2}')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.banderaNumeroSeRaiz = False
                                    if self.banderaNumeroSeInverso == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Raiz de {self.resultadoFinal} invert {self.almacenoPrimeroNumero}\n')
                                        res2 = pow(self.resultadoFinal, -1, int(self.almacenoPrimeroNumero))
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {res2}\n')
                                        print('El Resultado del Inverso es:', res2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeInverso = False
                                    if self.banderaSeno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Seno de {self.almacenoPrimeroNumero}\n')
                                        suSeno2 = math.sin(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suSeno2} en radianes\n')
                                        print('Su valor de Seno es:', suSeno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeSeno = False
                                    if self.banderaCoseno == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Coseno de {self.almacenoPrimeroNumero}\n')
                                        suCoseno2 = math.cos(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suCoseno2} en radianes\n')
                                        print('Su valor de Coseno es:', suCoseno2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeCoseno = False
                                    if self.banderaTangente == True:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n Tangente de {self.almacenoPrimeroNumero}\n')
                                        suTangente2 = math.tan(self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f'\n\n EL RESULTADO FINAL ES: {suTangente2} en radianes\n')
                                        print('Su valor de Tangente es:', suTangente2)
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1
                                        self.primerNumeroSuma = ''
                                        self.banderaNumeroSeTangente = False
                                    if self.banderaNumeroSeModulo == True and self.contadorOperadorModulo > 2:
                                        my_text2.insert(END, f'\n\n ¡Se detectó una Operacion Compleja!\n')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} % {self.resultadoFinal}\n')
                                        self.modulo2 = self.almacenoPrimeroNumero % float(self.resultadoFinal)
                                        print('El Resultado de la MODULO es:', self.modulo2)
                                        self.banderaNumeroSeModulo = False
                                        my_text2.insert(END, f'\n EL RESULTADO FINAL ES: {self.modulo2}\n')
                                        self.contadorOperadorSuma = 1
                                        self.contadorOperadorResta = 1
                                        self.contadorOperadorDivision = 1
                                        self.contadorOperadorPotencia = 1
                                        self.contadorOperadorRaiz = 1
                                        self.contadorOperadorInverso = 1
                                        self.contadorOperadorSeno = 1
                                        self.contadorOperadorCoseno = 1
                                        self.contadorOperadorTangete = 1
                                        self.contadorOperadorModulo = 1



                elif self.estado == 3:
                    if c.isdecimal():
                        self.primerNumeroSuma += c

                        print(f'Este es el numero {c}')
                        # self.primerNumeroSuma += c
                        print(self.primerNumeroSuma)
                        # self.numeroSuma1 = float(self.primerNumeroSuma)
                        # print(f'Almacenando el numero como flotante {self.numeroSuma1}')
                        juntar = ''
                        self.estado = 3


                    elif c == '.':
                        self.estado = 3
                        print('Esto es un punto')
                        print(juntar)
                        self.primerNumeroSuma += c

                        juntar = ''
                        # self.numeroSuma1 = float(self.primerNumeroSuma)
                        # print(f'Almacenando el numero como flotante {self.numeroSuma1}')
                    elif c == ' ':
                        print('Espacio Final de numeros')
                        juntar = ''
                        self.estado = 1

                elif self.estado == 4:
                    if str.isalpha(c):
                        self.estado = 4
                    elif c == '<':
                        self.estado = 4
                        print('Abriendo etiqueta')
                    elif c == '\n':
                        self.estado = 4
                        print('Salto de linea, se regrea a estado 4')
                    elif c == '.':
                        print(juntar)
                        print('Finaliza el texto')
                        # my_text2.insert(END, juntar)
                        self.textoGuardado = juntar
                        global textoGuardado
                        textoGuardado = self.textoGuardado
                        juntar = ''
                        self.estado = 1
                    elif c.isdecimal():
                        global tamanioFuenteTitulo
                        self.tamanioFuente += c
                        tamanioFuenteTitulo = self.tamanioFuente
                        juntar = ''

                    if juntar == '/>':
                        print('Cerrando parametros de estilo')
                        juntar = ''
                        self.tamanioFuente = ''
                        self.estado = 1

                    elif c == ' ':
                        # print(juntar)
                        # print('Espacio de Texto')
                        # juntar = ' '
                        self.estado = 4


                        if juntar == ' Operaciones ':
                            # print(juntar)
                            print('Titulo de OPERACIONES')
                            self.titulo = juntar
                            global titulo
                            titulo = self.titulo
                            # my_text2.insert(END, f'\n\n*************{juntar}*************\n\n')
                            juntar = ''
                            self.estado = 1
                        elif juntar == ' [TEXTO] ':
                            juntar = ''
                            self.estado = 1

                        elif juntar == ' [TIPO] ':
                            juntar = ''
                            self.estado = 1

                        elif juntar == '\n<Titulo ':
                            print('Estilo para titulo')
                            print(f'{juntar}')
                            juntar = ''
                            self.estado = 4

                    elif c == '=':
                        if juntar == 'Color=':
                            print('Seleccionando Color')
                            juntar = ''
                            self.estado = 4
                        elif juntar == ' Tamanio=':
                            print('Seleccionando tamaño de fuente')
                            juntar = ''
                            self.estado = 4


                    elif juntar == 'AZUL':
                        print(f'COLOR PARA TITULO {juntar}')
                        global colorTitulo
                        colorTitulo = '#0000FF'
                        juntar = ''
                        self.estado = 4

                    # elif juntar == 'NEGRO':
                    #     print(f'COLOR PARA TITULO {juntar}')
                    #     global colorTitulo
                    #     colorTitulo = '#000000'
                    #     juntar = ''
                    #     self.estado = 4
                    #
                    # elif juntar == 'ROJO':
                    #     print(f'COLOR PARA TITULO {juntar}')
                    #     global colorTitulo
                    #     colorTitulo = '#FF0000'
                    #     juntar = ''
                    #     self.estado = 4
                    #
                    # elif juntar == 'AMARRILLO':
                    #     print(f'COLOR PARA TITULO {juntar}')
                    #     global colorTitulo
                    #     colorTitulo = '#FFFF00'
                    #     juntar = ''
                    #     self.estado = 4
                    #
                    # elif juntar == 'VERDE':
                    #     print(f'COLOR PARA TITULO {juntar}')
                    #     global colorTitulo
                    #     colorTitulo = '#008000'
                    #     juntar = ''
                    #     self.estado = 4
                    #
                    # elif juntar == 'VERDE':
                    #     print(f'COLOR PARA TITULO {juntar}')
                    #     global colorTitulo
                    #     colorTitulo = '#800080'
                    #     juntar = ''
                    #     self.estado = 4



                    elif juntar == '\n<Funcion = ESCRIBIR>':
                        # print(juntar)
                        print('Esta es una funcion ESCRIBIR')
                        juntar = ''
                        self.estado = 1


                if not c:
                    print("End of file")
                    print(juntar)
                    break
                # print("Read a character:", c)

    # except IOError:
    #     messagebox.showerror('ERROR', 'ERROR EN LA CARGA DEL ARCHIVO')


    def Guardar(self):
        text_file = open(guardarArchivo, 'w', encoding='utf-8')
        text_file.write(my_text.get(1.0, END))

    def Guardar2(self):
        text_file2 = open('Texto_para_HTML.txt', 'w', encoding='utf-8')
        text_file2.write(my_text2.get(1.0, END))

    def GenerarHTML(self):
        global titulo
        global textoGuardado
        global colorTitulo
        global tamanioFuenteTitulo
        fichero = open('Texto_para_HTML.txt', encoding='utf-8')
        Linea = ""
        htmlparte1 = "<html><head><title>"
        htmlparte2 = "</title></head><body>"
        htmlh1 = '<h3>'
        htmlh2C = "</h3>"
        # <h1 style="color:red;font-size:40px;">
        htmlh3 = '<h1 style="color:'
        tamaFuente = ";font-size: "
        finaFuente = 'px;">'
        htmlh3C = "</h1>"
        iniParrafo = "<p>"
        cerraParrafo = "</p>"
        htmlparte3 = "</body></html>"


        documentohtml = ""
        lineas = fichero.readlines()
        documentohtml += htmlparte1
        documentohtml += titulo
        documentohtml += htmlparte2
        documentohtml += htmlh3
        documentohtml += colorTitulo
        documentohtml += tamaFuente
        documentohtml += tamanioFuenteTitulo
        documentohtml += finaFuente
        documentohtml += titulo
        documentohtml += htmlh3C
        documentohtml += htmlh1
        documentohtml += textoGuardado
        documentohtml += htmlh2C
        documentohtml += iniParrafo
        for Linea in lineas:
            documentohtml += Linea
            documentohtml += '<br>'
            print(Linea)
        documentohtml += cerraParrafo
        documentohtml += htmlparte3
        f = open('PaginaDinamica.html', 'w')
        f.write(documentohtml)

    def main(self):
        menu = Principal()
        # menu.mainMenu()
        root = Tk()
        abrir = Principal()
        analizar = Principal()
        # abrir.Abrir()
        guardar1 = Principal()
        guardar2 = Principal()
        generar = Principal()

        wrapper1 = LabelFrame(root, text="Mostrando archivo de texto leido")
        wrapper2 = LabelFrame(root, text="Acciones")
        wrapper3 = LabelFrame(root, text="Mostrando resultado de operaciones")

        wrapper1.pack(fill="both", expand="yes", side="left", padx=20, pady=20)
        wrapper2.pack(fill="both", expand="no", side="left", padx=20, pady=195)
        wrapper3.pack(fill="both", expand="yes", side="left", padx=20, pady=20)

        my_text = Text(wrapper1, width=50, height=40, font=("Helvetica", 12))
        my_text.pack(pady=20)

        my_text.insert(END, guardarArchivo)

        btnAbrir = Button(wrapper2, text="  Abrir Archivo", bg='green3', command=abrir.Abrir)
        btnAbrir.pack(side=tk.TOP, padx=6, pady=15)
        btnGuardar = Button(wrapper2, text="Guardar Cambios", bg='#856ff8', command=guardar1.Guardar)
        btnGuardar.pack(side=tk.TOP, padx=6, pady=15)
        btnAnalizar = Button(wrapper2, text="Analizar Archivo", bg='orange2', command=analizar.lecturaPrueba2)
        btnAnalizar.pack(side=tk.TOP, padx=6, pady=15)
        btnErrores = Button(wrapper2, text=" Guardar texto HTML ", bg='red2', command=guardar2.Guardar2)
        btnErrores.pack(side=tk.TOP, padx=6, pady=15)
        btnSalir = Button(wrapper2, text="Generar HTML", bg='yellow2', command=generar.GenerarHTML)
        btnSalir.pack(side=tk.TOP, padx=6, pady=15)


        # lbl = Label(wrapper2, text="Eliminar curso por codigo")
        # lbl.pack(side=tk.LEFT, padx=10)


        my_text2 = Text(wrapper3, width=50, height=40, font=("Helvetica", 12))
        my_text2.pack(pady=20)
        root.title("Ventana Principal Diego Barrios 20190018 LFP A+")
        root.geometry("1300x700")
        root.mainloop()

        # prueba = Principal()
        # prueba.lecturaPrueba2()


menu = Principal()
        # menu.mainMenu()
root = Tk()
abrir = Principal()
analizar = Principal()
guardar = Principal()
guardar2 = Principal()
html = Principal()
        # abrir.Abrir()

wrapper1 = LabelFrame(root, text="Mostrando archivo de texto leido")
wrapper2 = LabelFrame(root, text="Acciones")
wrapper3 = LabelFrame(root, text="Mostrando resultado de operaciones")

wrapper1.pack(fill="both", expand="yes", side="left", padx=20, pady=20)
wrapper2.pack(fill="both", expand="no", side="left", padx=20, pady=195)
wrapper3.pack(fill="both", expand="yes", side="left", padx=20, pady=20)

my_text = Text(wrapper1, width=60, height=40, font=("Helvetica", 12))
my_text.pack(pady=20)

my_text2 = Text(wrapper3, width=60, height=40, font=("Helvetica", 12))
my_text2.pack(pady=20)
btnAbrir = Button(wrapper2, text="  Abrir Archivo  ", bg='green3', command=abrir.Abrir)
btnAbrir.pack(side=tk.TOP, padx=6, pady=15)
btnGuardar = Button(wrapper2, text="Guardar cambios", bg='#856ff8', command=guardar.Guardar)
btnGuardar.pack(side=tk.TOP, padx=6, pady=15)
btnAnalizar = Button(wrapper2, text="Analizar Archivo", bg='orange2', command=analizar.lecturaPrueba2)
btnAnalizar.pack(side=tk.TOP, padx=6, pady=15)
btnErrores = Button(wrapper2, text="Guardar texto para HTML", bg='red2', command=guardar2.Guardar2)
btnErrores.pack(side=tk.TOP, padx=6, pady=15)
btnSalir = Button(wrapper2, text="Generar HTML", bg='yellow2', command=html.GenerarHTML)
btnSalir.pack(side=tk.TOP, padx=6, pady=15)


root.title("Ventana Principal Diego Barrios 20190018 LFP A+")
root.geometry("1300x700")
root.mainloop()

        # prueba = Principal()
        # prueba.lecturaPrueba2()

# if __name__ == "__main__":
#     main()
