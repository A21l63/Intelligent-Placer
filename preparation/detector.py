import numpy as np
import matplotlib.pyplot as plt
from imageio import imread, imsave
from skimage.color import rgb2gray, label2rgb
from skimage.transform import hough_line, hough_line_peaks, warp, AffineTransform
from skimage.feature import canny, corner_harris, corner_peaks, corner_fast, corner_subpix, match_descriptors, ORB
from skimage.filters import roberts, sobel, scharr, prewitt
from skimage.segmentation import watershed
from skimage.morphology import binary_closing, binary_erosion
from skimage.measure import ransac
from skimage import util
from scipy import ndimage as ndi
import os


picture = util.invert(rgb2gray(imread(os.path.join("../", "tsk_2.jpg"))))


# Эти параметры можно менять
canny_sigma = 2.75
canny_low_threshold = 0.2
canny_high_threshold = 0.6
binary_closing_footprint_width = 5
binary_closing_footprint = np.ones((binary_closing_footprint_width, binary_closing_footprint_width))

def correct_mask_borders_after_canny(canny_result, border_width=3):
    # заполняем полосы толщиной border_width нулями
    canny_result[:border_width,:] = 0
    canny_result[:,:border_width] = 0
    canny_result[-border_width:,:] = 0
    canny_result[:,-border_width:] = 0

my_edge_map = binary_closing(
    canny(
        picture,
        sigma=canny_sigma,
        low_threshold=canny_low_threshold,
        high_threshold=canny_high_threshold,
    ),
    footprint=binary_closing_footprint
)
correct_mask_borders_after_canny(my_edge_map)
my_edge_segmentation = ndi.binary_fill_holes(my_edge_map)

plt.imshow(label2rgb(my_edge_segmentation, image=picture))
result_image_file = os.path.join("../output", "res.png")
plt.savefig(result_image_file, dpi=150)


