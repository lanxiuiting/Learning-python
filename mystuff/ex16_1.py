from sys import argv

script,filename=argv
txt=open(filename)
print "opening the file %r."%filename
print txt.read()
txt.close()
