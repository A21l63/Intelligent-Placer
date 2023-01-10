import cv2


class Contour:
    def __init__(self, contour):
        self.contour = contour
        self.area = cv2.contourArea(contour)
        self.radius = cv2.minEnclosingCircle(contour)[1]
