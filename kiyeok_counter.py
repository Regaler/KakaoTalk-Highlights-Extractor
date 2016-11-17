#-*- coding: utf-8 -*-
"""Gets a text file, and count the number of kiyeoks for each lines."""
import sys
def kiyeok_counter():
    fin = open(sys.argv[1], 'r')
    fout = open('./featuredata.txt','w')
    while True:
        counter = 0
        line = fin.readline()
        if not line: break
        counter = line.count('ㅋ')
        fout.write(str(counter))
        fout.write('\n')
    fin.close()
    fout.close()

kiyeok_counter()
