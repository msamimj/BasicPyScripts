from PIL import Image
img = Image.open('contour.png','r')
pix_val = list(img.getdata())
red_val = list()
for a in pix_val:
    red_val.append(a[0])
res = open("terrain-data.js","w")
val = ','.join(str(e) for e in red_val)
res.write("var zCoords = ["+val+"];")
