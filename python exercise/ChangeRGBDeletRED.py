from PIL import Image
im=Image.open("C:\\Users\\lanxiuting\\Desktop\\Learning-python\\me.jpg")
r,g,b=im.split()
om=Image.merge("RGB",(b,g,b))
om.save('me3.jpg')
