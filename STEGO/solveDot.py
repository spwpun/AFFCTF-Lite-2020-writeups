#/usr/bin/env python3

from PIL import Image, ImageDraw
image = Image.open("image.png")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
tmp = ''
flag = ''
cnt = 0
pix = image.load()
for x in range(height):
    for y in range(width):
        r = pix[y,x][0]
        g = pix[y,x][1]
        b = pix[y,x][2]
        sr = (r + g + b)
        if sr == 0: #black dot
            tmp += '1'
        else:
            tmp += '0'
        cnt += 1
        if cnt == 8:
            flag += chr(int(tmp,2))
            cnt = 0
            tmp = ''
print(flag)
