#age.py
def get_age():
  while True:
      try:
        n=int(input('How old are you?'))
        return n
      except ValueError:
        print('Please enter a integer value.')
        
