import cv2
import numpy as np

from preparation.find_sheet_and_polygon import polygon_detector, sheet_detector


def parse(contours):
    correct = []
    sheet = sheet_detector(contours)
    polygon = polygon_detector(contours, sheet)
    contours.remove(sheet)
    contours.remove(polygon)

    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for contour in contours:
        if cv2.pointPolygonTest(sheet, cv2.minEnclosingCircle(contour)[0], True) <= 0:
            correct.append(contour)

    for contour in correct:
        area = cv2.contourArea(contour)
        rect = cv2.minAreaRect(contour)
        for contour_1 in correct:
            if cv2.matchShapes(contour, contour_1, cv2.CONTOURS_MATCH_I2, 0.0) > 0:
                intersect = cv2.rotatedRectangleIntersection(cv2.minAreaRect(contour_1), rect)
                if (intersect is not None) and cv2.contourArea(contour_1) < area:
                    correct.remove(contour_1)
    return correct, sheet, polygon
