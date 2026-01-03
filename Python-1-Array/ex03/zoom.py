import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def main():
    try:
        img = ft_load("../animal.jpeg")

        if img.size == 0:
            return

        # Convert to grayscale
        gray = np.mean(img, axis=2, keepdims=True).astype(np.uint8)

        # Zoom (slice center area)
        zoomed = gray[200:600, 450:850]

        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)

        # Display image with axis scale
        plt.imshow(zoomed.squeeze(), cmap="gray")
        # plt.xlabel("X axis (pixels)")
        # plt.ylabel("Y axis (pixels)")
        # plt.title("Zoomed Image")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
