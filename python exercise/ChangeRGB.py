from PIL import Image
im=Image.open("C:\\Users\\lanxiuting\\Desktop\\Learning-python\\me.jpg")
r,g,b=im.split()
om=Image.merge("RGB",(b,g,r))
om.save('me2.jpg')
