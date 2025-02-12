import re

email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
# ^ 以什么开头
# $ 以什么结尾
for email in email_list:
    ret = re.search("^[\w]+@163\.com$", email)
    if ret:
        print("%s 是符合规定的邮件地址，匹配后的结果是:%s" % (email, ret.group()))
    else:
        print("%s 不符合要求" % email)
