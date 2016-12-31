#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image
import PIL
import Tkinter
import tkFileDialog
from StaticParameters import statischeParameter


breite = 128


class Bildverarbeitung:
	#~256 
	def __init__(self):
		self.basewidht = statischeParameter.BildBreite # Bild Breite Bild h�he wird skalirt
		self.imheight = 127 # Bild H�he
		
		self.blackwhite = 127 # Grund Schwarzweiss skala fon 0 bis 255
		
		self.im = "" #Variabel f�r Bild
		self.file_path = "" #Variabel f�r datei pfad
		self.im_array = "" #Variabel f�r ferarbeitetes Bild
		self.ColSel = "BW" # BW , C , M , Y, K 
		
	def ImgOpen(self): # f�nktion um das Bild zu �ffnen und in eine variabel zu tun

		root = Tkinter.Tk() #Name des Tkinter fensters bestimmen
		root.withdraw() #Tkinter fenster unsichtbar machen
		
		self.file_path = tkFileDialog.askopenfile(parent=root,filetypes=[("Image files",("*.jpg"))]) #fenster f�r Bildauswal �ffnen
		self.im = Image.open(self.file_path) #Bild aus filephath in variabel schreiben
		
		impersent = (self.basewidht/float(self.im.size[0])) # wie die h�he und breite zueinander stehen herausfinden
		self.imheight = int((float(self.im.size[1])*float(impersent)))	# Bild h�he Berechnen
		
		self.imgwork = self.im.resize((self.basewidht,self.imheight), Image.ANTIALIAS)  #Bild in in die richtige breite und h�he formatieren und in
												#self.imwork speichern	
		
		self.imgwork_BW = self.imgwork.convert("L") # Macht Bild aus self.imgwork Schwarz weiss  
		self.imgwork_COL = self.imgwork.convert("CMYK") # Macht Bild aus self.imgwork in den Druker farbcode 
		
	def Imgconverter(self): # funktion um das bild im gew�nschten farbcode in array zu schreiben 
		if self.file_path != "": #Wenn funktion aufgerufen wurde und noch kein Bild geladen ist dass es kein error gibt

			im_x , im_y = self.imgwork_COL.size # die breite und h�he werden in die variabeln im_x und im_y geschrieben 							
			self.im_array=[[0 for i1 in range(im_y)] for i2 in range(im_x)] # das array wird auf die anzal der Pixel im Bild gross gemacht
			print ("I: im_x = "+ str(im_x)+"\n")
			print ("I: im_y = "+ str(im_y)+"\n")
			print ("I: Colorselector = "+str(self.ColSel)+"\n")
			# Array abfullen
			for iy in range (im_y): # einfacher for loop wird so viell mal aufgerufen wie dass bild Hoch ist 										
				zeile=""													
				for ix in range(im_x):  # einfacher for loop wird so viell mal aufgerufen wie dass bild Breit ist 
										
					if self.ColSel == "BW": #Schaut ob dass bild in schwarzweiss onder in farbig gemacht werden soll
						self.im_array[ix][iy]= self.imgwork_BW.getpixel((ix, iy)) # Bef�llt dass programm mit dem farbcode der pixel im bild am richtigen ort
					else: #Wird aufgerufen wen das Array nicht schwarz weiss be�llt werden soll
						C,M,Y,K = self.imgwork_COL.getpixel((ix, iy)) # Es Schreibt die drei ferschiedenen farben in den gegebenen koordinaten in die fier gegebenen variabeln
											      # K ist nur ein faktor
						#~ zeile = zeile + str(K) + ":" 
						if self.ColSel == "C": #Schaut ob dass bild mit dem Cyan farbton gefiltert werden soll
							self.im_array[ix][iy] = 255 - C #Schreibt die farbskala ins arfray fon 1 bis 255
						elif self.ColSel == "M": #Schaut ob dass bild mit dem MKagenta farbton gefiltert werden soll
							self.im_array[ix][iy] = 255 - M #Schreibt die farbskala ins arfray fon 1 bis 255
						else: #wen dur einen fehler nichts angegeben wurde filtert er es mit der farbskala Yellow
							self.im_array[ix][iy] = 255 - Y #Schreibt die farbskala ins arfray fon 1 bis 255
				#~ print(zeile)

	def infoImgArray(self): 	#Gibt das verarbeitete Array zur�ck
		return self.im_array
		
	def infoblackwhite(self): 	#Gibt die farbskala zur�ck 1-255
		return int(self.blackwhite)

	def setblackwhite(self, pblackwhite): #�ndert die farbskala
		self.blackwhite = pblackwhite

	def infoFilePath(self): #Gibt den filepath zur�ck
		if self.file_path != "": # wenn filepath nicht lehr ist
			filename = str(self.file_path) #Schreibt file path in filename variabel als string f�rs konkatinieren
			filename = filename.split("'") #halbiert der inhalt der variabel bei einem Hochkomma
			return filename[1] # Gibt alles bis auf den ersten Buchstaben zur�ck
		else: # filepath leer ist
			return "" #es wird einen lehren string zur�ck gegeben
	
	def infoBildgeladen(self): #Gibt zur�ck ob ein bild geladen wurde
		if self.file_path == "": #wenn die variabel self.file_path leer ist
			return False # es gibt den booleanischen wert False zur�ck
		else:  #wird aufgerufen wenn in self.file_path variabel nicht leer ist
			return True # es gibt den booleanischen wert True zur�ck
			
	def infoBasewidht(self): # gibt breite des Bildes zur�ck
		return self.basewidht	

	def infoBaseheight(self): # gibt H�he des Bildes zur�ck
		return self.imheight	
		
	def infoColor(self): # gibt gewelte darbe zur�ck
		return self.ColSel
		
	def setColor(self, pCOL): #diese funktion kann die auswal farbe endern bekommt als parameter die auswalfarbe
		self.ColSel = pCOL #speichert die gew�nscht farbe in self.ColSel

	#Img in konsole schreiben test	
	def imgtestprint(self):
		im_x , im_y = self.imgwork.size
		#Array zum test ausdrucken
		print(self.blackwhite)
		for iy in range (im_y):
			zeile = ""
			for ix in range(im_x):
				px = self.im_array[ix][iy]
				if px > int(self.blackwhite):  #0==weiss  255==schwarz
					zeile = zeile + "W" + str(px)
				#~ elif px>127:
					#~ zeile=zeile + " "
				#~ elif px>64:
					#~ zeile=zeile + "x"
				else:
					zeile = zeile+"S" + str(px) 
			print(zeile)
			



