"""Librerias QT"""
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QStackedLayout,
    QPushButton,
    QWidget,
    QLabel,
    QLCDNumber,
    QSlider,
    QLayoutItem,
    QMessageBox,
    QLineEdit,
    QAction,
    QFileDialog,
    QDesktopWidget,
    QSizePolicy,
    QToolBar,
    QStatusBar,
    QDockWidget,
    QMenuBar,
    QCheckBox
)

from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from sklearn.feature_extraction import img_to_graph 

"""Librerias PDI"""
import sys
from skimage.io import imread
from matplotlib import pyplot as plt


"""Clases importadas"""
from Funciones import *
from FuncionesPDI import *


class MainApp(QWidget):
    """Docstring for MainApp"""
    def __init__(self):

        """Inicializacion"""
        #Main
        self.init__ = super(MainApp, self).__init__()
        """Window"""
        """Titulo"""
        self.setWindowTitle("VisualPDI")
        """Dimensiones"""
        # setMiniumSize() (Tamaño minimo de la pantalla)
        #self.setMinimumSize(500,300)
        # setMaximunSize() (Tamaño Maximo de la pantalla)
        #self.setMaximumSize(700,500)
        # setFixedSize() (Tamaño Fijo de la pantalla)
        self.setFixedSize(1500,1000)
        width_main_window = self.frameGeometry().width()
        height_main_window = self.frameGeometry().height()
        print("Las dimensiones de la pantalla son:\n")
        sizeWidgets(self)

        """Imagenes"""

        img = r"D:\Universidad\Procesamiento Digital de Imagenes\Proyecto\VisualPDI\Imagenes\lena.jpg"
        pixmap = QPixmap(img)
       

        """Labels"""
        """Forma"""
        labelClase1 = QLabel("Clase 1", self) 
        labelClase2 = QLabel("Clase 2", self)  
        labelClase3 = QLabel("Clase 3", self)
        labelClase4 = QLabel("Clase 4", self)  
        labelClase5 = QLabel("Clase 5", self)
        labelImg = QLabel(self)
        labelImg.setPixmap(pixmap)  
        """Dimensiones y posicion"""
        labelClase1.setAlignment(Qt.AlignCenter) #Setea posicion texto al centro
        labelClase2.setAlignment(Qt.AlignCenter) #Setea posicion texto al centro
        labelClase3.setAlignment(Qt.AlignCenter) #Setea posicion texto al centro
        labelClase4.setAlignment(Qt.AlignCenter) #Setea posicion texto al centro
        labelClase5.setAlignment(Qt.AlignCenter) #Setea posicion texto al centro
        """Estilo"""
        labelClase1.setStyleSheet("background:black;color:white") #Stilo background = fondo , color = color letra
        labelClase2.setStyleSheet("background:blue;color:white") #Stilo background = fondo , color = color letra
        labelClase3.setStyleSheet("background:red;color:white") #Stilo background = fondo , color = color letra
        labelClase4.setStyleSheet("background:green;color:white") #Stilo background = fondo , color = color letra
        labelClase5.setStyleSheet("background:purple;color:white") #Stilo background = fondo , color = color letra

        """Buttons"""
        """Forma"""
        self.btnClase1_1 = QPushButton("Black And White", self)
        self.btnClase1_2 = QPushButton("FaceShape", self)
        self.btnClase1_3 = QPushButton("Negativo", self)
        self.btnClase1_4 = QPushButton("Pixeleado", self)
        self.btnClase1_5 = QPushButton("Brillo", self)
        self.btnClase1_6 = QPushButton("Matiz Variado", self)
        self.btnClase2_1 = QPushButton("Ruido Gaussiano", self)
        self.btnClase2_2 = QPushButton("Ruido Sal & Pimienta", self)
        self.btnClase2_3 = QPushButton("Filtro De La Media", self)
        self.btnClase2_4 = QPushButton("Filtro Gaussiano", self)
        self.btnClase2_5 = QPushButton("Filtro Maximo & Minimo", self)
        self.btnClase2_6 = QPushButton("Filtro De La Mediana", self)
        self.btnClase3_1 = QPushButton("Laplaciano", self)
        self.btnClase3_2 = QPushButton("Plot Gradients", self)
        self.btnClase3_3 = QPushButton("Sobel", self)
        self.btnClase3_4 = QPushButton("Canny", self)
        self.btnClase4_1 = QPushButton("Histogram", self)
        self.btnClase4_2 = QPushButton("Histogram RGB", self)
        self.btnClase4_3 = QPushButton("K-Means", self)
        self.btnClase4_4 = QPushButton("Dominant Colors", self)
        self.btnClase4_5 = QPushButton("Segmentation K-means", self)
        self.btnClase4_6 = QPushButton("Filtro De La Mediana", self)
        self.btnClase5_1 = QPushButton("SLIC", self)
        self.btnClase5_2 = QPushButton("Ruido Sal & Pimienta", self)
        self.btnClase5_3 = QPushButton("Filtro De La Media", self)
        self.btnClase5_4 = QPushButton("Filtro Gaussiano", self)
        self.btnClase5_5 = QPushButton("Filtro Maximo & Minimo", self)
        self.btnClase5_6 = QPushButton("Filtro De La Mediana", self)
        """Dimensiones y posicion"""
        """Signals"""
        self.btnClase1_1.clicked.connect(self.blackAndWhite)
        self.btnClase1_2.clicked.connect(self.faceShape)
        self.btnClase1_3.clicked.connect(self.negativeSlot)
        self.btnClase1_4.clicked.connect(self.pixeleado)
        self.btnClase1_5.clicked.connect(self.brillo)
        self.btnClase1_6.clicked.connect(self.matizVariado)
        self.btnClase2_1.clicked.connect(self.ruidoGaussiano)
        self.btnClase2_2.clicked.connect(self.ruidoSal_Pimienta)
        self.btnClase2_3.clicked.connect(self.filtroDeLaMedia)
        self.btnClase2_4.clicked.connect(self.filtroGaussiano)
        self.btnClase2_5.clicked.connect(self.filtroMaximoMinimo)
        self.btnClase2_6.clicked.connect(self.filtroDeLaMediana)
        self.btnClase3_1.clicked.connect(self.laplaciano)
        self.btnClase3_2.clicked.connect(self.plotGradients)
        self.btnClase3_3.clicked.connect(self.sobel)
        self.btnClase3_4.clicked.connect(self.canny)
        self.btnClase4_1.clicked.connect(self.histogram)
        """self.btnClase4_2.clicked.connect(self.clase4F2)
        self.btnClase4_3.clicked.connect(self.clase4F3)
        self.btnClase4_4.clicked.connect(self.clase4F4)
        self.btnClase4_5.clicked.connect(self.clase4F5)
        self.btnClase4_6.clicked.connect(self.clase4F6)
        self.btnClase5_1.clicked.connect(self.clase5F1)
        self.btnClase5_2.clicked.connect(self.clase5F2)
        self.btnClase5_3.clicked.connect(self.clase5F3)
        self.btnClase5_4.clicked.connect(self.clase5F4)
        self.btnClase5_5.clicked.connect(self.clase5F5)
        self.btnClase5_6.clicked.connect(self.clase5F6)"""
        """QLine"""
        self.linePixeleado = QLineEdit(self)
        self.linePixeleado.setPlaceholderText("Cantidad Pixeleado")
        self.lineBrillo = QLineEdit(self)
        self.lineBrillo.setPlaceholderText("Cantidad Brillo")
        self.lineRuidoGaussianoVarianza = QLineEdit(self)
        self.lineRuidoGaussianoVarianza.setPlaceholderText("Cantidad Varianza")
        self.lineRuidoSalPimientaRuido = QLineEdit(self)
        self.lineRuidoSalPimientaRuido.setPlaceholderText("Cantidad Ruido")
        self.lineRuidoSalPimientaRatio = QLineEdit(self)
        self.lineRuidoSalPimientaRatio.setPlaceholderText("Cantidad Ratio")
        self.lineFiltroDeLaMediaSize = QLineEdit(self)
        self.lineFiltroDeLaMediaSize.setPlaceholderText("Tamano")
        self.lineFiltroDeLaMediaMode = QLineEdit(self)
        self.lineFiltroDeLaMediaMode.setPlaceholderText("full, valid OR same")
        self.lineFiltroDeLaMediaBoundary = QLineEdit(self)
        self.lineFiltroDeLaMediaBoundary.setPlaceholderText("Fill, wrap OR symm")
        self.lineFiltroDeLaMediaFillvalue = QLineEdit(self)
        self.lineFiltroDeLaMediaFillvalue.setPlaceholderText("Cantidad Fill")
        self.lineFiltroGaussianoSize = QLineEdit(self)
        self.lineFiltroGaussianoSize.setPlaceholderText("Tamano")
        self.lineFiltroGaussianoSigma = QLineEdit(self)
        self.lineFiltroGaussianoSigma.setPlaceholderText("Cantidad Sigma")
        self.lineFiltroGaussianoFillvalue = QLineEdit(self)
        self.lineFiltroGaussianoFillvalue.setPlaceholderText("Fill")
        self.lineFiltroGaussianoMode = QLineEdit(self)
        self.lineFiltroGaussianoMode.setPlaceholderText("full, valid OR same")
        self.lineFiltroGaussianoBoundary = QLineEdit(self)
        self.lineFiltroGaussianoBoundary.setPlaceholderText("Fill, wrap OR symm")
        self.lineFiltroMaximoMinimo = QLineEdit(self)
        self.lineFiltroMaximoMinimo.setPlaceholderText("Tamano")
        self.lineFiltroDeLaMediana = QLineEdit(self)
        self.lineFiltroDeLaMediana.setPlaceholderText("Tamano")

        """Layouts"""
        """Forma"""
        layout = QGridLayout()
        layoutButtonClase1 = QHBoxLayout()
        layoutButtonClase2 = QHBoxLayout()
        layoutButtonClase3 = QHBoxLayout()
        layoutButtonClase4 = QHBoxLayout()
        layoutButtonClase5 = QHBoxLayout()
        """Composición"""
        layoutButtonClase1.addWidget(self.btnClase1_1)
        layoutButtonClase1.addWidget(self.btnClase1_2,1)
        layoutButtonClase1.addWidget(self.btnClase1_3,2)
        layoutButtonClase1.addWidget(self.btnClase1_4,3)
        layoutButtonClase1.addWidget(self.linePixeleado,3)
        layoutButtonClase1.addWidget(self.btnClase1_5,4)
        layoutButtonClase1.addWidget(self.lineBrillo,4)
        layoutButtonClase1.addWidget(self.btnClase1_6,5)
        layoutButtonClase2.addWidget(self.btnClase2_1)
        layoutButtonClase2.addWidget(self.lineRuidoGaussianoVarianza)
        layoutButtonClase2.addWidget(self.btnClase2_2,1)
        layoutButtonClase2.addWidget(self.lineRuidoSalPimientaRuido,1)
        layoutButtonClase2.addWidget(self.lineRuidoSalPimientaRatio,1)
        layoutButtonClase2.addWidget(self.btnClase2_3,2)
        layoutButtonClase2.addWidget(self.lineFiltroDeLaMediaSize,2)
        layoutButtonClase2.addWidget(self.lineFiltroDeLaMediaFillvalue,2)
        layoutButtonClase2.addWidget(self.lineFiltroDeLaMediaMode,2)
        layoutButtonClase2.addWidget(self.lineFiltroDeLaMediaBoundary,2)
        layoutButtonClase2.addWidget(self.btnClase2_4,3)
        layoutButtonClase2.addWidget(self.lineFiltroGaussianoSize,3)
        layoutButtonClase2.addWidget(self.lineFiltroGaussianoSigma,3)
        layoutButtonClase2.addWidget(self.lineFiltroGaussianoFillvalue,3)
        layoutButtonClase2.addWidget(self.lineFiltroGaussianoMode,3)
        layoutButtonClase2.addWidget(self.lineFiltroGaussianoBoundary,3)
        layoutButtonClase2.addWidget(self.btnClase2_5,4)
        layoutButtonClase2.addWidget(self.lineFiltroMaximoMinimo,4)
        layoutButtonClase2.addWidget(self.btnClase2_6,5)
        layoutButtonClase2.addWidget(self.lineFiltroDeLaMediana,5)
        layoutButtonClase3.addWidget(self.btnClase3_1)
        layoutButtonClase3.addWidget(self.btnClase3_2,1)
        layoutButtonClase3.addWidget(self.btnClase3_3,2)
        layoutButtonClase3.addWidget(self.btnClase3_4,3)
        layoutButtonClase4.addWidget(self.btnClase4_1)
        """layoutButtonClase4.addWidget(self.btnClase4_2,1)
        layoutButtonClase4.addWidget(self.btnClase4_3,2)
        layoutButtonClase4.addWidget(self.btnClase4_4,3)
        layoutButtonClase4.addWidget(self.btnClase4_5,4)
        layoutButtonClase4.addWidget(self.btnClase4_6,5)
        layoutButtonClase5.addWidget(self.btnClase5_1)
        layoutButtonClase5.addWidget(self.btnClase5_2,1)
        layoutButtonClase5.addWidget(self.btnClase5_3,2)
        layoutButtonClase5.addWidget(self.btnClase5_4,3)
        layoutButtonClase5.addWidget(self.btnClase5_5,4)
        layoutButtonClase5.addWidget(self.btnClase5_6,5)"""


        layout.addWidget(labelClase1,0,0)
        layout.addLayout(layoutButtonClase1,1,0)
        layout.addWidget(labelClase2,2,0)
        layout.addLayout(layoutButtonClase2,3,0)
        layout.addWidget(labelClase3,4,0)
        layout.addLayout(layoutButtonClase3,5,0)
        layout.addWidget(labelClase4,6,0)
        layout.addLayout(layoutButtonClase4,7,0)
        """layout.addWidget(labelClase5,8,0)
        layout.addLayout(layoutButtonClase5,9,0)"""



        """Others"""
        layoutButtonClase1.addStretch()
        layoutButtonClase2.addStretch()
        layoutButtonClase3.addStretch()
       
        """Set"""
        #self.setLayout(layoutImgLCD)
        #self.setLayout(layoutsSlider)
        #self.setLayout(layoutLabelButton)
        self.setLayout(layout)

        """Menu"""
        #Estructura Menu Principal
        """Abrir Archivo"""
        self.actOpen = QAction(QIcon(r"VisualPDI\Imagenes\open.png"),"Abrir", self)
        self.actOpen.setShortcut("Ctrl+O")
        self.actOpen.setStatusTip("Abrir una nueva imagen")
        img = self.actOpen.triggered.connect(self.abrirImagen)
        pixmap = img
        """Guardar Archivo"""
        self.actSave = QAction(QIcon(r"VisualPDI\Imagenes\save.png"),"Guardar", self)
        self.actSave.setShortcut("Ctrl+G")
        self.actSave.setStatusTip("Guardar la imagen")
        self.actSave.triggered.connect(self.guardarImagen)
        """Imprimir Archivo"""
        self.actPrint = QAction(QIcon(r"VisualPDI\Imagenes\printer.png"),"Imprimir", self)
        self.actPrint.setShortcut("Ctrl+P")
        self.actPrint.setStatusTip("Imprimir la imagen")
        self.actPrint.triggered.connect(self.imprimirImagen)
        """Cerrar Aplicacion"""
        self.actExit = QAction(QIcon(r"VisualPDI\Imagenes\exit.png"),"Cerrar", self)
        self.actExit.setShortcut("Ctrl+Q")
        self.actExit.setStatusTip("Cerrar la aplicacion")
        self.actExit.triggered.connect(self.close)
        """Limpiar"""
        self.actClear = QAction(QIcon(r"VisualPDI\Imagenes\clear.png"),"Limpiar", self)
        self.actClear.setShortcut("Ctrl+D")
        self.actClear.setStatusTip("Limpiar imagen actual")
        self.actClear.triggered.connect(self.limpiarImagen)
        #Estructura Editaje basico
        """Rotar 90°"""
        self.actRotate90 = QAction(QIcon(r"VisualPDI\Imagenes\rotate90.png"),"Rotar90°", self)
        self.actRotate90.setStatusTip("Rotar en 90° imagen actual")
        self.actRotate90.triggered.connect(self.rotate90)
        """Rotar 180°"""
        self.actRotate180 = QAction(QIcon(r"VisualPDI\Imagenes\rotate180.png"),"Rotar180°", self)
        self.actRotate180.setStatusTip("Rotar en 180° imagen actual")
        self.actRotate180.triggered.connect(self.rotate180)
        """Redimensionar"""
        self.actResize = QAction(QIcon(r"VisualPDI\Imagenes\resize.png"),"Redimensionar", self)
        self.actResize.setStatusTip("reajusta la imagen")
        self.actResize.triggered.connect(self.redimensionarImagen)
        #Vista
        menuBar = QMenuBar(self)
        menuBar.setNativeMenuBar(False)
        #Menu Principal
        menuFile = menuBar.addMenu("Archivo")
        menuFile.addAction(self.actOpen)
        menuFile.addAction(self.actSave)
        menuFile.addSeparator()
        menuFile.addAction(self.actPrint)
        menuFile.addSeparator()
        menuFile.addAction(self.actExit)
        #Editaje Basico
        menuEdit = menuBar.addMenu("Edicion")
        menuEdit.addAction(self.actRotate90)
        menuEdit.addAction(self.actRotate180)
        menuEdit.addSeparator()
        menuEdit.addAction(self.actResize)
        menuEdit.addSeparator()
        menuEdit.addAction(self.actClear)
    #Funciones Menu Principal
    def abrirImagen(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        if imagen:
            imagenLeida = imread(imagen)
            print(imagen)
            plt.imshow(imagenLeida)
            plt.show()
            return imagenLeida
        else:
            QMessageBox.information(self, "Error", "No se pudo abrir la imagen",QMessageBox.OK)

    def guardarImagen(self):
        pass

    def imprimirImagen(self):
        pass

    def limpiarImagen(self):
        pass

    #Funciones Editaje basico
    def redimensionarImagen(self):
        pass

    def rotate90(self):
        pass

    def rotate180(self):
        pass

    """Cierre Aplicación"""
    def closeEvent(self, event):
        cuadro = QMessageBox.warning(self, "Cerrar", "¿Estas seguro que deseas cerrar la ventana?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if cuadro == QMessageBox.Yes:
            event.accept()
        elif cuadro == QMessageBox.No:
            event.ignore()



    
    """Slots Buttons"""
    #CLASE 1
    def blackAndWhite(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
        plt.figure(figsize=(10, 10))
        plt.subplot(1, 2, 1)
        plt.imshow(imagenLeida)
        plt.title("Imagen Normal")
        imgLum=(imagenLeida[:,:,0]*.2126+imagenLeida[:,:,1]*.7152+imagenLeida[:,:,2]*.0722)
        plt.subplot(1, 2, 2)
        plt.imshow(imgLum, cmap="gray")
        plt.title("Imagen Blanco & Negro")
        plt.show()

    def negativeSlot(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
        plt.figure(figsize=(10, 10))
        plt.subplot(1, 2, 1)
        plt.imshow(imagenLeida)
        plt.title("Imagen Normal")
        plt.subplot(1, 2, 2)
        plt.imshow(negativeEffect(imagenLeida))
        plt.title("Imagen en Negativo")
        plt.show()

    def faceShape(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
        MessageBoxFaceShape = QMessageBox(self)
        MessageBoxFaceShape.setIcon(QMessageBox.Information)
        MessageBoxFaceShape.setWindowTitle("Face Shape")
        MessageBoxFaceShape.setText("Las Posicion de la cara de la imagen es: " + str(imagenLeida.shape))
        MessageBoxFaceShape.setStandardButtons(QMessageBox.Ok)
        MessageBoxFaceShape.setDefaultButton(QMessageBox.Ok)
        MessageBoxFaceShape.exec_()

    def pixeleado(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
        pixeleado = int(self.linePixeleado.text()) #Max 50
        plt.figure(figsize=(10, 10))
        plt.subplot(1, 2, 1)
        plt.imshow(imagenLeida)
        plt.title("Imagen Normal")
        plt.subplot(1, 2, 2)
        plt.imshow(imagenLeida[::pixeleado, ::pixeleado])
        plt.title("Imagen Pixeleada")
        plt.show()

    def matizVariado(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
        f, axarr = plt.subplots(3,3,figsize=(12,8))
        for channel in (0,1,2):
            x=0
            for i in (2.5,.75,0.2):
                axarr[channel,x].imshow(matiz(imagenLeida,channel,i))
                axarr[channel,x].axis('off')
                x+=1
        f.tight_layout()
        plt.show()

    def brillo(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
        factor = int(self.lineBrillo.text()) #Max 255
        plt.figure(figsize=(10, 10))
        plt.subplot(1,2,1)
        plt.imshow(imagenLeida)
        plt.title("Imagen Normal")
        plt.subplot(1,2,2)
        plt.imshow(multiplicativa(imagenLeida,factor))
        plt.title("Imagen con Brillo")
        plt.show()

    #Clase 2
    def ruidoGaussiano(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
        varianza = float(self.lineRuidoGaussianoVarianza.text()) #Max 1
        ruido_gaussiano(imagenLeida, varianza)

    def ruidoSal_Pimienta(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
        ruido = float(self.lineRuidoSalPimientaRuido.text()) #Max 1
        ratio = float(self.lineRuidoSalPimientaRatio.text()) #Max 1
        ruido_sal_pimienta(imagenLeida,ruido,ratio)

    def filtroDeLaMedia(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
        size = int(self.lineRuidoSalPimientaRatio.text()) #Max Infinito
        mode = self.lineFiltroDeLaMediaMode.text() #full, valid & same
        boundary = self.lineFiltroDeLaMediaBoundary.text() #fill, wrap, symm
        fillvalue = float(self.lineRuidoSalPimientaRatio.text()) #Max Infinito (Predeterminado = 1)
        if mode == "valid":
            media_filter_img_valid(imagenLeida,size,mode)
        else:
            media_filter_img_full_AND_same(imagenLeida,size,mode,boundary,fillvalue)

    def filtroGaussiano(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
        size = int(self.lineFiltroGaussianoSize.text()) #Max Infinito
        sigma = int(self.lineFiltroGaussianoSigma.text()) #Max Infinito
        mode = self.lineFiltroGaussianoMode.text() #full, valid & same
        boundary = self.lineFiltroGaussianoBoundary.text() #fill, wrap, symm
        fillvalue = float(self.lineFiltroGaussianoFillvalue.text()) #Max Infinito (Predeterminado = 1)
        filtro_gaussiano(imagenLeida, size, sigma, mode, boundary, fillvalue)

    def filtroMaximoMinimo(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
        size = int(self.lineFiltroMaximoMinimo.text()) #Max Infinito
        max_min_filter_img(imagenLeida, size)

    def filtroDeLaMediana(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
        size = int(self.lineFiltroDeLaMediana.text()) #Max Infinito
        filtro_medianaPlt(imagenLeida, size)

    #Clase3
    def laplaciano(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
        laplaciano(imagenLeida)

    def plotGradients(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
        plot_gradients(imagenLeida)

    def sobel(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
        sobel(imagenLeida)

    def canny(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
        canny(imagenLeida)

    #Clase4

    def histogram(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
        plt.figure(figsize=(10, 3))
        plt.subplot(1,2,1)
        plt.imshow(imagenLeida)
        plt.title("Imagen Normal")
        plt.subplot(1,2,2)
        plt.plot(histogram(imagenLeida))
        plt.title("Histograma")
        plt.show()

"""    def clase4F2(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)

    def clase4F3(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
    
    def clase4F4(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)

    def clase4F5(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)

    def clase4F6(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
    

    #Clase5
    def clase5F1(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)

    def clase5F2(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)

    def clase5F3(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)
    
    def clase5F4(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)

    def clase5F5(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)

    def clase5F6(self):
        imagen, _ = QFileDialog.getOpenFileName(self, "Abrir imagen", "", "jpg (*.jepg *.jpg);; PNG (*.png)")
        imagenLeida = imread(imagen)"""

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Mainwindow = MainApp() #Ventana Principal
    Mainwindow.show() 
    sys.exit(app.exec_())


