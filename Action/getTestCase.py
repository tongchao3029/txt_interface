from ProjectVar import *

def getTestCase(testfilepath):
    with open(testfilepath,encoding="utf-8") as fp:
        content=fp.readlines()
    #兼容过滤不需要测试case
    testcase=[ i.split("||") for i in content if not i.startswith("#")]
    return testcase


if __name__=="__main__":
    print(getTestCase(TestDataPath))