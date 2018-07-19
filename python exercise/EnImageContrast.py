from PIL import Image
from PIL import ImageEnhance
im=Image.open("C:\\Users\\lanxiuting\\Desktop\\Learning-python\\me.jpg")
om=ImageEnhance.Contrast(im)
om.enhance(20).save("meEncontrast.jpg")
