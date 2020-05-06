from k9_multipart.login_xmind import  login_fuc
from requests_toolbelt import MultipartEncoder
import  requests
from lxml import etree
import re



def add_teacher_name(s):
    url = "http://49.235.92.12:8020/xadmin/hello/teacher/add/"
    r = s.get(url)
    token = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", r.text)
    print(token[0])


    body = MultipartEncoder(
        fields=[
            ('csrfmiddlewaretoken', token[0]),
            ('csrfmiddlewaretoken', token[0]),
            ('teacher_name',  'testhahaah123235'),
            ("tel", "1237475757"),
            ('mail', 'test@qq.com'),
            ('sex', 'M',),
            ('_save', '')
            ]
    )
    r2 = s.post(url, data=body, headers={"Content-Type": body.content_type})
    # print(r2.text)
    return r2.text


def get_add_result(text):
    demo = etree.HTML(text)
    nodes = demo.xpath('/html/body/div[2]/div[2]/form/div[1]/table/tbody/tr[1]/td[2]/a')
    get_result = nodes[0].text
    print(get_result)
    return get_result

s = requests.session()
login_fuc(s)
url3 = "http://49.235.92.12:8020/xadmin/hello/fileimage/add/"
r = s.get(url3)
csrftoken = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", r.text)
print(csrftoken)
body3 = MultipartEncoder(
    fields=[
            ('csrfmiddlewaretoken', csrftoken[0]),
            ('csrfmiddlewaretoken', csrftoken[0]),
            ('title',  '上传图片hahaah'),
            ("image", ('testhahaha.jpg', open('testhahaha.jpg', 'rb'), 'image/png')),
            ('files', ''),
            ('_save', '')
    ]
)
r3 = s.post(url3, data=body3, headers={"Content-Type": body3.content_type})
print(r3.text)

# if __name__ == '__main__':
#     s = requests.session()
#     login_fuc(s)
#     from connet_mysql import select_sql
#     sql = "select count(*) as sum from djangoweb.hello_teacher where teacher_name = 'testhahaah123235';"
#     result1 = select_sql(sql)[0]['sum']
#     print("查询结果：{}".format(result1))
#     text = add_teacher_name(s)
#     result2 = select_sql(sql)[0]['sum']
#     print("查询结果：{}".format(result2))
#     assert result2 - result1 == 1
    # result = get_add_result(text)
    # assert result == 'testhahaah123234'




# if __name__ =='__main__':
#     s = requests.session()
#     r =get_info(s)
#     print(r)
