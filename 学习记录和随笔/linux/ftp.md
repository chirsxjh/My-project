# 在LINUX上搭建一个ftp服务器
----
## 步骤
1. 检查安装``vsftpd``服务器
以root进入终端后（其他账户进入终端的可以用su root 输入密码后进入root 模式）之后，在终端命令窗口输入以下命令进行验证：``# rpm –qa | grep vsftpd``。如果结果显示为“vsftpd-1.1.3-8”，则说明系统已经安装vsftpd服务器。若没有回复，即系统中没有安装。  

2. 若没有安装vsftpd，则使用``pip install vsftpd ``进行安装  

3. 创建用户
> 使用vsftpd软件，主要包括如下几个命令：  
启动ftp命令  
service vsftpd start  
停止ftp命令  
service vsftpd stop  
重启ftp命   
service vsftpd restart  

* 先启动ftpd  
![png](https://images2015.cnblogs.com/blog/818082/201607/818082-20160731211306200-28595613.png)  

* 再创建两个用户  
![png](https://images2015.cnblogs.com/blog/818082/201607/818082-20160731211351013-1177136203.png)

4. vsftpd的配置  
ftp的配置文件主要有三个，位于/etc/vsftpd/目录下，分别是  
* ftpusers 该文件用来指定那些用户不能访问ftp服务器。
* user_list 该文件用来指示的默认账户在默认情况下也不能访问ftp
* vsftpd.conf vsftpd的主配置文件
 
5. 以匿名用户登录  
我们去掉配置文件vsftpd.conf 里面以下
```
anon_upload_enable=YES
anon_mkdir_write_enable=YES
```
两项前面的#号，就可以完成匿名用户的配置，此时匿名用户既可以登录上传、下载文件。记得修改配置文件后需要重启服务  

6. 登陆方式
1. 浏览器打开 ： 
浏览器上输入  
ftp://vsftp所在机器ip/  
2. 文件打开 ： 
文件夹输入  
ftp://vsftp所在机器ip/ ；  
 右键可以选择登录



