from PIL import ImageOps, ImageEnhance, ImageChops, ImageFilter
import numpy as np
import cv2
from PIL import Image

def black_white(image):
    """Change image to greyscale."""
    return ImageOps.grayscale(image)


def glassial_blur(image, amount=1):
    """Blur image."""
    im = image.filter(ImageFilter.GaussianBlur(radius=amount))
    return im


def desaturate(image, amount=.9):
    """Reduce vibrance."""
    enhanced = ImageEnhance.Color(image)
    return enhanced.enhance(amount)


def saturate(image, amount=1.1):
    """Increase vibrance."""
    enhanced = ImageEnhance.Color(image)
    return enhanced.enhance(amount)


def sharpness(image, amount=1.1):
    """Shapen edges of an image."""
    enhanced = ImageEnhance.Sharpness(image)
    return enhanced.enhance(amount)


def contrast(image, amount=1.1):
    """Adjust ."""
    enhanced = ImageEnhance.Contrast(image)
    return enhanced.enhance(amount)
    

def invert(image):
    """Invert the image."""
    return ImageChops.invert(image)


def denoise(image_path):
    img = cv2.imread(image_path)
    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    image = Image.fromarray(dst)
    return image
    
    
# Create list  to handle respective effects
effect = {
    "greyscale": black_white,
    "blur": glassial_blur,
    "desaturate": desaturate,
    "saturate": saturate,
    "sharpness": sharpness,
    "contrast": contrast,
    "invert": invert,
    "denoise": denoise,
    
   
}
