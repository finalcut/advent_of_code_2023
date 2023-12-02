def loadFile(pathToFile):
  with open(pathToFile) as f:
    lines = f.readlines()
  return lines