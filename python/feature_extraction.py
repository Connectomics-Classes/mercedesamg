import numpy as np
from skimage.io import imread
from skimage.feature import blob_dog
from skimage.transform import hough_circle


def extract(image):
	
    # used with default parameters, play around with params for other results
    blob_dog_feature = blob_dog(image, min_sigma=1, max_sigma=50, sigma_ratio=1.6, threshold=2.0, overlap=.5)

    # several sizes of radius, play around with params for other results
    hough_radii = np.array([5, 10, 15, 20, 30, 50])

    hough_circle_feature = hough_circle(image, hough_radii, normalize=True, full_output=False)

	# prints a LOT... takes a while
	# comment out the next line to print short version
    np.set_printoptions(threshold='nan')
    print([blob_dog_feature, hough_circle_feature])
    return [blob_dog_feature, hough_circle_feature]


if __name__ == '__main__':

    # NOTE: Hard coded png --> this is swapped out for EM data
    image = imread('vesicle_example.png')

    # we only need 1 channel from the png
    # (if image isn't grayscale, then grayscale it!!)
    image = image[:, :, 0]

    # inverting image because blob_dog detection is sensitive to light spots!!
    image = np.invert(image)
    features = extract(image)
