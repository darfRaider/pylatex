import os
class Plot:

  def __init__(self, figureDir: str = "./out/figures"):
    self.figureDir = figureDir
    if not os.path.exists(figureDir):
      os.makedirs(figureDir)