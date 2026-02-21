import logging
logging.basicConfig(
  filename="missingnum.log",
  level=logging.INFO,
  format="%(asctime)s-%(levelname)s-%(message)s"
)

def missingnum(nums:list[int],N:int)->list[int]:
  """
  To find the missing number in a list containing number from 1 to N 
  Parameters:
    nums (list):Input List
    N (int):Range Limit
  Returns:
    list[int]:List of missing numbers
  
  """
  ans:list[int]=[]
  for i in range (1,N+1):
    if i not in nums:
      ans.append(i)
  return ans

N:int=int(input("Enter the value of N:-"))
nums:list[int]=eval(input("Enter list of number:-"))
logging.info(f"Orignal List:-{nums}\nList of missing numbers:-{missingnum(nums,N)}")

