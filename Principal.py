import math
import os
from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox
import traceback
import linecache
import sys
from tkinter.filedialog import asksaveasfilename

from VentanaDatos import VentanaDatos

guardarArchivo = ''
titulo = ''
textoGuardado = ''
colorTitulo = ''
tamanioFuenteTitulo = ''
tamanioFuenteDescripcion = ''
tamanioFuenteContenido = ''
colorDescripcion = ''
colorContenido = ''
tamanioDescripcion = ''
errorDivison = ''
errorDivisonCompleja = ''
errores = ''


class Principal(VentanaDatos):
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
        self.banderaColorTitulo = False
        self.banderaTamanioTitulo = False
        self.banderaColorDescripcion = False
        self.banderaTamanioDescripcion = False
        self.banderaColorContenido = False
        self.banderaTamanioContenido = False
        self.banderaOperacionAbierta = False

    #Reinicia contadores de las operaciones para poder ejecutar sin limites
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

        self.banderaOperacionCerrada = False
    #Abre el archivo txt para su lectura
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

    #Automata
    def lecturaPrueba2(self):
        try:
            with open(guardarArchivo, encoding="utf8") as f:

                juntar = ''
                juntarTodo = ''
                contadorCarracteres = 0
                contadorSaltos = 1
                while True:
                    c = f.read(1)
                    contadorCarracteres += 1
                    juntar += c
                    juntarSinSaltos = juntar
                    juntarTodo += c

                    # print(f.readline())
                    if self.estado == 1:
                        if c == '<':
                            self.estado = 2
                            print('Abriendo etiqueta')
                        elif c == '\n':
                            self.estado = 1
                            contadorSaltos += 1
                            print('Salto de linea, se regrea a estado 1')
                        elif c == ' ':
                            print('Esto es un espacio de los numeros')
                            self.estado = 3
                        elif c == '/':
                            print('Cerrando etiqueta')
                            # break
                        elif c == '\t':
                            print('tabulacion')
                            # break
                        elif c.isdigit():
                            print(f'??Error! se ha encontrado que "{c}" no corresponde a la lectura de una etiqueta')
                            global errores
                            errores = f'??Error Lexico! se ha encontrado que "{c}" no corresponde a la lectura de una etiqueta. En el carracter {contadorCarracteres} en la linea {contadorSaltos}'
                            print(f'En el carracter {contadorCarracteres} en la linea {contadorSaltos}')
                            messagebox.showerror('ERROR LEXICO',
                                                 'Posiblemente se deba a un error en la escritura de una etiqueta, verifique su archivo')
                            break
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
                        # elif c.isdigit():
                        #     print(f'??Error! se ha encontrado que "{c}" no corresponde a la lectura de una etiqueta')
                        #     # global errores
                        #     errores = f'??Error! se ha encontrado que "{c}" no corresponde a la lectura de una etiqueta. En el carracter {contadorCarracteres} en la linea {contadorSaltos}'
                        #     print(f'En el carracter {contadorCarracteres} en la linea {contadorSaltos}')
                        #     break

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

                            elif juntar == '\n\t<Titulo>':
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

                            elif juntar == '\n\t<Descripcion>':
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

                            elif juntar == '\n\t<Contenido>':
                                print('Esto es una etiqueta CONTENIDO')
                                print(juntar)
                                print(f'Creando archivo de texto donde se guardar??n las operaciones')
                                # my_text2.insert(END, juntar)
                                juntar = ''
                                self.estado = 4

                            elif juntar == '</Contenido>':
                                print('Esto es una etiqueta CONTENIDO')
                                print(juntar)
                                print(f'Finaliza etiqueta Contenido')
                                juntar = ''
                                self.estado = 1

                            elif juntar == '\n<Estilo>':
                                print('Esta es un Estilo')
                                print(f'{juntar}')
                                juntar = ''
                                self.estado = 4

                            elif c.isdigit():
                                print(f'??Error Lexico! se ha encontrado')
                                errores = f'??Error! se ha encontrado un error de escritura en alguna etiqueta. Revisar en el carracter {contadorCarracteres} en la linea {contadorSaltos}'
                                print(f'En el carracter {contadorCarracteres} en la linea {contadorSaltos}')
                                messagebox.showerror('ERROR LEXICO',
                                                     'Posiblemente se deba a un error en la escritura de una etiqueta, verifique su archivo')
                                break

                            elif juntar == '\n\t<Operacion=':
                                print('Esto es una Operacion')
                                print(juntar)
                                juntar = ''
                                self.numeroEntrada = False
                                my_text2.insert(END, '\n----------------------Se Realizar?? una Operaci??n----------------------')
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

                            elif juntar == '\n\t</Operacion>':
                                print('Finaliza una operacion')
                                print(juntar)
                                juntar = ''
                                self.estado = 1
                                self.resultadoFinal = 0
                                self.contadorOperador = 0
                                my_text2.insert(END, '\n----------------------Se Finaliz?? una Operaci??n--------------------------\n')
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
                                # my_text2.insert(END, '\nSe Realizara una Multiplicaci??n')

                            elif juntar == 'DIVISION>':
                                print('Esto es una DIVISION')
                                juntar = ''
                                self.banderaDivision = True
                                self.contadorOperadorDivision += 1
                                # my_text2.insert(END, '\nSe Realizar?? una Divisi??n')

                            elif juntar == 'POTENCIA>':
                                print('Esto es una POTENCIA')
                                juntar = ''
                                self.banderaPotencia = True
                                self.contadorOperadorPotencia += 1
                                # my_text2.insert(END, '\nSe Realizar?? una Potencia')

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

                            elif juntar == '\n\t\t<Numero>':
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
                                my_text2.insert(END, '\nFinaliz?? la lectura')
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
                                        my_text2.insert(END, f'\n\nSe sumar??n: \n\n {self.almacenoPrimeroNumero}')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            global errorDivisonCompleja
                                            global errorDivison
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\nSe Restar??n: \n\n {self.almacenoPrimeroNumero}')
                                        print(f'Este es el primer numero a restar {self.almacenoPrimeroNumero}')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            if self.resultadoFinal == '0' or 0:
                                                print('Se quizo dividir entre 0, el programa se cerr??')
                                                break
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
                                            my_text2.insert(END, f'\n {self.almacenoPrimeroNumero} / {self.resultadoFinal}\n')
                                            self.almacenoPrimeroNumero /= self.resultadoFinal
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
                                            self.banderaNumeroSeDivide = False
                                        if self.banderaNumeroSeMultiplica == True:
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\nSe Multiplicar??n: \n\n {self.almacenoPrimeroNumero}')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\nSe Dividir??n: \n\n {self.almacenoPrimeroNumero}')
                                        print(f'Este es el primero numero a dividir {self.almacenoPrimeroNumero}\n')
                                        if self.resultadoFinal == False:
                                            self.resultadoFinal = self.almacenoPrimeroNumero
                                        self.primerNumeroSuma = ''
                                        self.numeroEntrada = True
                                        self.banderaNumeroSeDivide = True

                                    elif self.numeroEntrada == True:
                                        my_text2.insert(END, f' / {self.primerNumeroSuma}')

                                        try:
                                            self.almacenoPrimeroNumero /= float(self.primerNumeroSuma)
                                        except ZeroDivisionError:
                                            global errorDivisonCompleja
                                            global errorDivison
                                            print(traceback.format_exc())
                                            errorDivison = traceback.format_exc()

                                        print('El Resultado de la DIVISION es:', self.almacenoPrimeroNumero)
                                        my_text2.insert(END, f' = {self.almacenoPrimeroNumero}')
                                        my_text2.insert(END, f'\n {self.almacenoPrimeroNumero}\n')
                                        self.primerNumeroSuma = ''
                                        if self.banderaNumeroSeSuma == True:
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
                                            my_text2.insert(END, f'\n {self.resultadoFinal} / {self.almacenoPrimeroNumero}\n')
                                            try:
                                                self.almacenoPrimeroNumero /= self.resultadoFinal
                                            except ZeroDivisionError:
                                                print(traceback.format_exc())
                                                errorDivisonCompleja = traceback.format_exc()
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
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\nSe Potenciar??: \n\n {self.almacenoPrimeroNumero}')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\nSe Sacar?? Ra??z: \n\n Ra??z de {self.almacenoPrimeroNumero}')
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
                                        my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\nSe Invertir??: \n\n {self.almacenoPrimeroNumero}')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\nSe sacar?? el Seno a: \n\n {self.almacenoPrimeroNumero}')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
                                            suSeno2 = math.sin(suSeno)
                                            my_text2.insert(END, f'\n Se volver?? a sacar el seno de {suSeno}')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\nSe sacar?? el Coseno a: \n\n {self.almacenoPrimeroNumero}')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
                                            suCoseno2 = math.cos(suCoseno)
                                            my_text2.insert(END, f'\n Se volver?? a sacar el coseno de {suCoseno}')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\nSe sacar?? la Tangente a: \n\n {self.almacenoPrimeroNumero}')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                        my_text2.insert(END, f'\n\nSe sacar?? Modulo a: \n\n {self.almacenoPrimeroNumero}')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                                            my_text2.insert(END, f'\n\n ??Se detect?? una Operacion Compleja!\n')
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
                            if self.banderaOperacionAbierta == True:
                                print('Error de escritura')
                                break


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

                        else:
                            errores = f'??Error Lexico! se ha encontrado que "{c}" no corresponde a la lectura correcta del archivo. En el carracter {contadorCarracteres} en la linea {contadorSaltos}'
                            print(f'En el carracter {c} {contadorCarracteres} en la linea {contadorSaltos}')
                            messagebox.showerror('ERROR LEXICO', 'Posiblemente se deba a un error en la escritura de un numero, verifique su archivo y reinicie el programa')
                            break

                    elif self.estado == 4:
                        if str.isalpha(c):
                            self.estado = 4
                        elif c == '<':
                            self.estado = 4
                            print('Abriendo etiqueta')
                        elif c == '\n':
                            contadorSaltos += 1
                            self.estado = 4
                            print('Salto de linea, se regrea a estado 4')
                        elif c == '\t':
                            print('tabulacion')
                            self.estado = 4
                        elif c == '.':
                            print(juntar)
                            print('Finaliza el texto')
                            # my_text2.insert(END, juntar)
                            self.textoGuardado = juntar
                            global textoGuardado
                            textoGuardado = self.textoGuardado
                            juntar = ''
                            self.tamanioFuente = ''
                            self.estado = 1
                        elif c.isdecimal():
                            global tamanioFuenteTitulo
                            global tamanioFuenteDescripcion
                            global tamanioFuenteContenido
                            self.tamanioFuente += c

                            if self.banderaTamanioTitulo == True:
                                tamanioFuenteTitulo = self.tamanioFuente
                                juntar = ''

                            elif self.banderaTamanioDescripcion == True:
                                tamanioFuenteDescripcion = self.tamanioFuente
                                juntar = ''

                            elif self.banderaTamanioContenido == True:
                                tamanioFuenteContenido = self.tamanioFuente
                                juntar = ''
                                # self.estado = 1

                                # self.banderaTamanioContenido = True

                        if juntar == '/>':
                            print('Cerrando parametros de estilo')
                            juntar = ''
                            self.tamanioFuente = ''
                            self.estado = 4
                            self.banderaTamanioTitulo = False
                            self.banderaTamanioDescripcion = False
                            self.banderaTamanioContenido = False
                            self.banderaColorContenido = False
                            self.banderaColorDescripcion = False
                            self.banderaColorTitulo = False


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

                            elif juntar == '\n\t\t<Titulo ':
                                print('Estilo para titulo')
                                print(f'{juntar}')
                                juntar = ''
                                self.banderaTamanioTitulo = True
                                self.banderaColorTitulo = True
                                contadorSaltos += 1
                                self.estado = 4

                            elif juntar == '\n\t\t<Descripcion ':
                                print('Estilo para Descripcion')
                                print(f'{juntar}')
                                juntar = ''
                                self.banderaTamanioDescripcion = True
                                self.banderaColorDescripcion = True
                                contadorSaltos += 1
                                self.estado = 4

                            elif juntar == '\n\t\t<Contenido ':
                                print('Estilo para Descripcion')
                                print(f'{juntar}')
                                juntar = ''
                                self.banderaTamanioContenido = True
                                self.banderaColorContenido = True
                                contadorSaltos += 1
                                self.estado = 4



                        elif c == '=':
                            if juntar == 'Color=':
                                print('Seleccionando Color')
                                juntar = ''
                                self.estado = 4
                            elif juntar == ' Tamanio=':
                                print('Seleccionando tama??o de fuente')
                                juntar = ''
                                self.estado = 4


                        elif juntar == '\n</Estilo>':

                            print('Finaliza la seleccion de estilos')
                            print(f'{juntar}')
                            juntar = ''
                            self.estado = 1

                        elif juntar == 'AZUL':
                            print(f'COLOR Ser?? {juntar}')
                            global colorTitulo
                            global colorDescripcion
                            global colorContenido
                            if self.banderaColorTitulo == True:
                                colorTitulo = '#0000FF'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorTitulo = False

                            elif self.banderaColorDescripcion == True:
                                colorDescripcion = '#0000FF'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorDescripcion = False

                            elif self.banderaColorContenido == True:
                                colorContenido = '#0000FF'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorContennido = False

                        elif juntar == 'NEGRO':
                            print(f'COLOR PARA TITULO {juntar}')
                            # colorTitulo = '#000000'
                            if self.banderaColorTitulo == False:
                                colorTitulo = '#000000'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorTitulo = True

                            elif self.banderaColorDescripcion == False:
                                colorDescripcion = '#000000'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorDescripcion = True

                            elif self.banderaColorContenido == False:
                                colorContenido = '#000000'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorContennido = True

                        elif juntar == 'ROJO':
                            print(f'COLOR PARA TITULO {juntar}')
                            # colorTitulo = '#FF0000'
                            if self.banderaColorTitulo == True:
                                colorTitulo = '#FF0000'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorTitulo = False

                            elif self.banderaColorDescripcion == True:
                                colorDescripcion = '#FF0000'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorDescripcion = False

                            elif self.banderaColorContenido == True:
                                colorContenido = '#FF0000'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorContennido = False
                        #
                        elif juntar == 'AMARRILLO':
                            print(f'COLOR PARA TITULO {juntar}')
                            # colorTitulo = '#FFFF00'
                            if self.banderaColorTitulo == True:
                                colorTitulo = '#FFFF00'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorTitulo = False

                            elif self.banderaColorDescripcion == True:
                                colorDescripcion = '#FFFF00'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorDescripcion = False

                            elif self.banderaColorContenido == True:
                                colorContenido = '#FFFF00'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorContennido = False
                        #
                        elif juntar == 'VERDE':
                            print(f'COLOR PARA TITULO {juntar}')
                            # colorTitulo = '#008000'
                            if self.banderaColorTitulo == True:
                                colorTitulo = '#008000'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorTitulo = False

                            elif self.banderaColorDescripcion == True:
                                colorDescripcion = '#008000'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorDescripcion = False

                            elif self.banderaColorContenido == True:
                                colorContenido = '#008000'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorContennido = False
                        #
                        elif juntar == 'NARANJA':
                            print(f'COLOR PARA TITULO {juntar}')
                            # colorTitulo = '#ff8000'
                            if self.banderaColorTitulo == True:
                                colorTitulo = '#ff8000'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorTitulo = False

                            elif self.banderaColorDescripcion == True:
                                colorDescripcion = '#ff8000'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorDescripcion = False

                            elif self.banderaColorContenido == True:
                                colorContenido = '#ff8000'
                                juntar = ''
                                self.estado = 4
                                self.banderaColorContennido = False



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
        except IOError:
            messagebox.showerror('ERROR', 'Seleccione primero el archivo a analizar')
    # except IOError:
    #     messagebox.showerror('ERROR', 'ERROR EN LA CARGA DEL ARCHIVO')

    #Guarda los cambios efectuados en el archivo txt leido dentro del programa
    def Guardar(self):
        try:
            text_file = open(guardarArchivo, 'w', encoding='utf-8')
            text_file.write(my_text.get(1.0, END))
            messagebox.showinfo('Guardar Cambios', '??Se guardaron los cambios!')
        except IOError:
            messagebox.showerror('ERROR', 'No hay archivo seleccionado')
    #Guarda los datos del textbox derecho en un archivo txt nuevo para poder generar el HTML
    def Guardar2(self):
        messagebox.showinfo('Guardar Texto para HTML', '??Se guardaron con exito los datos en archivo txt!\nGenere su HTML')
        text_file2 = open('Texto_para_HTML.txt', 'w', encoding='utf-8')
        text_file2.write(my_text2.get(1.0, END))
    #Impresion de errores
    def PrintException(self):
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

    #Genera el HTML en la carpeta del proyecto
    def GenerarHTML(self):
        global titulo
        global textoGuardado
        global colorTitulo
        global tamanioFuenteTitulo
        global tamanioFuenteDescripcion
        global tamanioFuenteContenido
        global colorDescripcion
        global colorContenido
        global errorDivison
        global errorDivisonCompleja
        global errores

        fichero = open('Texto_para_HTML.txt', encoding='utf-8')
        Linea = ""
        htmlparte1 = "<html><head><title>"
        htmlparte2 = "</title></head><body>"
        htmlh1 = '<h3 style="color:'
        htmlh2C = "</h3>"
        # <h1 style="color:red;font-size:40px;">
        htmlh3 = '<h1 style="color:'
        tamaFuente = ";font-size: "
        tamaFuenteDes = ";font-size: "
        tamaFuenteCon = ";font-size: "
        finaFuente = 'px;">'
        finaDescripcion = 'px;">'
        finaContenido = 'px;">'
        htmlh3C = "</h1>"
        iniParrafo = '<p style="color:'
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
        documentohtml += str(tamanioFuenteTitulo)
        documentohtml += finaFuente
        documentohtml += titulo
        documentohtml += htmlh3C
        documentohtml += htmlh1
        documentohtml += colorDescripcion
        documentohtml += tamaFuenteDes
        documentohtml += tamanioFuenteDescripcion
        documentohtml += finaDescripcion
        documentohtml += textoGuardado
        documentohtml += htmlh2C
        documentohtml += iniParrafo
        documentohtml += colorContenido
        documentohtml += tamaFuenteCon
        documentohtml += str(tamanioFuenteContenido)
        documentohtml += finaContenido
        for Linea in lineas:
            documentohtml += Linea
            documentohtml += '<br>'
            print(Linea)
        documentohtml += cerraParrafo
        documentohtml += '<p style="color:red;font-size:40px;">'
        documentohtml += 'ERRORES:'
        documentohtml += '</p>'
        documentohtml += '<br>'
        documentohtml += errorDivisonCompleja
        documentohtml += '<br>'
        documentohtml += errorDivison
        documentohtml += '<br>'
        documentohtml += errores
        documentohtml += htmlparte3
        f = open('PaginaDinamica.html', 'w')
        f.write(documentohtml)
        messagebox.showinfo('Generar HTML', '??Se gener?? el HTML con exito!')

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

    #Crea una nueva ventana con los datos de la clase VentanaDatos
    def nuevaVentana(self):
        datos = VentanaDatos('Diego Alejandro', 'Barrios Gomez', '201900158', 'Proyecto #2', '25/09/2022', 'Guatemala', 'Desarrollado',
                             '343')
        nueva_ventana = Toplevel(root)
        nueva_ventana.geometry("500x500")
        nueva_ventana.title("Informaci??n")
        nueva_ventana.resizable(False, False)
        wrapper4 = LabelFrame(nueva_ventana, text="Acerca del Desarrollador")
        wrapper4.pack(fill="both", expand="yes", padx=20, pady=10)
        # lbl = Label(wrapper4, text="Contacto")
        # lbl.grid(row=0, column=0, padx=5, pady=3)
        my_text3 = Text(wrapper4, width=50, height=30, font=("Helvetica", 12))
        my_text3.pack(pady=5)
        my_text3.insert(END,f' Desarrollado por: \n\n\t {datos.nombre} {datos.apellidos}\n\n Carnet: \n\t{datos.carnet}\n\n {datos.proyecto}: \n\tLenguajes Formales de Programaci??n\n\n Fecha: \n\t{datos.fecha}\n\n Lugar:\n \tGuatemala/Guatemala\n\n\n\t\t Informacion de Contacto\n\n Correo: dialejandrobarriosg@gmail.com\n\n Linkedin: https://www.linkedin.com/in/diegoa-barriosg/ \n\n GitHub: https://github.com/DiAlejandroBarriosg' )



        # btn = Button(wrapper4, text="buscar", command=conseguirCreditos)
        # btn.pack(side=tk.LEFT, padx=6)

menu = Principal()
        # menu.mainMenu()
root = Tk()
abrir = Principal()
analizar = Principal()
guardar = Principal()
guardar2 = Principal()
html = Principal()
ventana = Principal()
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
btnVentana = Button(wrapper2, text="       Ayuda       ", bg='blue2', command=ventana.nuevaVentana)
btnVentana.pack(side=tk.TOP, padx=6, pady=15)




root.title("Ventana Principal Diego Barrios 20190018 LFP A+")
root.geometry("1300x750")
root.mainloop()

        # prueba = Principal()
        # prueba.lecturaPrueba2()

# if __name__ == "__main__":
#     main()
