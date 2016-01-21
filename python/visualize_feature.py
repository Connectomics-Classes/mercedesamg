import numpy as np
from skimage.io import imread, imshow
from skimage.feature import blob_dog
from skimage import color
from skimage.draw import circle_perimeter
import matplotlib.pyplot as plt


def visualize(image):
    blob_dog_feature = blob_dog(image, threshold=.1, max_sigma=10)
    max_y, max_x = image.shape
    image = color.gray2rgb(image)

    for item in blob_dog_feature:
        center_x, center_y, radius = item
        cx, cy = circle_perimeter(center_y, center_x, radius)

        # filtering out coordinates which are outside of the image
        cx, cy = zip(*filter(lambda (x, y): 0 <= x < max_x and 0 <= y < max_y, zip(cx, cy)))

        # make points red
        image[cy, cx] = (220, 20, 20)

    imshow(image)
    plt.show()


if __name__ == '__main__':
	
    # NOTE: Hard coded png --> this is swapped out for EM data
    image = imread('vesicle_example.png')

    # we only need 1 channel from the png (we made the image grayscale!)
    image = image[:, :, 0]

    # inverting image because blob_dog detection is sensitive to light spots!!
    image = np.invert(image)
    visualize(image)
