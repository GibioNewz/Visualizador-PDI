import cv2 as cv
import numpy as np
import os
from matplotlib import pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def recibir_img(nombre):  	#Inicializar imagen
	imagen = cv.imread(nombre)
	return imagen

def ajustar(imagen, factor): 	# Arreglar tamaño de la imagen //  se pueden añadir limites si desea posteriormente // capture.set
	ancho = int(imagen.shape[1] * factor)
	alto = int(imagen.shape[0] * factor)
	dimensiones = (ancho, alto)

	return cv.resize(imagen, dimensiones, interpolation= cv.INTER_AREA)
def escala_gris(imagen):
	img = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
	return img
def suavizar(imagen, x, y):
	img = cv.GaussianBlur(imagen,(x,y), cv.BORDER_DEFAULT) # x y y son la matriz de pixeles 
	return img
def ruido(noise_typ,image, vari): # var = varianza
	if noise_typ == "gauss": # se añade ruido a traves de: gauss, s&p, poisson, speckle
		row,col,ch= image.shape
		mean = 0
		var = vari
		sigma = var**0.5
		gauss = np.random.normal(mean,sigma,(row,col,ch))
		gauss = gauss.reshape(row,col,ch)
		noisy =  gauss + image
		return noisy
	elif noise_typ == "s&p":
		row,col,ch = image.shape
		s_vs_p = 0.5
		amount = 0.004
		out = np.copy(image)
		num_salt = np.ceil(amount * image.size * s_vs_p)
		coords = [np.random.randint(0, i - 1, int(num_salt))
			for i in image.shape]
		out[coords] = 1

      # Pepper mode
		num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
		coords = [np.random.randint(0, i - 1, int(num_pepper))
			for i in image.shape]
		out[coords] = 0
		return out
	elif noise_typ == "poisson":
		vals = len(np.unique(image))
		vals = 2 ** np.ceil(np.log2(vals))
		noisy = np.random.poisson(image * vals) / float(vals)
		return noisy
	elif noise_typ =="speckle":
		row,col,ch = image.shape
		gauss = np.random.randn(row,col,ch)
		gauss = gauss.reshape(row,col,ch)        
		noisy = image + image * gauss
		return noisy
##############################################################################
#clase 2
def suavizar_median(imagen, factor):
	imag = cv.medianBlur(imagen,factor)
	return imag
def minimumBoxFilter(factor, imagen):
  img = imagen
  size = (factor, factor)
  shape = cv.MORPH_RECT
  kernel = cv.getStructuringElement(shape, size)
  imgResult = cv.erode(img, kernel)
  return imgResult

def maximumBoxFilter(factor, imagen):
  img = imagen
  size = (factor,factor)
  shape = cv.MORPH_RECT
  kernel = cv.getStructuringElement(shape, size)
  imgResult = cv.dilate(img, kernel)
  return imgResult
##############################################################################
#clase 3
def laplaciano(imagen, kernel):
	img = cv.Laplacian(imagen,cv.CV_64F,kernel)
	return img
def sobel(imagen, kernel):
	img = cv.Sobel(imagen,cv.CV_64F,0,1,kernel,scale = 1) # kernel = 1,3,5,7 estricto
	return img

def canny(imagen, x,y):
	img = cv.Canny(imagen,x,y)
	return img

##############################################################################
#clase 4
def histograma(imagen, canales):
	if(canales>1):
		color = ('b','g','r')
		for i,col in enumerate(color):
			histr = cv.calcHist([imagen],[i],None,[256],[0,256])
			plt.plot(histr,color = col)
			plt.xlim([0,256])
		plt.show()
	else:
		hist = cv.calcHist([imagen],[0],None,[256],[0,256])
		hist,bins = np.histogram(imagen.ravel(),256,[0,256])
		plt.hist(imagen.ravel(),256,[0,256]); plt.show()
def thresholding(imagen):
	ret,thresh1 = cv.threshold(imagen,127,255,cv.THRESH_BINARY)
	ret,thresh2 = cv.threshold(imagen,127,255,cv.THRESH_BINARY_INV)
	ret,thresh3 = cv.threshold(imagen,127,255,cv.THRESH_TRUNC)
	ret,thresh4 = cv.threshold(imagen,127,255,cv.THRESH_TOZERO)
	ret,thresh5 = cv.threshold(imagen,127,255,cv.THRESH_TOZERO_INV)
	titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
	images = [imagen, thresh1, thresh2, thresh3, thresh4, thresh5]
	for i in range(6):
		plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
		plt.title(titles[i])
		plt.xticks([]),plt.yticks([])
	plt.show()
def kmeans(imagen,clusters):
	img = imagen
	Z = img.reshape((-1,3))
	# convert to np.float32
	Z = np.float32(Z)
	# define criteria, number of clusters(K) and apply kmeans()
	criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	K = clusters
	ret,label,center=cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
	# Now convert back into uint8, and make original image
	center = np.uint8(center)
	res = center[label.flatten()]
	res2 = res.reshape((img.shape))	
	return res2
def dominant_colors(image,k=2):
	km=KMeans(n_clusters=k).fit(image.reshape((-1,3)))
	i=0
	plt.figure(0,figsize=(15,3))
	plt.subplot(1,k+1,1)
	plt.imshow(image)
	plt.axis('off')
	for color in km.cluster_centers_:
		plt.subplot(1,k+1,i+2)
		plt.axis("off")
		a=np.zeros((100,100,3),dtype='uint8')
		a[:,:,:]=color
		plt.imshow(a)
		percent=list(km.labels_).count(i)/len(km.labels_)
		plt.title(f"{round(percent*100)}%")
		i+=1