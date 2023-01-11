import cv2


def sheet_detector(contours):
    sorted_contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    if len(sorted_contours[0]) > 0:
        return sorted_contours[0]
    else:
        return 0


def polygon_detector(contours, sheet):
    possible_polygons = []
    for contour in contours:
        if cv2.pointPolygonTest(sheet, cv2.minEnclosingCircle(contour)[0], True) >= 0:
            possible_polygons.append(contour)
    if len(possible_polygons) != 0:
        sorted_possible_polygons = sorted(possible_polygons, key=lambda x: cv2.contourArea(x), reverse=False)
        return sorted_possible_polygons[0]
    else:
        return("На фотографии отсутвует многоугольник")
