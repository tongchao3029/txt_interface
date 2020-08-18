#encoding=utf-8

from bottle import template
import os
from ProjectVar import *

def report_html(data,html_name):
    template_demo = """
    <!-- CSS goes in the document HEAD or added to your external stylesheet -->
    <style type="text/css">
table.hovertable {
    font-family: verdana,arial,sans-serif;
    font-size:11px;
    color:#333333;
    border-width: 1px;
    border-color: #999999;
    border-collapse: collapse;
}
table.hovertable th {
    background-color:#ff6347;
    border-width: 1px;
    padding: 8px;
    border-style: solid;
    border-color: #a9c6c9;
}
table.hovertable tr {
    background-color:#d4e3e5;
}
table.hovertable td {
    border-width: 1px;
    padding: 8px;
    border-style: solid;
    border-color: #a9c6c9;
}
</style>

<!-- Table goes in the document BODY -->

<head>

<meta http-equiv="content-type" content="txt/html; charset=utf-8" />

</head>

<table class="hovertable">
<tr>
    <th>#</th><th>接口 URL</th><th>请求数据</th><th>接口响应数据</th><th>接口调用耗时(单位：ms)</th><th>断言关键字</th><th>测试结果</th>
</tr>
% for case_num,url,request_data,response_data,test_time,assert_word,result in items:
<tr onmouseover="this.style.backgroundColor='#ffff66';" onmouseout="this.style.backgroundColor='#d4e3e5';">

    <td>{{case_num}}</td><td>{{url}}</td><td>{{request_data}}</td><td>{{response_data}}</td><td>{{test_time}}</td><td>{{assert_word}}</td><td>
    % if result == 'pass':
    <font color=green>
    %elif result=="fail":
    <font color=red>
    % end
    <b>{{result}}</b></td>
</tr>
% end
</table>
    """
    html = template(template_demo, items=data)
    with open(os.path.join(ResultPath,html_name+".html"), 'wb') as fp:
        fp.write(html.encode('utf-8'))

#测试数据
if __name__ == '__main__':
    data = [(1,'http://39.106.41.11:8080/register/', '{"username": "tiansl2831", "password": "xiaoli123451", "email": "xiaoli@qq.com"}','{"username": "tiansl2831", "code": "01"}',"5ms","00", 'pass')]
    html_name = '接口测试报告'
    report_html(data,html_name)

