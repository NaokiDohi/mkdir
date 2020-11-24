import os

path = 'RNN'
if not os.path.exists(path):
  os.mkdir(path)
else:
  print("Dude!! This dir is already existed!!")

path = 'RNN/log'
if not os.path.exists(path):
  os.mkdir(path)
else:
  print("Dude!! This dir is already existed!!")
