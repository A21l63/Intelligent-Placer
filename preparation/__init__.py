import cv2



def show_image(image):
    cv2.imshow('image',image)
    c = cv2.waitKey()
    if c >= 0 : return -1
    return 0



image = cv2.imread('../test_inputs/2_2.jpeg')

image = cv2.fastNlMeansDenoisingColored(image)
image = cv2.GaussianBlur(image, (9, 9), 0)

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, im = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy  = cv2.findContours(im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(image, contours, -1, (0,255,75), 2)
show_image(img)