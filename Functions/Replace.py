if(__name__ == '__main__'):
  string = input("Enter your string: ")
  wordToReplace = input("Word to replace: ")
  wordToReplaceWith = input("Word to replace with: ")
  print(string.replace(wordToReplace, wordToReplaceWith))

# 💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻 Making our own replace function 💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻💪🏻


def replace(string, toReplace, replaceWith, repAll=True):
  count=0
  fore=""
  dummyString=""
  replacedString=""
  strList = string.split()
  for i in strList:
    dummyString = str(i)
    if(dummyString == toReplace or dummyString.find(toReplace) != -1):
      fore=dummyString[0:dummyString.find(toReplace)]
      if(count==0):
        replacedString+="{}{}{}".format(fore, replaceWith, dummyString[len(toReplace+fore):dummyString.__len__()])
      else:
        replacedString+=f" {fore}{replaceWith}{dummyString[len(toReplace+fore):dummyString.__len__()]}"
      if(repAll == False):
        replacedString+=string[len(string[0:string.find(toReplace)]+toReplace+dummyString[len(toReplace+fore):dummyString.__len__()]):]
        break
    else:
      if(count==0):
        replacedString+=dummyString
      else:
        replacedString+=" "+dummyString
    count+=1
  return replacedString
  # NOTE: Our replace function doesn't change the original string.
if(__name__ == '__main__'):
  print(replace(string, wordToReplace, wordToReplaceWith))
  
