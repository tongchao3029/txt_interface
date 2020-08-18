from ProjectVar import *
import re



def storeData(storedatainfo,response):
    storevar_name=storedatainfo.split("--->")[0]
    regx=storedatainfo.split("--->")[1]
    #userid & articleId 的数据类型是int
    print("wwwwwwwwwwwwwwwwww",regx)
    if storevar_name=="userid":
        data_rely[storevar_name] = int(re.search(regx, response).group(1))
    elif storevar_name.startswith("articleId"):
        data_rely[storevar_name] = int(re.search(regx, response).group(1))
    else:
        data_rely[storevar_name]=re.search(regx,response).group(1)


if __name__=="__main__":
    storeData('token--->"token": "(\w+)"','{"token": "c4aee3dffdf87d8ee7c97c815a6c762e", "code": "00", "userid": 853, "login_time": "2020-07-01 18:19:47"}')
