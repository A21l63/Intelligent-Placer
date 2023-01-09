from object import Object


def parse(contours):
    contours_with_areas = []
    paper = None
    polygon = None
    for contour in contours:
        contours_with_areas.append(Object(contour))
    return contours_with_areas, paper, polygon
