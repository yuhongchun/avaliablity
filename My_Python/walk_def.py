#!/usr/bin/python
import os

def VisitDir(path):
    for root,dirs,files in os.walk(path):
        for filepath in files:
            print os.path.join(root,filepath)

if __name__ == "__main__":
    path = "c:\windows"
    VisitDir(path)