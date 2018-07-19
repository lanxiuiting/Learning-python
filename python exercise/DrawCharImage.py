#e12.1DrawCharImage.py
from PIL import Image
ascii_char=list('"$%_&WM#*oahkbdpqwmzO0QLCJUXYzcvunxr\jft/\|()1{}?-/+@<>i!;:,\^`.')
def get_char(r,b,g,alpha=256):
    if alpha==0:
        return''
    gray=int(0.2126*r+0.7125*g+0.0725*b)
    unit=256/len(ascii_char)
    return ascii_char[int(gray/unit)]
def main():
    im=Image.open("C:\\Users\\lanxiuting\\Desktop\\Learning-python\\astro.jpg")
    WIDTH,HEIGHT=100,60
    im=im.resize((WIDTH,HEIGHT))
    txt=""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt+= get_char(*im.getpixel((j,i)))
        txt +='\n'
    fo=open("pic_char.txt","w")
    fo.write(txt)
    fo.close()
main()
