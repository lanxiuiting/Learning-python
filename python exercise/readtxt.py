infile=open('read.txt',"r")
for i in range(5):
    line=infile.readline()
    print(line[:-1])
