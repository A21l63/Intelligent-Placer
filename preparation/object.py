import cv2


class Contour:
    def __init__(self, contour, x, y, ang):
        self.contour = contour
        self.x = x
        self.y = y
        self.ang = ang
