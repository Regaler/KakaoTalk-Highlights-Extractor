 #-*- coding: utf-8 -*-
import sys
fori = open(sys.argv[1],'r')
fpart = open('./steppartitions.txt','r')
fout = open('./result.txt','w')

steplines = fpart.readlines()
def stripNsplit(x):
    x = x.strip('\n')
    x = x.split(' ')
    x[0] = (int)(x[0])
    x[1] = (int)(x[1])
    return x
steppartitions = map(stripNsplit, steplines)
#print (steppartitions)
isTitle = True
effective = False
for i, line in enumerate(fori):
    for elem in steppartitions:
        if i > elem[0] and i < elem[1]:
            effective = True
            break
        else:
            effective = False
    if effective == True:
        if isTitle == True:
            fout.write("\n\n\n***************************")
            fout.write("***************************\n")
            isTitle = False
        else:
            fout.write(line)
    else:
        if isTitle == False:
            isTitle = True
        continue

"""
    if i > steppartitions[0][0] and i < steppartitions[0][1]:
        #print(line)
        fout.write(line)
    elif (i > steppartitions[1][0]) and (i < steppartitions[1][1]):
        #print(line)
        fout.write(line)
    elif (i > steppartitions[2][0]) and (i < steppartitions[2][1]):
        #print(line)
        fout.write(line)
    else:
        continue
        """

fori.close()
fpart.close()
fout.close()
