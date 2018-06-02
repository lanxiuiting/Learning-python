#read.py
def is_gif(fname):
  f=open(fname,'br')
  first4=tuple(f.read(4))
  return first4==(0*47,0*49,0*46,0*38)
