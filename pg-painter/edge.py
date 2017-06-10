import cv2
import resizer
import painter

img = cv2.imread("./images/p.jpg")
img = resizer.tshirt(img)

edge_detected = cv2.Canny(img, 50, 100)
cv2.imwrite("./test.png", edge_detected)

img = cv2.imread("./test.png")
img = painter.transparentize(img)

cv2.imwrite("./test.png", img)
