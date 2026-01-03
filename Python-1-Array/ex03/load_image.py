from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image, print its shape and pixel content.

    Parameters:
    path (str): Path to the image file.

    Returns:
    np.ndarray: Image pixels as a NumPy array.
                Returns an empty array if an error occurs.
    """
    try:
        img = Image.open(path)
        img = img.convert("RGB")
        pixels = np.array(img)

        print(f"The shape of image is: {pixels.shape}")
        print(pixels)

        return pixels

    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print("Error: Permission denied")
    except OSError:
        print("Error: Invalid image file")
    except Exception as e:
        print(f"Error: {e}")

    return np.array([])
