from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


fileName=input("Name of file to be watermarked...")
myText=input("Text of the watermark...")
posX=int(input("X position of text..."))
posY=int(input("Y position of text..."))
img = Image.open(fileName)
d = ImageDraw.Draw(img)
#possibilite de changer la police de caractere - a etudier
# font = ImageFont.truetype(<font-file>, <font-size>)
#font = ImageFont.truetype("sans-serif.ttf", 16)
# d.text((x, y),"Sample Text",(r,g,b))

##fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts')
##font = ImageFont.truetype(os.path.join(fonts_path, 'sans_serif.ttf'), 24)

d.text((posX, posY),myText,(255,255,255))
img.save('result.jpg')
