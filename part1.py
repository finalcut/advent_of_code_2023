import sys
import os

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
  with open(pathToFile) as f:
    lines = f.readlines()

  total = 0
  for line in lines:
    total = total + getCalibrationValueFromString(line)

  print(total)


sumCalibrationValues('data.txt')