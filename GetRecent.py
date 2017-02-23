import os
import glob

files = [os.path.join('C:\\',x) for x in os.listdir('C:\\') if x.endswith('.log')]

newest = max(files,key = os.path.getctime)

print(newest)
