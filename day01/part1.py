import sys
import os


# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)
from utils import loadFile

numbers = "0123456789"


def getNumberFromString(str):
  for char in str:
    if char in numbers:
      return char

def getCalibrationValueFromString(str):
  x = getNumberFromString(str)
  y = getNumberFromString(reversed(str))

  cali = x + y
  return int(cali)

def sumCalibrationValues(pathToFile):
  lines = loadFile(pathToFile)

  total = 0
  for line in lines:
    total = total + getCalibrationValueFromString(line)

  print(total)


sumCalibrationValues('data.txt')