# version 1.2.0

* 与 version 1.1.0 的不同点
  
  提高了程序的模块化

  将原来的 Email 类拆分为 SendMail 与 RecvMail 两个类，这两个类在 Email 中分别被 sendMail、recvMail 两个函数实例化并使用。

  main.py 用来执行发送或接收的程序

* 文件结构：
  - 主目录
    - main.py
    - config
      - configure.xml
    - tool
      - custom_email.py
      - configure.py
      - action
        - recv_mail.py
        - send_mail.py