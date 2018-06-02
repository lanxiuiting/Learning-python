def play_undercut(p1,p2):
  p1.reset_score()
  p2.reset_score()
  m1=p1.get_move()
  m2=p2.get_move()
  print("%s move:%s"%(p1.get_name(),m1))
  print("%s move:%s"%(p2.get_name(),m2))
  if m1==m2-1:
    p1.incr_score()
    return p1,p2,'%s wins!'%p1.get_name()
  elif m2== m1-1:
    return p1,p2,'%s wins!'%p2.get_name()
  else:
    return p1,p2,'draw:no winner'

class Human(Player):
  def __repr__(self):
    return'Human(%s)'%str(self)

def get_move(self):
  while True:
    try:
      n=int(input('%s move(1-10):'%self.get_name()))
      if 1<= n<=10:
        return n
      else:
        print('Oops!')
    except:
      print('Oops!')
import random #随机

class Computer(Player):
  def __repr__(self):
    return'Computer(%s)'%str(self)
  def get_move(self):
    return random.randint (1,10)

