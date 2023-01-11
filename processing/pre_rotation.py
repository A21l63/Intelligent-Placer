import numpy as np
import cv2
import math


def cart2pol(x, y):
    theta = np.arctan2(y, x)
    rho = np.hypot(x, y)
    return theta, rho


def pol2cart(theta, rho):
    x = rho * np.cos(theta)
    y = rho * np.sin(theta)
    return x, y


def rotate_contours_to_horizon(contours, polygon):
    rotated = []
    for contour in contours:
        rect = cv2.minAreaRect(contour)
        if rect[1][0] < rect[1][1]:
            angle = -rect[2] - 90
        else:
            angle = -rect[2] - 180

        #angle = -angle
        M = cv2.moments(contour)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])

        cnt_norm = contour - [cx, cy]

        coordinates = cnt_norm[:, 0, :]
        xs, ys = coordinates[:, 0], coordinates[:, 1]
        thetas, rhos = cart2pol(xs, ys)

        thetas = np.rad2deg(thetas)
        thetas = (thetas + angle) % 360
        thetas = np.deg2rad(thetas)

        xs, ys = pol2cart(thetas, rhos)

        cnt_norm[:, 0, 0] = xs
        cnt_norm[:, 0, 1] = ys

        cnt_rotated = cnt_norm + [cx, cy]
        cnt_rotated = cnt_rotated.astype(np.int32)
        rotated.append(cnt_rotated)

    rect = cv2.minAreaRect(polygon)
    if (rect[1][0] < rect[1][1]):
        angle = -rect[2] - 90
    else:
        angle = -rect[2] - 180

    # angle = -angle
    M = cv2.moments(polygon)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])

    cnt_norm = polygon - [cx, cy]

    coordinates = cnt_norm[:, 0, :]
    xs, ys = coordinates[:, 0], coordinates[:, 1]
    thetas, rhos = cart2pol(xs, ys)

    thetas = np.rad2deg(thetas)
    thetas = (thetas + angle) % 360
    thetas = np.deg2rad(thetas)

    xs, ys = pol2cart(thetas, rhos)

    cnt_norm[:, 0, 0] = xs
    cnt_norm[:, 0, 1] = ys

    cnt_rotated = cnt_norm + [cx, cy]
    cnt_rotated = cnt_rotated.astype(np.int32)

    return rotated, cnt_rotated
