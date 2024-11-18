# библиотека numpy позволяет обрабатывать массив чисел. Преобразовывать  масссивы
# в матрицу, совершать маематические операции.
import numpy as np

def print_array(a):
    print(a)
print_array (a = np.array([10,  2,  0,  4,  74,  46,  37,  88,  90]))
def summ(a,b,c):
    print (a+b+c)
summ(a=np.array([10,20,30,15]),b=np.array(10),c=20)



# библиотека pillow позволяет работаь с изображениями.
# Проводить простые действия без привлечения графических редакторов.
from PIL import Image
im1 = Image.open("kartinka.jpg")
print(im1.format, im1.size, im1.mode)
im2 = Image.open("LediBag i Superkot.png")
out = im1.resize((750,750))
out = im2.resize((750, 750))
im3 = im2.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
im1.paste(im3, (0,0))
im1.show()
new_image = Image.new('RGB',(2*im1.size[0], im1.size[1]), (250,250,250))
out = new_image.resize((750, 750))
new_image.paste(im1,(0,0))
new_image.paste(im2, (im1.size[0], 0))
new_image.show()

out = im1.transpose(Image.Transpose.ROTATE_90)
out.show()







