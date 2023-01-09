def area_check(polygon, contours):
    summary_area = 0
    for contour in contours:
        summary_area += contour.area
    return polygon.area >= summary_area


def rad_check(polygon, contours):
    for contour in contours:
        if polygon.radius <= contour.radius:
            return 0
    return 1
