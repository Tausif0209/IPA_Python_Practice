import logging
logging.basicConfig(
    filename="removeDuplicate.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
def removeduplicate(nums:list)->list:
  """
  Remove duplicate elements from a list while preserving the original order.

    Parameters:
        nums (list): Input list from which duplicates need to be removed

    Returns:
        list: New list containing only unique elements in original order
  """
  unique:set[int]=set()
  newlist:list[int]=[]
  for n in nums:
   if n not in unique:
     newlist.append(n)
     unique.add(n)
  return newlist
nums=eval(input("Enter list of number from user:-"))
logging.info(f"Orignal List:-{nums}\nAfter removing duplicates:-{removeduplicate(nums)}")
