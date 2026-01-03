from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """
    Load an image, print its shape and pixel content in RGB format.

    Supported formats:
    - JPG
    - JPEG

    Parameters:
    path (str): Path to the image file.

    Returns:
    np.ndarray: Image pixels as a NumPy array.
                Returns an empty array if an error occurs.
    """
    try:
        img = Image.open(path)

        if img.format not in ("JPEG", "JPG"):
            print("Error: Unsupported image format (only JPG and JPEG are allowed)")
            return np.array([])

        img = img.convert("RGB")
        pixels = np.array(img)

        print(f"The shape of image is: {pixels.shape}")
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
