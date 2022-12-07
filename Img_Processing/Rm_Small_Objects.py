import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage import data
from skimage import color, morphology
from skimage.morphology import (closing)

#image = color.rgb2gray(data.hubble_deep_field())[:500, :500]
image = io.imread("Images/Laconce01.jpg", as_gray=True)

footprint = morphology.disk(2)
res = morphology.white_tophat(image, footprint)
closed = closing(res, footprint)

fig, ax = plt.subplots(ncols=3, figsize=(20, 8))
ax[0].set_title('Original')
ax[0].imshow(image, cmap='gray')
ax[1].set_title('White tophat')
ax[1].imshow(res, cmap='gray')
ax[2].set_title('Complementary')
ax[2].imshow(image - closed, cmap='gray')


plt.xticks([])
plt.yticks([])
plt.show()