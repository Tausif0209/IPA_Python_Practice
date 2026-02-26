ls=eval(input("Enter list of number"))
print(ls)
if len(ls)>1 and ls[0]==ls[-2] and ls[1]==ls[-1]:
  print("valid slice")