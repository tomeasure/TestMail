# version 1.1.0

* 与 version 1.0.0 的不同点
  
  * xml 文件
    > 将原有 host 等标签置于 smtp 标记下
    > 增加了 pop 所需的 host、user、pswd、port

  * configure.py 文件
    > 增加了 pop 所需的 host、user、pswd、port

  * custom_email.py
    > 在类 Email 中使用函数获取 csv 文件作为邮件附件
    > 获取配置信息的方式被创建为一个方法
    > 保存附件的代码段也被创建成为一个方法

> 有一个问题，每次创建 Email 实例，都会创建一次邮件的 message，这样如果仅仅用来接收邮件的话，程序运行起来效率不高。这点在 version 1.2.0 中会得到解决