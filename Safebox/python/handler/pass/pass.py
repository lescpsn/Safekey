#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

################################################################################
def Passfile_init():
    pass

################################################################################
def Record_Read():
    print("==== Enter:", Record_Read)
    with open("pass.json","rb+") as f:
        d = json.load(f)

    bstr = json.dumps(d)
    print(bstr)

################################################################################
def Record_Write():
    print("==== Enter:", Record_Write)
    with open("pass.json", "rb+") as f:
        d = json.load(f)

    print(type(d),d)

################################################################################
def Pass_Test():
    Record_Read()
    Record_Write()



################################################################################
if __name__ == '__main__':
    Pass_Test()