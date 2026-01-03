import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def manual_transpose(img):
    """
    Manually transpose an image array from (H, W, C) to (W, H, C)
    without using numpy transpose.
    """
    h, w, c = img.shape
    transposed = np.zeros((w, h, c), dtype=img.dtype)

    for y in range(h):
        for x in range(w):
            for ch in range(c):
                transposed[x][y][ch] = img[y][x][ch]

    return transposed


def main():
    try:
        img = ft_load("../animal.jpeg")

        if img.size == 0:
            return

        # Convert to grayscale
        gray = np.mean(img, axis=2, keepdims=True).astype(np.uint8)

        # Zoom (slice center area)
        zoomed = gray[200:600, 450:850]

        # Rotate (transpose)
        rotated = manual_transpose(zoomed)

        print(f"New shape after Transpose: {rotated.shape}")
        print(rotated)

        # Display image with axis scale
        plt.imshow(rotated.squeeze(), cmap="gray")
        # plt.xlabel("X axis (pixels)")
        # plt.ylabel("Y axis (pixels)")
        # plt.title("Rotated Image")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
