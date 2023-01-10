import sys
import numpy as np
import cv2 as cv
import math

hsv_min = np.array((0, 54, 5), np.uint8)
hsv_max = np.array((187, 255, 253), np.uint8)

color_blue = (255, 0, 0)
color_yellow = (0, 255, 255)


def rotate_a(contours, path):
    img = cv.imread(path)

    # перебираем все найденные контуры в цикле
    for cnt in contours:
        rect = cv.minAreaRect(cnt)  # пытаемся вписать прямоугольник
        box = cv.boxPoints(rect)  # поиск четырех вершин прямоугольника
        box = np.int0(box)  # округление координат
        center = (int(rect[0][0]), int(rect[0][1]))
        area = int(rect[1][0] * rect[1][1])  # вычисление площади

    # вычисление координат двух векторов, являющихся сторонам прямоугольника
        edge1 = np.int0((box[1][0] - box[0][0], box[1][1] - box[0][1]))
        edge2 = np.int0((box[2][0] - box[1][0], box[2][1] - box[1][1]))

    # выясняем какой вектор больше
        usedEdge = edge1
        if cv.norm(edge2) > cv.norm(edge1):
            usedEdge = edge2
        reference = (1, 0)  # горизонтальный вектор, задающий горизонт

    # вычисляем угол между самой длинной стороной прямоугольника и горизонтом
        angle = 180.0 / math.pi * math.acos(
            (reference[0] * usedEdge[0] + reference[1] * usedEdge[1]) / (cv.norm(reference) * cv.norm(usedEdge)))

        if area > 1000:
            cv.drawContours(img, cnt, -1, (255, 0, 0), 2)  # рисуем прямоугольник
            cv.drawContours(img, [box], -1, (255, 0, 0), 2)  # рисуем прямоугольник
            cv.circle(img, center, 5, color_yellow, 2)  # рисуем маленький кружок в центре прямоугольника
        # выводим в кадр величину угла наклона
            cv.putText(img, "%d" % int(angle), (center[0] + 20, center[1] - 20),
                   cv.FONT_HERSHEY_SIMPLEX, 1, color_yellow, 2)

        cv.imshow('contours', img)

    cv.waitKey()
    cv.destroyAllWindows()