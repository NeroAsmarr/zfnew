from zfnew import Login

base_url = '学校教务系统的主页url'

lgn = Login(base_url=base_url)
lgn.login('账号', '密码')  # 登陆
print(lgn.cookies)  # cookiejar类的cookies
print(lgn.cookies_str)  # 字符串形式的的cookies
