import requests
import json
#requests.get()
#url=http://t.api.letv.cn/mms/inner/albumInfo/getLiveWaterMark?cid=2&platform=upload
#requests.post

class HttpClient():

    def get(self,url,paramType,params,**kwargs):
        if paramType=="url":
            print("urlxxxxxxxxxxxxx",url + params)
            res = requests.get(url + params)
        elif paramType=="params":
            res=requests.get(url,eval(params))
        return res

    def post(self,url, paramsType,params, **kwargs):
        if paramsType=="data":
            res=requests.post(url,data=eval(json.dumps(params)))
        elif paramsType=="json":
            res = requests.post(url, json=eval(params))
        return res

    def put(self,url,paramsType,params,**kwargs):
        if paramsType=="data":
            res=requests.put(url,data=eval(json.dumps(params)))
        elif paramsType=="json":
            res=requests.put(url,json=eval(params))
        return res





if __name__=="__main__":
    hc=HttpClient()
    # res=hc.get("http://t.api.letv.cn/mms/inner/albumInfo/getLiveWaterMark","params",'{"cid":2,"platform":"upload"}')
    # print(res.json())
    # res = hc.get("http://39.100.104.214:8080/getBlogContent","url","1")
    # print(res.json())
    # res = hc.post("http://39.100.104.214:8080/register/","json",'{"username":"aaaadddd111","password":"lilyd2222","email":"lily@qq.com"}')
    # print(res.json())
    res=hc.put("http://39.100.104.214:8080/update/","json",'{"userid":972, "token": "6c85a22b9f6c1f7e336782891dc7060e", "articleId":170, "title":"java", "content":"i lova java"}')
    print(res.json())