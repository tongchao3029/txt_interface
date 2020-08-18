from ProjectVar import *


def getUniqueNumber():
    with open(UniqueNumberPath,"r+") as fp:
        num=fp.read()
        fp.seek(0,0)
        fp.write(str(int(num)+1))
        print("get uniquenumber done")
    return num

if __name__=="__main__":
    print(getUniqueNumber())