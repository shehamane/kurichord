import numpy as np
from PIL import Image


def downscale(image: Image.Image, size: tuple) -> Image.Image:
    if image.size < size:
        raise Exception('Downscaling error: the source size is smaller than the destination size.')

    src_arr = np.array(image)
    result_arr = np.empty(shape=size + (3,), dtype=np.uint8)
    x_ratio, y_ratio = image.size[0] // size[0], image.size[1] // size[1]

    for y in range(0, size[1]):
        for x in range(0, size[0]):
            result_arr[y][x] = np.average(src_arr[y * y_ratio: (y + 1) * y_ratio, x * x_ratio: (x + 1) * x_ratio],
                                          axis=(0, 1))

    return Image.fromarray(result_arr)


if __name__ == '__main__':
    kurisu = Image.open('../test/scaling/kurisu.jpg')
    kurisu_scaled = downscale(kurisu, (224, 224))
    kurisu_scaled.show()
