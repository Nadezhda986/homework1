import numpy as np

def print_array(a):
    print(a)
print_array (a = np.array([10,  2,  0,  4,  74,  46,  37,  88,  90]))
def summ(a,b,c):
    print (a+b+c)
summ(a=np.array([10,20,30,15]),b=np.array(10),c=20)


from PIL import image
im = image.open ("hopper.ppm")
print(im.format, im.size, im.mode)
