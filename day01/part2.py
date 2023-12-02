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
numbers = {
 "zero": "0",
 "one": "1",
 "two": "2",
 "three": "3",
 "four": "4",
 "five": "5",
 "six": "6",
 "seven": "7",
 "eight": "8",
 "nine": "9"
}


def getNumberFromReversedString(str):
  rstr = ''.join(reversed(str))
  index = len(str)
  num = ""

  for key, value in numbers.items():
    rkey = ''.join(reversed(key))
    if rkey in rstr:
      tempindex = rstr.index(rkey)
      if tempindex < index:
        index = tempindex
        num = value
    if value in rstr:
      tempindex = rstr.index(value)
      if tempindex < index:
        index = tempindex
        num = value

  return num

def getNumberFromString(str):
  index = len(str)
  num = ""

  for key, value in numbers.items():
    if key in str:
      tempindex = str.index(key)
      if tempindex < index:
        index = tempindex
        num = value
    if value in str:
      tempindex = str.index(value)
      if tempindex < index:
        index = tempindex
        num = value
  return num


def getCalibrationValueFromString(str):
  x = getNumberFromString(str)
  y = getNumberFromReversedString(str)
  cali = x + y
  return int(cali)

def sumCalibrationValues(pathToFile):
  lines = loadFile(pathToFile)

  total = 0
  for line in lines:
    total = total + getCalibrationValueFromString(line)

  print(total)


sumCalibrationValues('data.txt')