#codesum.py
def codesum1(s):
  """ Returns the sums of the character codes of s."""
  total=0
  for c in s:
    total =total +ord(c)
  return total
