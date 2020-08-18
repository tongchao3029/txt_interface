import os

ProjectPath=os.path.abspath(os.path.dirname(__file__))
UniqueNumberPath=os.path.join(ProjectPath,"TestData\\uniquenumber")
TestDataPath=os.path.join(ProjectPath,"TestData\\testdata")
ResultPath=os.path.join(ProjectPath,"Result")

data_rely={}

failed_case=0
passed_case=0
total_case=0

test_results=[]

#create||POST||{"userid":"%{userid}", "token":"%{token}", "title":"python", "content":"python port test"}||json||"code": "00"||None
#[testcase_info]
request_url_no=0
http_method_no=1
params_no=2
params_type_no=3
assert_keyword_no=4
assert_keywordinfo_no=5





if __name__=="__main__":
    print(ProjectPath)