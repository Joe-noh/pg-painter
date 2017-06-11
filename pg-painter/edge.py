import cv2
import resizer
import painter

def edge_detection(input, output):
    img = cv2.imread(input)
    img = resizer.tshirt(img)

    edge_detected = cv2.Canny(img, 50, 100)
    cv2.imwrite(output, edge_detected)

    img = cv2.imread(output)
    img = painter.transparentize(img)

    cv2.imwrite(output, img)
