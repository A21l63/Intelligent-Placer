from preparation import *
from preparation.detector import proc, draw, find_contours
from processing.pre_rotation import rotate_a


def place(contours, polygon, file_path):
    image = cv2.imread(file_path)
    draw(image, polygon)
    return


if __name__ == '__main__':
    file_path = '../test_inputs/pic1.jpg'
    contours, polygon, sheet, path = find_contours(file_path)
    rotate_a(contours, path)
    #place(contours, polygon, path)
