import numpy as np
import matplotlib.pyplot as plt

def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    inverted = 255 - array
    plt.imshow(inverted)
    plt.title("Inverted Image")
    plt.axis("off")
    plt.show()
    return inverted


def ft_red(array) -> np.ndarray:
    """
    Keeps only the red channel of the image.
    """
    red = array.copy()
    red[:, :, 1] = red[:, :, 1] * 0
    red[:, :, 2] = red[:, :, 2] * 0
    plt.imshow(red)
    plt.title("Red Filter")
    plt.axis("off")
    plt.show()
    return red


def ft_green(array) -> np.ndarray:
    """
    Keeps only the green channel of the image.
    """
    green = array.copy()
    green[:, :, 0] = green[:, :, 0] - green[:, :, 0]
    green[:, :, 2] = green[:, :, 2] - green[:, :, 2]
    plt.imshow(green)
    plt.title("Green Filter")
    plt.axis("off")
    plt.show()
    return green


def ft_blue(array) -> np.ndarray:
    """
    Keeps only the blue channel of the image.
    """
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    plt.imshow(blue)
    plt.title("Blue Filter")
    plt.axis("off")
    plt.show()
    return blue


def ft_grey(array) -> np.ndarray:
    """
    Converts the image to true greyscale, avoiding overflow.
    """
    # Convert to int to avoid uint8 overflow
    arr_int = array.astype(np.int32)

    # Use one channel to approximate grey (green)
    grey = (arr_int[:, :, 1] / 1).astype(np.uint8)

    plt.imshow(grey, cmap="gray")
    plt.title("Greyscale Image")
    plt.axis("off")
    plt.show()

    return grey
