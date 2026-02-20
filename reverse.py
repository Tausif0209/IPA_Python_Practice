import logging
logging.basicConfig(
  filename="reverse.log",
  level=logging.INFO,
  format="%(asctime)s-%(levelname)s-%(message)s"
)
def reverse(s:str)->str:
  """
  To reverse string using for loop
  Parameters:
   s(str):Input String
  Returns:
    str:Reverse String
  """
  rev=""
  for i in range (len(s)-1,-1,-1):
    rev=rev+s[i]
  return rev
s=input("Enter String:-")
logging.info(reverse(s))