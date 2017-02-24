import os
import glob
import locale

locale.setlocale (locale.LC_ALL,'')
'English_United States.1252'

isk = 225000
tip = 20000
charName = ""

logPath = ""
files = [os.path.join(logPath,x) for x in os.listdir(logPath) if x.endswith('.txt')]
newest = max(files,key = os.path.getctime)

for j in files:
    if j != newest:
        os.remove(j)

blocks = 0

f = open(newest,"r")
search = f.readlines()
f.close()

for i in search:
    if charName in i and i.split("\t")[4]=="Ice":
        amount = i.split('\t')[3]
        blocks += int(amount)
        print(i)
print("Weekly isk/block is: "+locale.currency(isk,grouping=True))
print("Weekly tip is: "+locale.currency(tip,grouping=True))
print("Per Block Amount: "+locale.currency(isk-tip,grouping=True))
print("You looted: "+str(blocks)+" blocks of ice.")
print("It is worth: "+locale.currency((isk-tip)*blocks,grouping=True))
