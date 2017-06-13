import cv2
import numpy
import random
import itertools
import resizer
import painter

def quantize(input, output):
    original_img = cv2.imread(input)
    original_img = resizer.tshirt(original_img)
    img = original_img.reshape((-1, 3))

    # convert to np.float32
    img = numpy.float32(img)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    k = 4
    ret,label,center = cv2.kmeans(img, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = numpy.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((original_img.shape))

    colors = extract_colors(res2, k)
    print(colors)

    new_colors = [
        [159, 173, 31],
        [49, 49, 205],
        [18, 18, 171],
        [181, 228, 246]
    ]

    for (c, replacement) in zip(colors, new_colors):
        replaced = [int(c[i:i+3]) for i in range(0, len(c), 3)]
        res2[numpy.where((res2 == replaced).all(axis=2))] = replacement

    cv2.imwrite(output, res2)

def extract_colors(img, k):
    colors = []

    for _ in itertools.repeat(None, 10):
        colors.extend(random.choice(img))

    uniqs = []
    for c in colors:
        stringified = str(c[0]).zfill(3) + str(c[1]).zfill(3) + str(c[2]).zfill(3)
        uniqs.append(stringified)

        if len(list(set(uniqs))) == k:
            return list(set(uniqs))

    return False
