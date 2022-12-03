# finds any char in str1 that is also in str2
def findCommonItem(str1, str2):
  for char in str1:
    if char in str2:
      return char

# turns single character strings into given ints
def convertPriorities(char):
  if char == char.lower():
    return ord(char) - 96 # this is to get a started at 1
  elif char == char.upper():
    return ord(char) - 38 # this is to get A started at 27
  else:
    print("error")

def findBadge(str1, str2, str3):
  for char in str1:
    if char in str2 and char in str3:
      return char

prioritiesSum = 0
groupOfThree = []
with open("day3.txt") as file:
  # Part 1
  # for line in file:
  #   commonItem = findCommonItem(line[:len(line)//2], line[len(line)//2:])
  #   prioritiesSum += convertPriorities(commonItem)

  # Part 2
  for line in file:
    if(len(groupOfThree) == 3):
      commonItem = findBadge(groupOfThree[0], groupOfThree[1], groupOfThree[2])
      prioritiesSum += convertPriorities(commonItem)
      groupOfThree = [line.replace("\n", "")]
    else:
      groupOfThree.append(line.replace("\n", ""))

# Part 2 - Running this step again since the last group of three does not run
commonItem = findBadge(groupOfThree[0], groupOfThree[1], groupOfThree[2])
prioritiesSum += convertPriorities(commonItem)

print(prioritiesSum)