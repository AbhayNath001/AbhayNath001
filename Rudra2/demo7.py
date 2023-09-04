import cv2
import numpy as np

# Load the black and white image
bw_img = cv2.imread('Abhay Nath.png', cv2.IMREAD_GRAYSCALE)

# Create a color version of the image by stacking the same grayscale image into 3 color channels
color_img = np.stack((bw_img, bw_img, bw_img), axis=-1)

# Apply a color map to the image to fill in the color
color_img = cv2.applyColorMap(bw_img, cv2.COLORMAP_JET)

# Save the black and white image
cv2.imwrite('bw_img.png', bw_img)

# Save the colored image
cv2.imwrite('color_img.png', color_img)