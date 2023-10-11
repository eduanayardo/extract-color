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

plt.imshow([palette])
plt.show()