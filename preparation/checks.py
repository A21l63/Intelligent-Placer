import cv2


def area_check(polygon, contours):
    summary_area = 0
    for contour in contours:
        summary_area += cv2.contourArea(contour)
    #print(summary_area, ' qwerty ', cv2.contourArea(polygon))
    return cv2.contourArea(polygon) >= summary_area


def rad_check(polygon, contours):
    poly_rad = cv2.minEnclosingCircle(polygon)[1]
    for contour in contours:
        if poly_rad <= cv2.minEnclosingCircle(contour)[1]:
            return 0
    return 1


def check(polygon, contours):
    return rad_check(polygon, contours) and area_check(polygon, contours)