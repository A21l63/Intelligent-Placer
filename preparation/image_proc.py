import cv2

def resize(file_path):
    img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    scale_percent = 1500 / img.shape[1]
    width = int(img.shape[1] * scale_percent)
    height = int(img.shape[0] * scale_percent)
    dim = (width, height)
    image = cv2.resize(img, dim, interpolation=cv2.INTER_LANCZOS4)
    new_path = '../test_inputs/test_pic.jpg'
    cv2.imwrite(new_path, image)
    return new_path
