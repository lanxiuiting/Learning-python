fo=open("C:\\Users\\lanxiuting\\Desktop\\Learning-python\\price2016.csv","r")
ls=[]
for line in fo:
    line=line.replace("\n","")
    ls.append(line.split(" "))
print(ls)
fo.close()
