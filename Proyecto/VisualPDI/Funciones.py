import numpy as np
from skimage.util import random_noise
from matplotlib import pyplot as plt
from scipy.signal import convolve2d
from scipy import ndimage
from skimage import filters
from skimage import feature
from scipy.ndimage import median_filter
from skimage.color import rgb2gray,rgba2rgb

def sizeWidgets(widgets):
    """Devuelve el tamño del objeto"""
    print("El largo es:", widgets.frameGeometry().width(), "\nEl alto es:", widgets.frameGeometry().height(),"\n")  #Devuelve el tamaño 

#Clase1
def negativeEffect(imagen):   
    return np.full(imagen.shape,255) - imagen

def matiz(imagen, canal, correccion):
    i=imagen.copy()
    i[:,:,canal]=i[:,:,canal]*correccion
    i[i>255]=255
    return i

def multiplicativa(imagen,factor):
    """Funcion usada en brillo"""
    i=imagen.copy()
    i*=factor
    i[i>255] = 255
    return i

#Clase2
#FUNCIONES RUIDO_GAUSSIANO

def ruido_gaussiano(imagen, varianza):
    noisy = random_noise(image = imagen, mode='gaussian', var=varianza)
    plt.imshow(noisy)
    plt.show()

#FUNCIONES RUIDO_SAL_PIMIENTA

def ruido_sal_pimienta(imagen, ruido, ratio):
    noisy = random_noise(image = imagen, mode = "s&p", amount = ruido, salt_vs_pepper = ratio)
    plt.imshow(noisy)
    plt.show()

#FUNCIONES FILTRO DE LA MEDIA

def media_filter_img_valid(imagen, tamaño, mode, boundary="fill", fillvalue=0):
    ims = []
    mask = np.full((tamaño,tamaño), 1/(tamaño**2))
    for d in range(3):
        im_conv_d = convolve2d(imagen[:,:,d], mask, mode=mode, boundary=boundary, fillvalue=fillvalue)
        ims.append(im_conv_d)
    im_conv = np.stack(ims, axis=2).astype("uint8")
    plt.imshow(im_conv)    
    plt.show()

def media_filter_img_full_AND_same(imagen, tamaño, mode, boundary, fillvalue):
    ims = []
    mask = np.full((tamaño,tamaño), 1/(tamaño**2))
    for d in range(3):
        im_conv_d = convolve2d(imagen[:,:,d], mask, mode=mode, boundary=boundary, fillvalue=fillvalue)
        ims.append(im_conv_d)
    im_conv = np.stack(ims, axis=2).astype("uint8")
    plt.imshow(im_conv)    
    plt.show()

#FUNCIONES FILTRO GAUSSIANO

def filtro_gaussiano(imagen, tamaño, sigma, mode, boundary, fillvalue):
    nn = int((tamaño-1)/2)
    a = np.asarray([[x**2 + y**2 for x in range(-nn,nn+1)] for y in range(-nn,nn+1)])        
    mask = np.exp(-a/(2*sigma**2))
    mask /= np.sum(mask)
    ims = []
    for d in range(3):
        im_conv_d = convolve2d(imagen[:,:,d], mask, mode=mode, boundary=boundary, fillvalue=fillvalue)
        ims.append(im_conv_d)
    im_conv = np.stack(ims, axis=2).astype("uint8")
    plt.imshow(im_conv)    
    plt.show()

#FUNCIONES FILTRO MAXIMO Y MINIMO

def max_min_filter_img(imagen, size):
    fig = plt.figure()
    ax1 = fig.add_subplot(121) 
    ax2 = fig.add_subplot(122)      
    maximum = ndimage.maximum_filter(imagen, size)
    minimum = ndimage.minimum_filter(imagen, size)    
    ax1.set_title("maximum")
    ax2.set_title("minimum")    
    ax1.imshow(maximum)
    ax2.imshow(minimum)    
    plt.show()

#FUNCIONES FILTRO DE LA MEDIANA

def filtro_medianaPlt(imagen, tamaño):
    ims = []
    for d in range(3):
        im_conv_d = median_filter(imagen[:,:,d], size=(tamaño,tamaño))
        ims.append(im_conv_d)
    im_conv = np.stack(ims, axis=2).astype("uint8")
    plt.imshow(im_conv)    
    plt.show()

#Clase3

def laplacian_kernel():
    mask = np.array([[0, 1, 0],
                    [1, -4, 1],
                    [0, 1, 0]])
    return mask

def laplaciano(imagen, binario=False):
    if binario:
        out = abs(convolve2d(rgb2gray(imagen), laplacian_kernel(), mode="same", boundary="fill"))
        plt.imshow(out, cmap='binary')
    else:
        ims = []
        for d in range(3):
            g = convolve2d(imagen[:,:,d], laplacian_kernel(), mode="same", boundary="fill")
            ims.append(g)        
        im_conv = np.stack(ims, axis=2).astype("uint8")
        plt.imshow(im_conv)    
    plt.show()

# Horizontal Sobel Filter
def h_sobel():
    mask = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]])
    return mask

# Vertical Sobel Filter
def v_sobel():
    mask = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])
    return mask

def plot_gradients(binary_image):
    gx = abs(convolve2d(rgb2gray(binary_image), h_sobel(), mode="same", boundary="fill"))
    gy = abs(convolve2d(rgb2gray(binary_image), v_sobel(), mode="same", boundary="fill"))
    fig = plt.figure(figsize=(13, 5))
    ax1 = fig.add_subplot(131)
    plt.imshow(binary_image)
    plt.title("Imagen Normal")         
    ax2 = fig.add_subplot(132)        
    plt.imshow(gx, cmap='binary')  
    plt.title("Gx")
    ax3 = fig.add_subplot(133)   
    plt.imshow(gy, cmap='binary')    
    plt.title("Gy")
    plt.show()

def sobel(imagen, binario=False):
    fig = plt.figure(figsize=(13, 5))    
    ax1 = fig.add_subplot(121)
    plt.imshow(imagen)
    plt.title("Imagen Normal")     
    if binario:
        sx = abs(convolve2d(rgb2gray(imagen), h_sobel(), mode="same", boundary="fill"))
        sy = abs(convolve2d(rgb2gray(imagen), v_sobel(), mode="same", boundary="fill"))
        out = np.sqrt(sx*sx + sy*sy)
        plt.imshow(out, cmap='binary')
    else:
        ims = []
        for d in range(3):
            sx = convolve2d(imagen[:,:,d], h_sobel(), mode="same", boundary="fill")
            sy = convolve2d(imagen[:,:,d], v_sobel(), mode="same", boundary="fill")
            ims.append(np.sqrt(sx*sx + sy*sy))        
        im_conv = np.stack(ims, axis=2).astype("uint8")
        ax2 = fig.add_subplot(122)
        plt.imshow(im_conv)
        plt.title("Sobel")    
    plt.show()

def filtro_medianaReturn(imagen, tamaño=1):
    ims = []
    for d in range(3):
        g = median_filter(imagen[:,:,d], size=(tamaño,tamaño))
        ims.append(g)
    im_conv = np.stack(ims, axis=2).astype("uint8")
    return im_conv

def canny(imagen):
    edge = feature.canny(rgb2gray(imagen))
    fig = plt.figure(figsize=(13, 5))
    ax1 = fig.add_subplot(121)
    plt.imshow(imagen)
    plt.title("Imagen Normal")         
    ax2 = fig.add_subplot(122)        
    plt.imshow(edge, cmap='binary')
    plt.title("Canny")
    plt.show()

#Clase4
def histogram(imagen):
    histogram, bin_edges = np.histogram(rgb2gray(rgba2rgb(imagen)), bins=256, range=(0, 1))
#Clase5