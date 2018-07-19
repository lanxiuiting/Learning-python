from PIL import Image
from PIL import ImageFilter
im= Image.open("C:\\Users\\lanxiuting\\Desktop\\Learning-python\\me.jpg")
om=im.filter(ImageFilter.CONTOUR)
om.save("metto.jpg")
