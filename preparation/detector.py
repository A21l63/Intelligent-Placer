def show_image(image):
    cv2.imshow('image', image)
    c = cv2.waitKey()
    if c >= 0: return -1
    return 0


def correct_mask_borders_after_canny(canny_result, border_width=3):
    canny_result[:border_width, :] = 0
    canny_result[:, :border_width] = 0
    canny_result[-border_width:, :] = 0
    canny_result[:, -border_width:] = 0


def find_contours(file_path = '../test_inputs/pic1.jpg'):
    image = cv2.imread(file_path)

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.GaussianBlur(img_gray, (5, 5), 0)
    canny = cv2.Canny(img_gray, 100, 200)
    correct_mask_borders_after_canny(canny)

    contours, hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_L1)
    img = cv2.drawContours(image, contours, -1, (255, 255, 0), 2)
    show_image(img)
    return contours
