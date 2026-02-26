import logging
logging.basicConfig(
  filename="sorted.log",
  level=logging.INFO,
  format="%(asctime)s-%(levelname)s-%(message)s")
def isSorted(nums:list)->bool:
  """
  To check whether the given list is sorterd in ascending order or not
  Parameters:
    nums (list):Input List
  Returns:
    bool:True if list is sorted in ascending order,otherwise false

  """
  for i in range (1,len(nums)):
    if nums[i]<nums[i-1]:
      return False 
  return True
nums=eval(input("Enter list:-"))
if len(nums)==0:logging.error("Empty List")
else:
  if isSorted(nums):
   logging.info(f"List is sorted {nums}")
  else:logging.warning(f"List is not sorted{nums}")