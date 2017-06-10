MAX_HEIGHT = 2992
MAX_WIDTH  = 2520

def tshirt(img):
    height = img.shape[0]
    width  = img.shape[1]

    if height > MAX_HEIGHT and width > MAX_WIDTH:
        offset_y = int((height - MAX_HEIGHT) / 2)
        offset_x = int((width - MAX_WIDTH) / 2)

        return img[offset_y:offset_y+MAX_HEIGHT, offset_x:offset_x+MAX_WIDTH]
    elif height > MAX_HEIGHT:
        offset_y = int((height - MAX_HEIGHT) / 2)

        return img[offset_y:offset_y+MAX_HEIGHT, 0:width]
    elif width > MAX_WIDTH:
        offset_x = int((width - MAX_WIDTH) / 2)

        return img[0:height, offset_x:offset_x+MAX_WIDTH]
    else:
        return img
