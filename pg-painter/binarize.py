import cv2
import resizer
import painter

def binarize(input, output):
    img = cv2.imread(input)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = resizer.tshirt(img)

    _, binarized = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(output, binarized)

    img = cv2.imread(output)
    img = painter.transparentize(img)

    cv2.imwrite(output, img)
