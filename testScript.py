from Action.preHandleTestCase import *
from Utils.httpClient import *
from Action.getTestCase import *
from ServerInfo import *
from Action.storeData import *
from Action.getCorrelatedData import *
from ProjectVar import *
from Utils.assertResult import *
import time
from Utils.htmlReport import *
from Utils.sendMail import *
from Utils.DateAndTime import *
import logging.config
import logging

logging.config.fileConfig("Config\\Logger.conf")
logger = logging.getLogger("mylogger01")


def main():
    passed_case = 0
    failed_case = 0
    total_case = 0
    test_case_result=""
    cases=getTestCase(TestDataPath)
    hc=HttpClient()
    for case_num,case in enumerate(cases,1):
        total_case+=1
        request_url = case[request_url_no]
        http_method = case[http_method_no]
        params = case[params_no]
        params_type= case[params_type_no]
        assert_keyword = case[assert_keyword_no]
        assert_keywordinfo = case[assert_keywordinfo_no].strip()
        logger.debug("当前测试用例--->request_url:%s, http_method:%s,params:%s, params_type:%s,assert_keyword:%s,assert_keywordinfo:%s" %(request_url, http_method,params, params_type, assert_keyword, assert_keywordinfo))
        if "$" in params:
            logger.info("-" * 10 + "处理请求参数" + "-" * 10)
            params=preHandleTestCase(params)
            print(params)
        elif "%" in params:
            logger.info("-" * 10 + "处理关联参数" + "-" * 10)
            params=getCorrelatedData(params,data_rely)
        if http_method.lower()=="get":
            start=time.time()
            res=hc.get(eval(request_url),params_type,params)
            end=time.time()
            eplased_time=int((end-start)*1000)
            #print("sssssssssssss",eplased_time)
            print(res.text)
        elif http_method.lower()=="post":
            start = time.time()
            res=hc.post(eval(request_url),params_type,params)
            end = time.time()
            print(res.text)
            eplased_time = int((end - start) * 1000)
            print("eplased_time[%s]ms"%eplased_time)
        elif http_method.lower()=="put":
            start = time.time()
            res=hc.put(eval(request_url),params_type,params)
            end = time.time()
            print(res.text)
            eplased_time = int((end - start) * 1000)
            print("eplased_time[%s]ms"%eplased_time)
        if "--->" in assert_keywordinfo:
            logger.info("-"*10+"处理响应数据"+"-"*10)
            storeData(assert_keywordinfo, res.text)
            logger.info("数据存储--->data_rely:%s"%data_rely)
        logger.info("-" * 10 + "断言响应结果" + "-" * 10)
        if assertResult(assert_keyword,res):
            passed_case+=1
            test_case_result="pass"
            print("case %s"%test_case_result)
        else:
            failed_case+=1
            test_case_result="fail"
            print("case %s"%test_case_result)
        test_results.append((case_num,res.url,params,res.text,eplased_time,assert_keyword,test_case_result))


    print(test_results)
    print(data_rely)
    print("total_case[%s] passed_case[%s] failed_case[%s]"%(total_case,passed_case,failed_case))





if __name__=="__main__":
    main()
    timer=TimeUtil()
    html_name = '接口测试报告'+timer.get_date()
    report_html(test_results, html_name)
    content="Hi all,\n接口测试已经完成，详情请查看附件!"+("\n"*5)+"Br\nTongChao"
    # try:
    #     sendMail(content,os.path.join(ResultPath,html_name+".html"),["222222222@qq.com"])
    # except Exception as e:
    #     print(e)
