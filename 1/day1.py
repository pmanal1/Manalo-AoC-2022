file = open("day1.txt", "r")
# use int(example) to turn the read string into something
# a separate elf means empty string
# need a list of elves and total calories
  # each entry in list represent total calories for one elf

totalCalories = []
currentElf = 0

for line in file:
  if(line == "\n"):
    totalCalories.append(currentElf)
    currentElf = 0
  else:
    currentElf += int(line)

print(totalCalories)
elf1 = max(totalCalories)
totalCalories.remove(max(totalCalories))
elf2 = max(totalCalories)
totalCalories.remove(max(totalCalories))
elf3 = max(totalCalories)
totalCalories.remove(max(totalCalories))

print(elf1 + elf2 + elf3)

# print(example)
# print(int(example))
# print(type(example))
# print(type(int(example)))