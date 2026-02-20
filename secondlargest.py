import logging
logging.basicConfig(
  filename="secondLargest.log",
  level=logging.INFO,
  format="%(asctime)s-%(levelname)s-%(message)s")
def secondLargest(nums:set)->int:
  """
  Find the second largest element in a list using a for loop
    Parameters:
        nums (set): Input set of distinct elements
    Returns:
        int: Second largest element in a list.
  """
  largest,secondLargest= float('-inf'),float('-inf')
  for num in nums:
    if num>largest:
      secondLargest=largest
      largest=num
    elif num<largest:
      secondLargest=max(secondLargest,num)
  return secondLargest
nums=set(eval(input("Enter list of numbers:-")))
if len(nums)<2:logging.error("Less than two distinct elements")
else:logging.info(f"second largest element:-{secondLargest(nums)
}")
