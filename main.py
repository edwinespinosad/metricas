import sqlite3
from sqlite3 import Error
import math
from pathlib import Path
from kivymd.uix import screen
from plyer import filechooser
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen, Screen
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
global Cod, n1, n2, eN1, eN2, NN, nn, V, D, L, E, T, B


class new(MDApp):
    def file_chooser(self, args):
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        if selection:
            url = selection[0]
            ext = url.split(".")
            if ext[1] == "py":
                print(url.split("."))
                texto = AbrirArch(url)
            else:
                self.label.text += "Archivo no aceptado"

    def mostrar(self, args):
        conn = crearBase()
        cursor = conn.cursor()
        sentencia = "SELECT * FROM MetricasApp;"
        cursor.execute(sentencia)
        Metricas = cursor.fetchall()
        cadenaF = "+{:-<13}+{:-<8}+{:-<8}+{:-<8}+{:-<8}+{:-<8}+{:-<8}+{:-<8}+{:-<8}+{:-<8}+{:-<10}+{:-<10}+{:-<8}+".format(
            '', "", "", "", "", "", "", "", "", "", "", "", "")+"\n"
        cadenaF += "|{:^10}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{:^10}|{:^10}|{:^8}|".format(
            "Código", "n1", "n2", "N1", "N2", "N", "n", "V", "D", "L", "E", "T", "B")
        cadenaF += "+{:-<13}+{:-<8}+{:-<8}+{:-<8}+{:-<8}+{:-<8}+{:-<8}+{:-<8}+{:-<8}+{:-<8}+{:-<10}+{:-<10}+{:-<8}+".format(
            "", "", "", "", "", "", "", "", "", "", "", "", "") + "\n"
        
        for codigo, n1, n2, N3, N4, N5, n, V, D, L, E, T, B in Metricas:
            cadenaF += "|{:^10}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{:^10}|{:^10}|{:^8}|".format(
                codigo, n1, n2, N3, N4, N5, n, V, D, L, E, T, B) + "\n"
            print("|{:^10}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{:^8}|{:^10}|{:^10}|{:^8}|".format(
                codigo, n1, n2, N3, N4, N5, n, V, D, L, E, T, B))

        # self.label.text = str(cadenaF)
        return Metricas

    def mosTabla(self, args):
        datos = self.mostrar(args)

        tabla = MDDataTable(
            size_hint=(0.9, 0.6),
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            use_pagination=True,
            column_data=[
                ("Codigo", dp(20)),
                ("n1", dp(20)),
                ("n2", dp(20)),
                ("N1", dp(20)),
                ("N2", dp(20)),
                ("N", dp(20)),
                ("n", dp(20)),
                ("V", dp(20)),
                ("D", dp(20)),
                ("L", dp(20)),
                ("E", dp(20)),
                ("T", dp(20)),
                ("B", dp(20)),
            ],
            row_data=[
                (
                    # "[color=#297B50]1[/color]",
                    # "[color=#C552A1]2[/color]",
                    # "[color=#297B50]1[/color]",
                    # "[color=#C552A1]2[/color]",
                    # "[color=#297B50]1[/color]",
                    # "[color=#C552A1]2[/color]",
                    # "[color=#297B50]1[/color]",
                    # "[color=#C552A1]2[/color]",
                    # "[color=#297B50]1[/color]",
                    # "[color=#C552A1]2[/color]",
                    # "[color=#297B50]1[/color]",
                    # "[color=#C552A1]2[/color]",
                    # "[color=#297B50]1[/color]",
                ), (
                    # "[color=#C552A1]2[/color]",
                    # "[color=#C552A1]2[/color]",
                    # "[color=#297B50]1[/color]",
                    # "[color=#C552A1]2[/color]",
                    # "[color=#297B50]1[/color]",
                    # "[color=#C552A1]2[/color]",
                    # "[color=#297B50]1[/color]",
                    # "[color=#C552A1]2[/color]",
                    # "[color=#297B50]1[/color]",
                    # "[color=#C552A1]2[/color]",
                    # "[color=#297B50]1[/color]",
                    # "[color=#C552A1]2[/color]",
                    # "[color=#297B50]1[/color]",
                )
            ],
        )
        i = 0
        for dato in datos:
            tabla.row_data.insert(i, dato)
            i = i+1
        screen.add_widget(tabla)

    def build(self):
        conn = crearBase()
        self.theme_cls.primary_palette = "BlueGray"
        global screen
        screen = MDScreen()

        self.toolbar = MDToolbar(title="Metricas de Software")
        self.toolbar.pos_hint = {"top": 1}
        screen.add_widget(self.toolbar)

        self.label = MDLabel(
            halign="center",
            pos_hint={'center_x': .5, 'center_y': .7},
        )

        screen.add_widget(MDRaisedButton(
            text="Cargar Archivo",
            pos_hint={'center_x': .4, 'top': .85},
            on_press=self.file_chooser
        ))

        screen.add_widget(MDRaisedButton(
            text="Mostrar Datos",
            pos_hint={'center_x': .6, 'top': .85},
            # on_press=self.mostrar,
            on_press=self.mosTabla
        ))

        screen.add_widget(self.label)
        return screen


def AbrirArch(url):
    global Cod, n1, n2, eN1, eN2, NN, nn, V, D, L, E, T, B

    n1 = 1
    n2 = 1
    eN1 = 1
    eN2 = 1
    NN = 0
    nn = 0
    V = 0
    D = 0
    L = 0
    E = 0
    T = 0
    B = 0

    tClas = 0
    tOr = 0
    tCont = 0
    tImp = 0
    tFin = 0
    tIn = 0
    tPrint = 0
    tFalse = 0
    tTrue = 0
    tNone = 0
    tFile = 0
    tTry = 0
    tNot = 0
    tBreak = 0
    tElif = 0
    tElse = 0
    tIs = 0
    tMenIgual = 0
    tMIgual = 0
    tPot = 0
    tDifQ = 0
    tAnd = 0
    tFor = 0
    tDef = 0
    tDP = 0
    tIgual = 0
    tModulo = 0
    tWhile = 0
    tMQ = 0
    tMas = 0
    tMenos = 0
    tPor = 0
    tDiv = 0
    tComa = 0
    tPA = 0
    tMenorQ = 0
    tCA = 0
    tIf = 0

    path = url   # devuelve la ruta del archivo
    Cod = Path(path).resolve().stem
    # abre el archivo en modo lectura
    archivo = open(path, "r", encoding='utf-8')
    texto = archivo.read().capitalize()
    listaOpres = []
    listaOpdos = []
    #       O P E R A D O R E S
    tDef = texto.count("def")
    if tDef > 0:
        listaOpres.append(1.0)
    tAnd = texto.count("and")
    if tAnd > 0:
        listaOpres.append(1.0)
    tIs = texto.count("is")
    if tIs > 0:
        listaOpres.append(1.0)
    tDP = texto.count(":")
    if tDP > 0:
        listaOpres.append(1.0)
    tIgual = texto.count("=")
    if tIgual > 0:
        listaOpres.append(1.0)
    tDifQ = texto.count("!=")
    if tDifQ > 0:
        listaOpres.append(1.0)
    tWhile = texto.count("while")
    if tWhile > 0:
        listaOpres.append(1.0)
    tFor = texto.count("for")
    if tFor > 0:
        listaOpres.append(1.0)
    tIf = texto.count("if")
    if tIf > 0:
        listaOpres.append(1.0)
    tElse = texto.count("else")
    if tElse > 0:
        listaOpres.append(1.0)
    tElif = texto.count("elif")
    if tElif > 0:
        listaOpres.append(1.0)
    tBreak = texto.count("break")
    if tBreak > 0:
        listaOpres.append(1.0)
    tNot = texto.count("not")
    if tNot > 0:
        listaOpres.append(1.0)
    tTry = texto.count("try")
    if tTry > 0:
        listaOpres.append(1.0)
    tClas = texto.count("class")
    if tClas > 0:
        listaOpres.append(1.0)
    tOr = texto.count("or")
    if tOr > 0:
        listaOpres.append(1.0)
    tCont = texto.count("continue")
    if tCont > 0:
        listaOpres.append(1.0)
    tImp = texto.count("import")
    if tImp > 0:
        listaOpres.append(1.0)
    tFin = texto.count("finally")
    if tFin > 0:
        listaOpres.append(1.0)
    tIn = texto.count("in")
    if tIn > 0:
        listaOpres.append(1.0)
    tPrint = texto.count("print")
    if tPrint > 0:
        listaOpres.append(1.0)
    tFalse = texto.count("false")
    if tFalse > 0:
        listaOpres.append(1.0)
    tTrue = texto.count("true")
    if tTrue > 0:
        listaOpres.append(1.0)
    tNone = texto.count("None")
    if tNone > 0:
        listaOpres.append(1.0)
    tFile = texto.count("File")
    if tFile > 0:
        listaOpres.append(1.0)
    tMQ = texto.count(">")
    if tMQ > 0:
        listaOpres.append(1.0)
    tMenorQ = texto.count("<")
    if tMenorQ > 0:
        listaOpres.append(1.0)
    tMIgual = texto.count(">=")
    if tMIgual > 0:
        listaOpres.append(1.0)
    tMenIgual = texto.count("<=")
    if tMenIgual > 0:
        listaOpres.append(1.0)
    tMas = texto.count("+")
    if tMas > 0:
        listaOpres.append(1.0)
    tMenos = texto.count("-")
    if tMenos > 0:
        listaOpres.append(1.0)
    tPor = texto.count("*")
    if tPor > 0:
        listaOpres.append(1.0)
    tPot = texto.count("**")
    if tPot > 0:
        listaOpres.append(1.0)
    tDiv = texto.count("/")
    if tDiv > 0:
        listaOpres.append(1.0)
    tModulo = texto.count("%")
    if tModulo > 0:
        listaOpres.append(1.0)
    tComa = texto.count(",")
    if tComa > 0:
        listaOpres.append(1.0)
    tPA = texto.count("(")
    if tPA > 0:
        listaOpres.append(1.0)
    tCA = texto.count("[")
    if tCA > 0:
        listaOpres.append(1.0)
    n1 = len(listaOpres)
    eN1 = tDef+tAnd+tIs+tDP+tIgual+tDifQ+tWhile+tFor+tIf+tElse+tElif+tBreak+tNot+tTry+tClas+tOr+tCont+tImp+tFin + \
        tIn+tPrint+tFalse+tTrue+tNone+tFile+tMQ+tMenorQ+tMIgual + \
        tMenIgual+tMas+tMenos+tPor+tPot+tDiv+tModulo+tComa+tPA
    print("\n\tCÓDIGO FUENTE\n")

    print(texto)
    print("/////////////////////////////////////////////////////////////////////////////////")
    mBasicas = "Archivo: " + str(Cod) + "\n\nMÉTRICAS BÁSICAS" + \
        "\nTotal de ocurrencias de los Operadores N1 : " + \
        str(eN1) + "\nTotal operadores n1 : " + str(n1)
    print("\n\tMÉTRICAS BÁSICAS")
    print("\nTotal de ocurrencias de los Operadores N1 : ", eN1)
    print("\nTotal operadores n1 : ", n1)
    # O P E R A N D O S
    tMul = texto.count("mul")
    if tMul > 0:
        listaOpdos.append(tMul)
    tX = texto.count("x")
    if tX > 0:
        listaOpdos.append(tX)
    tY = texto.count("y")
    if tY > 0:
        listaOpdos.append(tY)
    tZ = texto.count("z")
    if tZ > 0:
        listaOpdos.append(tZ)
    tCero = texto.count("0")
    if tCero > 0:
        listaOpdos.append(tCero)
    tUno = texto.count("1")
    if tUno > 0:
        listaOpdos.append(tUno)
    tA = texto.count("a")
    if tA > 0:
        listaOpdos.append(tA)
    tN = texto.count("n")
    if tN > 0:
        listaOpdos.append(tN)
    tRes = texto.count("result")
    if tRes > 0:
        listaOpdos.append(tRes)
    tIi = texto.count("i")
    if tIi > 0:
        listaOpdos.append(tIi)

    n2 = len(listaOpdos)
    eN2 = tA+tIi+tN+tRes + float(tMul) + float(tX) + \
        float(tY) + float(tZ) + float(tCero) + float(tUno)
    print("\nTotal de ocurrencias de operandos N2 : ", eN2)
    print("\nTotal operandos n2 : ", n2)
    print("\n\tMÉTRICAS DERIVADAS")
    mBasicas += "\nTotal de ocurrencias de operandos N2 : " + \
        str(eN2) + "\nTotal operandos n2 : " + \
        str(n2) + "\n\nMÉTRICAS DERIVADAS"
    NN = "{0:.2f}".format(float(eN1) + float(eN2))
    print("\nLongitud N : ", NN)
    nn = "{0:.2f}".format(float(n1) + float(n2))
    print("\nVocabulario n : ", nn)
    V = "{0:.2f}".format(float(NN) * (math.log(float(nn)))/math.log(2))
    print("\nVolumen V : ", V)
    D = "{0:.2f}".format((n1/2.0)*(float(eN2)/n2))
    print("\nDificultad D : ", D)
    L = "{0:.5f}".format(1.0/float(D))
    print("\nNivel L : ", L)
    E = "{0:.2f}".format(float(D)*float(V))
    print("\nEsfuerzo E : ", E)
    T = "{0:.2f}".format(float(E)/18.0)
    print("\nTiempo T : ", T, " segundos")
    B = "{0:.2f}".format(float(E)**(2/3)/3000)
    print("\nNúmero de BUGS B : ", B)
    mBasicas += "\nLongitud N : " + str(NN) + "\nVocabulario n : " + str(nn) + "\nVolumen V : " + str(V) + "\nDificultad D : " + str(
        D) + "\nNivel L : " + str(L) + "\nEsfuerzo E : " + str(E) + "\nTiempo T : " + str(T) + " segundos" + "\nNúmero de BUGS B : " + str(B)

    archivo.close()
    conn = crearBase()
    print(conn)
    # bd = sqlite3.connect("Metricas.db")
    cursor = conn.cursor()
    sentencia = "INSERT INTO MetricasApp(codigo, n1, n2, N3, N4, N5, n, V, D, L, E, T, B) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
    try:
        cursor.execute(sentencia, [Cod, n1, n2, eN1,
                       eN2, NN, nn, V, D, L, E, T, B])
        conn.commit()

        screen.add_widget(MDLabel(
            text="Guardado correctamente",
            halign="center",
            pos_hint={'center_x': .5, 'center_y': .75},
        ))
        # screen.label.text = "Guardado correctamente"
        print("Guardado correctamente")
    except Error as e:
        screen.add_widget(MDLabel(
            text="Error al guardar",
            halign="center",
            pos_hint={'center_x': .5, 'center_y': .75},
        ))
        print("ERROR: " + e)

    return mBasicas


def crearBase():
    try:
        conn = sqlite3.connect("MetricasN.db")
        print("Conexion bien")
        conn.cursor()
        tablas = [
            """
                    CREATE TABLE IF NOT EXISTS MetricasApp(
                        codigo text,
                        n1 DOUBLE NOT NULL,
                        n2 DOUBLE NOT NULL,
                        N3 DOUBLE NOT NULL,
                        N4 DOUBLE NOT NULL,
                        N5 DOUBLE NOT NULL,
                        n DOUBLE NOT NULL,
                        V DOUBLE NOT NULL,
                        D DOUBLE NOT NULL,
                        L DOUBLE NOT NULL,
                        E DOUBLE NOT NULL,
                        T DOUBLE NOT NULL,
                        B DOUBLE NOT NULL       
                        );
                """
        ]
        for tabla in tablas:
            conn.execute(tabla)
        print("Tabla bien")
        return conn
    except Error as e:
        print(e)

if __name__ == '__main__':
    new().run()
