#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
def del_files(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            # print(name)
            if len(re.findall(r"\d", str(name))) != 0:
                print(int(''.join(re.findall(r"\d", str(name)))))
                if int(''.join(re.findall(r"\d", str(name)))) < 56254:
                    os.remove(os.path.join(root, name))
                    print("Delete File: " + os.path.join(root, name))
# test
if __name__ == "__main__":
    path = os.getcwd()
    del_files(path)