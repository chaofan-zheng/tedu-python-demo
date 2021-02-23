## **远程连接Redis配置流程**

- **配置流程**

  ```
  【1】修改配置文件
      sudo gedit /etc/redis/redis.conf
      修改如下2个内容后保存退出:
         # bind 127.0.0.1 ::1  把此行注释掉
         protected-mode no     把默认的yes改为no
         
  【2】重启redis服务
      sudo /etc/init.d/redis-server restart
      
  【3】远程连接测试(在远程机器上)
      redis-cli -h IP地址
  ```

## **远程连接MySQL配置流程**

- **配置流程**

  ```
  【1】修改配置文件,允许远程连接
      sudo gedit /etc/mysql/mysql.conf.d/mysqld.cnf
      将如下行注释并保存退出:
       # bind-address = 127.0.0.1
       
  【2】给用户授权
      mysql -uroot -p123456
      mysql> grant all privileges on *.* to 'root'@'%' identified by '123456' with grant option;
      mysql> flush privileges;
      
  【3】重启MySQL服务
      sudo /etc/init.d/mysql restart
      
  【4】远程连接测试(远程服务器上)
      mysql -hIP地址 -uroot -p123456
  ```

  