
import numpy as np
import scipy
import matplotlib.pyplot as plt
import PIL
import imageio

img = imageio.v2.imread('cat_tinted_imshow.png')
img_tinted = img * [1, 0.95, 0.9]

plt.subplot(1, 2, 1)
plt.imshow(img)

plt.show()