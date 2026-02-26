import logging
logging.basicConfig(
  filename="frequency.log",
  level=logging.INFO,
  format="%(asctime)s-%(levelname)s-%(message)s")
def fre(key:str,s:str)->int:
  """
  Count the frequency of given character  in a given string.
    Parameters:
        key(str):Character for which frequency needed to be calculated
        s (str): Input string
    Returns:
        int: frequency of given character.
  """
  count=0
  for ch in s:
    if key==ch:count+=1
  return count
s=input("Enter a String:-")
unique=set()
for ch in s:
 if ch not in unique: 
   logging.info(f"{ch} frequency:-{fre(ch,s)}")
   unique.add(ch)