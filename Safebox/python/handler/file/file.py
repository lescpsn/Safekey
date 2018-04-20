#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
def File_Encrypt(srcPlainFile, dstEncFile):
    with open(dstEncFile,'wb') as df:
        with open(srcPlainFile,'rb') as sf:
            for buf in sf:
                df.write(buf)

################################################################################
def File_Decrypt(srcEncFile, dstPlainFile):
    with open(dstPlainFile,'wb') as df:
        with open(srcEncFile,'rb') as sf:
            for buf in sf:
                df.write(buf)


################################################################################
def File_Test():
    File_Encrypt("test.txt", "e.test.txt")
    File_Decrypt("e.test.txt", "d.test.txt")


################################################################################
if __name__ == '__main__':
    File_Test()