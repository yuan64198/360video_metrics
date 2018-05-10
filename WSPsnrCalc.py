import numpy
import math
from PIL import Image

PIXEL_MAX = 255.0

def WSPsnrCalc(img1, img2):
    width, height = img1.size
    img1_list = list(img1.getdata())
    img2_list = list(img2.getdata())
    img1_list = [img1_list[i * width:(i + 1) * width] for i in range(height)]
    img2_list = [img2_list[i * width:(i + 1) * width] for i in range(height)]
    weight_list = [[math.cos((j+0.5-height/2)*math.pi/height) for j in range(height)] for i in range(width)]
    weight_sum = sum(sum(weight_list,[]))
    wmse = 0
    for i in range(height):
        for j in range(width):
            for k in range(3):#RGB
                wmse += ((img1_list[i][j][k] - img2_list[i][j][k])**2)*weight_list[i][j]
    wmse = (wmse/(width*height))/3
    if wmse == 0:
        return 100
    ws_psnr = 10*numpy.log10((PIXEL_MAX**2 /wmse))
    return ws_psnr
