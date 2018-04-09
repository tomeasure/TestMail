# version 1.0
* 功能

  向某个邮箱发送带有附件的邮件

* 特点

  使用xml存储邮箱信息

* 用到的模块

  1. email.mime.text.MIMEText()
  2. email.mime.multipart.MIMEMultipart()
  3. email.header.Header()
  4. smtplib.SMTP()
  5. xml.sax.ContentHandler
  6. xml.sax.parse()

* 发送的步骤

  1. 创建 MIMEMultipart 实例 message
  2. 设置 message 的 from、to、subject
  3. 创建 MIMEText 对象 att
  4. 设置 att：
     > Content-Type 为 application/octet-stream
     >
     > Content-Disposition 为 attachment;filename="parse_xml.py"

  5. 添加att到message
  6. 创建 SMTP 实例 obj
  7. 执行 obj 的函数 connect、starttls、login、sendmail

* 各文件简介

  1. main.py
    > 设置各项参数，创建邮件，发送邮件

  2. parse_xml.py
    > 继承 xml.sax.ContentHandler，创建新类 ConfigureHandler， 用于 sax 的回调函数，同时也用于存储xml中的信息

  3. configure.py
    > 提取xml中的信息，存储在 ConfigureHandler 中。

  4. configure.xml
    > 存储邮箱的设置信息
      - configure
        - mail
          - host
          - user
          - pass
          - port
        - sender
        - receiver
        - message
          - from
          - to
          - subject
