# For some unholy reason the first line wasn't being read.... (see **)

# A - X - Rock - 1
# B - Y - Paper - 2
# C - Z - Scissors - 3

# Loss - 0 - X
# Draw - 3 - Y
# Win - 6 - Z

file = open("day2.txt", "r")
totalScore = 0

for line in file: # ** I found the error, it's here in for line in file. **
  # Get the round
  elf = file.read(1)
  file.read(1)
  you = file.read(1)
  result = you

  # Translate choices into score numbers for simplicity
  if(elf == "A"):
    elf = 1
  elif(elf == "B"):
    elf = 2
  elif(elf == "C"):
    elf = 3
  else:
    print("error")
  
  # Part 1
  # if(you == "X"):
  #   you = 1
  # elif(you == "Y"):
  #   you = 2
  # elif(you == "Z"):
  #   you = 3
  # else:
  #   print("error")

  # Part 2
  if(result == "X"):
    result = 0
  elif(result == "Y"):
    result = 3
  elif(result == "Z"):
    result = 6
  else:
    print("error")

  # Part 1
  # Decide the score for this line
  # if((elf == 1 and you == 2) or (elf == 2 and you == 3) or (elf == 3 and you == 1)): # You Win
  #   totalScore += you + 6
  # elif((elf == 1 and you == 1) or (elf == 2 and you == 2) or (elf == 3 and you == 3)): # Draw
  #   totalScore += you + 3
  # elif((elf == 1 and you == 3) or (elf == 2 and you == 1) or (elf == 3 and you == 2)): # You Lose
  #   totalScore += you
  # else:
  #   print("error")

  # Part 2
  if((elf == 1 and result == 3) or (elf == 2 and result == 0) or (elf == 3 and result == 6)): # You chose Rock
    totalScore += 1 + result
  elif((elf == 1 and result == 6) or (elf == 2 and result == 3) or (elf == 3 and result == 0)): # You chose Paper
    totalScore += 2 + result
  elif((elf == 1 and result == 0) or (elf == 2 and result == 6) or (elf == 3 and result == 3)): # You chose Scissors
    totalScore += 3 + result
  else:
    print("error")


print(totalScore)

