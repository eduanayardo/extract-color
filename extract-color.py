from PIL import Image
img = Image.open("1.jpg")

import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = mpimg.imread('1.jpg')
w, h, d = tuple (image.shape)
pixels = numpy.reshape(image, (w * h, d))

from sklearn.cluster import KMeans

n_colors = 10
model = KMeans(n_clusters=n_colors, random_state=42).fit (pixels)
palette = numpy.uint8(model.cluster_centers_)

def rgb_to_hex(r, g, b):
     return '#{:02x}{:02x}{:02x}'.format(r, g, b)

colors = []
for i in palette:
    ind = 0
    rgb  = ""
    for e in i:
        if ind == 2:
            rgb = rgb + str(e)
            rgb1 = rgb.split(",")
            colors.append(rgb_to_hex(int(rgb1[0]),int(rgb1[1]),int(rgb1[2])))
            rgb = ""
        else:
            rgb = rgb + str(e) + ","
        ind = ind + 1
print(colors)

plt.imshow([palette])
plt.show()