#script for Nael N.P. Prelaz
from PIL import Image
import sys
import numpy as np
n1=input("Watermark file name...")
n2=input("Name of file to be watermarked...")
#must be the same size !
wm = Image.open(n1)
im2 = Image.open(n2)
#tester que les 2 images on bien la meme taille
#sinon afficher une erreur
if (wm.size[0]!=im2.size[0]) or (wm.size[1]!=im2.size[1]):
    print("Error: files are not of the same size!")
    sys.exit()

#im.load()

#parcourir tous les pixels des images
#(=parcours d'un tableau a 2 dimentions)
#i:parcours les lignes, j:parcours les colonnes
#on prend la taille en lignes et colonnes du watermark(wm)
#(puisque de tt facon wm a la meme taille que im2)
for i in range(wm.size[0]):
    for j in range(wm.size[1]):
        #extraire la valeur du pixel a la position (i,j)
        #dans le watermark
        r,g,b=wm.getpixel((i,j))
        #on considere ici que si le pixel extrait n est pas blanc
        #(ne fait pas partie du fond) alors c est un pixel du wm
        #le blanc pur etant R=255,G=255,B=255 on test qu on ai
        #n importe quel valeur AUTRE que 255
        if r!=255 and g!=255 and b!=255:
            #changer la valeur du pixel a la position (i,j)
            #dans l image destination en la valeur du watermark
            #ici on a choisi la couleur bleu clair (R=0 G=127 B=255)
            im2.putpixel((i,j),(0,127,255))
im2.show()
im2.save("result.jpg")
