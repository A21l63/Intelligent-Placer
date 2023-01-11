from preparation import *
from preparation.find_sheet_and_polygon import polygon_detector, sheet_detector
from preparation.image_proc import resize
from processing.pre_rotation import rotate_contours_to_horizon
import cv2


AREA = 1500


def show_image(image):
    cv2.imshow('image', image)
    c = cv2.waitKey()
    if c >= 0:
        return -1
    return 0


def correct_mask_borders_after_canny(canny_result, border_width=20):
    canny_result[:border_width, :] = 0
    canny_result[:, :border_width] = 0
    canny_result[-border_width:, :] = 0
    canny_result[:, -border_width:] = 0


def find_contours_polygon_sheet(file_path):
    path = resize(file_path)
    image = cv2.imread(path)

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.GaussianBlur(img_gray, (5, 5), 0)

    canny = cv2.Canny(img_gray, 80, 200)
    correct_mask_borders_after_canny(canny)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    canny = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = area_filter(contours, 1)

    canny = cv2.Canny(img_gray, 80, 200)
    correct_mask_borders_after_canny(canny)
    cont, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cont = area_filter(cont, 0)
    sheet = sheet_detector(cont)
    if len(sheet) == 0:
        return ("На фотографии отсутствует лист")
    polygon = polygon_detector(cont, sheet)


    rotate, polygon = rotate_contours_to_horizon(contours, polygon)

    return rotate, polygon, sheet, path


def area_filter(contours, flag):
    correct = []
    maks = 0
    for contour in contours:
        arr = cv2.contourArea(contour)
        if maks < cv2.contourArea(contour):
            maks = arr
    for contour in contours:
        arr = cv2.contourArea(contour)
        if arr >= AREA and ((not flag) or arr != maks):
            correct.append(contour)
    return correct


def draw(image, correct_contours):
    img = cv2.drawContours(image, correct_contours, -1, (255, 0, 255), 2)
    show_image(img)

file_path = '../test_inputs/2_1.jpeg'

#draw(cv2.imread(file_path), find_contours_polygon_sheet(file_path)[0])