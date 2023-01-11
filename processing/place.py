from shapely import hausdorff_distance, difference, make_valid, LinearRing, intersection

import cv2

from shapely.geometry import Polygon
from shapely.affinity import translate, rotate

from processing.working_space import Working_space

NUMBER_OF_STEPS = 20
NUMBER_OF_ROTATES = 8

def place(polygon, contours):
    new_poly = polygon[:, 0, :]
    placed_objects = []
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    working_space = Working_space(cv2.boundingRect(new_poly))

    for contour in contours:
        placed_object, new_poly = place_contour(contour, Polygon(polygon[:, 0, :]), working_space, placed_objects)
        if new_poly == 0:
            print("Решение не найдено")
            return -1
        placed_objects.append(placed_object)
    return placed_objects


def place_contour(contour, polygon, working_space, placed_objects):
    contour = Polygon(contour[:, 0, :])

    step_x = int(abs(working_space.left_x - working_space.right_x) / NUMBER_OF_STEPS)
    step_y = int(abs(working_space.top_y - working_space.bot_y) / NUMBER_OF_STEPS)
    step_rotation = int(180 / NUMBER_OF_ROTATES)

    new_poly = 0
    hausdorff = -1

    placed_obj = None
    for stepx in range(working_space.left_x - int(contour.centroid.x), working_space.right_x - int(contour.centroid.x), step_x):
        for stepy in range(working_space.bot_y - int(contour.centroid.y), working_space.top_y - int(contour.centroid.y), step_y):
            moved = translate(contour, stepx, stepy)
            for step_ang in range(0, 180, int(step_rotation)):
                turned = rotate(moved, -step_ang, origin='centroid')
                if turned.covered_by(polygon):
                    for confirmed in placed_objects:
                        if confirmed.intersection(turned).area > 0:
                            break
                    else:
                        metric = turned.hausdorff_distance(polygon)
                        if metric >= hausdorff:
                            placed_obj = turned
                            hausdorff = metric
                            new_poly = difference(polygon, placed_obj)
                            if metric >= abs(working_space.top_y - working_space.bot_y):
                                break
    if hausdorff == -1 or placed_obj is None:
        return 0, 0

    return placed_obj, new_poly
