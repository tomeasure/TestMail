# version 1.0.0

* 与 version 0.1.0 的不同点
  * 解析 xml 文件
    > 采用 ElementTree 解析xml文件，删除了 parse_xml.py 模块。

  * xml 文件
    > 删除了 Subject 项

  * main.py
    > 将发送邮件的代码封装成一个函数，创建了一个类，将该函数封装进该类中，在该类中添加了接收邮件的新函数。

  * 1.txt 与 2.txt 是两个用于测试发送邮件程序

* 程序里 poplib 的使用
  > 连接服务器，并创建 POP3 的实例：
  > ` p = poplib.POP3(host, port) `
  > 登陆服务器：
  > ```
  >   p.user(user)
  >   p.pass_(pswd)
  > ```
  > 获取收件箱的邮件列表，并获得最近的邮件：
  > ```
  > p.list()
  > p.retr(email_index)
  > ```
  > 利用 `p.walk()` 以及 `get_filename()` 获取附件名称，用 `get_payload` 获取附件数据，最后根据名称，将数据保存即可
