from preparation import *
from preparation.find_sheet_and_polygon import polygon_detector, sheet_detector
from preparation.parse_master import parse
from preparation.image_proc import resize


AREA = 800


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

    canny = cv2.Canny(img_gray, 100, 200)
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
    polygon = polygon_detector(cont, sheet)

    return contours, polygon, sheet, path



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


def proc(file_path):
    contours, file_path = find_contours(file_path)
    correct_contours, sheet, polygon = parse(contours)
    return correct_contours, polygon, file_path


if __name__ == '__main__':
    proc()
