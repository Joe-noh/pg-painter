import cv2

def transparentize(img):
    gray_scaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, alpha = cv2.threshold(gray_scaled, 0, 255, cv2.THRESH_BINARY)

    b, g, r = cv2.split(img)
    rgba = [b, g, r, alpha]

    return cv2.merge(rgba, 4)
