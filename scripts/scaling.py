import numpy as np
from PIL import Image


def downscale(image: Image.Image, size: tuple) -> Image.Image:
    if image.size < size:
        raise Exception('Downscaling error: the source size is smaller than the destination size.')

    src_arr = np.array(image)
    result_arr = np.empty(shape=tuple(reversed(size)) + (3,), dtype=np.uint8)
    x_ratio, y_ratio = size[0] / image.size[0], size[1] / image.size[1]

    box_width = int(np.ceil(1 / x_ratio))
    box_height = int(np.ceil(1 / y_ratio))

    for y in range(size[1]):
        for x in range(size[0]):
            x_start = int(np.floor(x / x_ratio))
            y_start = int(np.floor(y / y_ratio))

            x_end = min(x_start + box_width, image.size[0])
            y_end = min(y_start + box_height, image.size[1])

            result_arr[y][x] = np.ceil(np.mean(src_arr[y_start: y_end, x_start: x_end],
                                       axis=(0, 1)))

    return Image.fromarray(result_arr)


if __name__ == '__main__':
    kurisu = Image.open('../test/scaling/kurisu.jpg')
    kurisu_scaled = downscale(kurisu, (256, 256))
    kurisu_scaled.show()
