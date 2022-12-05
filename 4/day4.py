def getNumbers(string):
  elf1, partition, elf2 = string.partition(",")
  
  minElf1, partition2, maxElf1 = elf1.partition("-")
  minElf2, partition3, maxElf2 = elf2.partition("-")

  return int(minElf1), int(maxElf1), int(minElf2), int(maxElf2)

def fullyContains(minElf1, maxElf1, minElf2, maxElf2):
  if (minElf1 >= minElf2 and maxElf1 <= maxElf2) or (minElf2 >= minElf1 and maxElf2 <= maxElf1):
    return True
  return False

def overlap(minElf1, maxElf1, minElf2, maxElf2):
  if((minElf1 <= maxElf2 and maxElf1 >= minElf2) or (minElf1 >= maxElf2 and maxElf1 <= minElf2)):
    return True
  return False

numFullyContains = 0
with open("day4.txt", "r") as file:
  for line in file.readlines():
    minElf1, maxElf1, minElf2, maxElf2 = getNumbers(line)
    if(overlap(minElf1, maxElf1, minElf2, maxElf2)): # replace overlap with fullyContains here for part 1
      numFullyContains += 1

print(numFullyContains)
