import replace from Replace


string = input("Enter your string to format: ")
formatStrings = []
count = string.count("{")
for i in range(count):
  formatStrings.append(input(f"Enter {i} item to format: "))
print(string.format("heaven", "world"))

# Take a string "Hello {1} in the {0}.".format("heaven", "world") the output will be - Hello world in the heaven.

# # 💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻 Making our own format method using function 💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻

def format(string, *args):
  k=0
  indexList = []
  args = list(args)
  if(type(args[0]) == list):
    for i in args[0]:
      args.append(i)
    args.remove(args[0])
  formattedString = string
  while True:
    hasString = False
    index = 0
    try:
      i = formattedString.index("{")
      j = formattedString.index("}")
    except ValueError:
      break
    if j != i + 1:
      try:
        index = int(string[i+1 : j])
        indexList.append(index)
      except:
        hasString = True
    if hasString == False and j != i + 1:
      formattedString = replace(formattedString, formattedString[i : j+1], args[index], False)
      k-=1
    elif indexList.count(i) == 0:
      formattedString = replace(formattedString, formattedString[i : j+1], args[k], False)
    k+=1
  return formattedString
  # NOTE: Our format function doesn't change the original string.
  # You can also pass array as a collection of substrings to our format function whereas you can't in format method.

myString = format(string, [i for i in formatStrings])
print(myString)
