import cv2
from find_sheet_and_polygon import sheet_detector, polygon_detector


def parse(contours):
    correct_contours = []
    sheet = sheet_detector(contours)
    polygon = polygon_detector(contours, sheet)
    for contour in contours:
        if cv2.pointPolygonTest(sheet, cv2.minEnclosingCircle(contour)[0], True) <= 0:
            correct_contours.append(contour)
    return correct_contours, sheet, polygon
