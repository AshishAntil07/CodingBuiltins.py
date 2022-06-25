from functools import reduce

l = [1, 2, 3, 4, 5]
val = reduce(lambda num1, num2: num1+num2, l)
print(val)

# 💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻 Making our own reduce function 💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻

def reduce(func, iterable, argCount=2):
  def sliceList(iterable, startIndex):
    poppedList = []
    for index, i in enumerate(range(startIndex, iterable.__len__())):
      if index >= argCount-1:
        break
      poppedList.append(iterable[i])
    if(poppedList.__len__() == argCount-1):
      return poppedList
  iterCount=0
  Any = iterable[0]
  while True:
    try:
      iterCount+=1
      Sliced_List = sliceList(iterable, iterCount)
      if(argCount > 2):
        Any = func(Any, Sliced_List)
      else:
        Any = func(Any, iterable[iterCount])
    except:
      return Any

def function(num1, num2):
  return num1+num2[0]+num2[1]

# NOTE: If you are taking arguments more than 2, the 2nd argument will be in the form of a list.
val = reduce(function, l, 3)
