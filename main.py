from skimage import io
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
ing = io.imread("Images/Laconce01.jpg", as_gray=True)
from skimage.filters import roberts, sobel, scharr, prewitt
from skimage.feature import canny

imgbgr = cv2.imread('Images/Laconce01.jpg')
imgRGB = cv2.cvtColor(imgbgr, cv2.COLOR_BGR2RGB)
edge_canny = canny(ing, sigma=2)

plt.xticks([])
plt.yticks([])
plt.imshow(edge_canny)
plt.show()