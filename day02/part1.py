import sys
import os

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

limits = {
  "red": 0,
  "green": 0,
  "blue": 0
}

def setLimits(r,g,b):
  limits["red"] = r
  limits["green"] = g
  limits["blue"] = b

# adding the parent directory to
# the sys.path.
sys.path.append(parent)
from utils import loadFile


def solve(filePath, r, g, b):
  setLimits(r,g,b)
  lines = loadFile(filePath)

  total = 0

  for line in lines:
    data = line.split(":")
    x = data[0].split(" ")

    id = int(x[1])

    isValid = True

    sets = data[1].split(";")
    for set in sets:
      games = set.split(",")
      for game in games:
        game = game.strip()
        parts = game.split(" ")
        num = int(parts[0])
        color = parts[1]

        if num > limits[color]:
          isValid = False

    if isValid:
      total = total + id

  return total

test = solve('test.txt', 12, 13, 14)
if test == 8:
  print("test passed: " + str(test))

part1 = solve('data.txt', 12, 13, 14)
print(part1)