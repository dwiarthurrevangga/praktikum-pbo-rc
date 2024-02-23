height = int(input("Height : "))

for triangle in range (1, height + 1) :
  print (" " * (height - triangle) + "*" * (2 * triangle - 1))
