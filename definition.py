#!/usr/bin/python
#coding=utf-8
#Add definition /etc/hosts For Linux System
import os

def add_defini():
    input = open('/etc/hosts', 'r')
    lines = input.readlines()
    input.close()

    output = open('/etc/hosts', 'w')
    for line in lines:
        if not line:
            break
        defini = line[0]
    #print defini
        if defini != '#':
            print line
            nf = '#' + line
            output.write(nf)
        else:
            output.write(line)
    output.close()
if __name__ == "__main__":
    add_defini()