from PIL import ImageOps
from PIL import Image


def flip(image):
    """Flip image."""
    return ImageOps.flip(image)

def rotate(image):
    """Rotate image by 25 degrees."""
    return image.rotate(90)

def resize(image):
    img = image.resize((200,400), Image.ANTIALIAS)
    return img

def imagefit(image):
    if image.mode not in ("L", "RGB"):
        image = image.convert("RGB")
    imagefit = ImageOps.fit(image, (300, 300), Image.ANTIALIAS)
    return imagefit
    
def crop(image):
    img = image.crop( (100,10,400,400) )
    return img
       
meffect = {
    "flip": flip,
    "rotate": rotate,
    "imagefit":imagefit,
    "resize":resize,
    "crop" : crop,
}
