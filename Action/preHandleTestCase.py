import re
from ProjectVar import *
from Utils.getUniqueNumber import *
from Utils.md5Encrypt import *
from Utils.getUniqueNumber import *

def preHandleTestCase(params):
    for var in re.findall("\${(.*?)}", params):
        if var == "uniquenumber":
            uniquenum = getUniqueNumber()
            params = re.sub("\${.*?}", uniquenum, params)
            data_rely["num"] = uniquenum
            print("params1", params)
        elif var == "num":
            params = re.sub("\${\w+}", data_rely["num"], params)
            print("params2", params)
        elif re.search("\(.*?\)", var):
            params = re.sub("\${.*?}", eval(var),params)
            print("params3", params)
    print("处理后的params--------->",params)
    return params

if __name__=="__main__":
    preHandleTestCase('{"username":"testman2020${uniquenumber}","password":"qwer1234","email": "testman@qq.com"}')
    preHandleTestCase('{"username":"testman2020${num}","password":"${get_md5(\'qwer1234\')}"}')

