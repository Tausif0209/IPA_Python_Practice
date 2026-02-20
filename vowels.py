import logging
logging.basicConfig(
    filename="vowels.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def vowelCount(s:str)->int:
  """
  Count the number of vowels in a given string.
    Parameters:
        s (str): Input string
    Returns:
        int: Total number of vowels in the string.
  """
  vowels=0
  for ch in s:
    if ch.lower() in "aeiou":
     vowels+=1
  return vowels  
s=input("Enter a String:-")
if len(s)==0:logging.error("Empty String")
else:logging.info(f"String:-{s} vowels count:-{vowelCount(s)}")