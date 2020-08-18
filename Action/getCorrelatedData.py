import re
import json


# 适用于新建一条博文
# def getCorrelatedData(params,datasource):
#     if re.findall(r"%r{(\w+)}",params):
#         for var in re.findall(r"%r{(\w+)}",params):
#             #通过2次的转化主要是使替换的数据和data_rely中存储的类型一致
#             params = json.loads(params)
#             print(var)
#             #params=re.sub("%{\w+}",datasource[var],params,1)
#             params[var]=datasource[var]
#             print(params)
#             params=json.dumps(params)
#
#     return params

def getCorrelatedData(params,datasource):
    params = json.loads(params)
    if isinstance(params,dict):
        for k,v in params.items():
            print("v", v)
            print(type(v))
            if "%" in v and isinstance(v,str):
                params[k]=datasource[re.search("%{(\w+)}",str(params)).group(1)]
                print("替换中的参数--->",params)
            if "%" in str(v) and isinstance(v,list):
                print("v",v)
                print(type(v))
                for idx,value in enumerate(v):
                    v[idx]=datasource[re.search("%{(\w+)}",str(v)).group(1)]
                params[k]=v
        params = json.dumps(params)
    elif isinstance(params,str):
        for var in re.findall("%{(\w+)}",params):
            params=re.sub("%{\w+}",str(datasource[re.search("%{(\w+)}",params).group(1)]),params,1)
    print("替换后的参数--->", params)
    return params

if __name__=="__main__":
    print(getCorrelatedData('{"userid":"%{userid}", "token":"%{token}", "title":"python", "content":"python port test"}',
                      {'num': '67', 'userid': 888, 'token': '6c2209243bced47dd2596f282a64e0ac'}))