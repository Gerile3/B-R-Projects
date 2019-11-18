"""input = open('problem3input','r')
inputs = input.read().splitlines()
input.close()"""

import sys

inputs = sys.stdin.readlines()
inputs = [line.rstrip('\n') for line in inputs]

list = inputs[1:]
Numbers = inputs[:1]
sayı = [int(sub.split(' ')[0]) for sub in Numbers]
sayı2 = [int(sub.split(' ')[1]) for sub in Numbers]
mylist = []


for k in range(0,sayı2[0]):
    liste1 = [int(item[k]) for item in list]
    toplam = sum(liste1)
    if sayı[0]/2 < toplam <= sayı[0]:
        mylist.append(0)
    elif sayı[0]/2 >= toplam >= 0:
        mylist.append(1)
    
print("".join(str(x) for x in mylist))
