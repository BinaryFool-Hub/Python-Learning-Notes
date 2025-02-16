# 下载安装

## 官网

> https://www.mysql.com/

## 第一步

![](images/image-20250206115748352.png)

## 第二步

![](images/PixPin_2025-02-06_12-03-13.png)

## 第三步

![](images/PixPin_2025-02-06_12-06-39.png)

## 第四步

![](images/PixPin_2025-02-06_12-07-51.png)

## 第五步

**会进行下载mis安装文件**

![](images/PixPin_2025-02-06_12-08-45.png)

## 第六步

**找到安装文件进行安装**

![](images/PixPin_2025-02-06_12-11-26.png)

## 第七步

**根据自己的情况进行安装**

![](images/PixPin_2025-02-06_12-14-06.png)

## 第八步

**选择好版本后一直点击execute/next，其余默认即可**

**这一步会执行安装和初始化，需要等待一会儿**

![](images/PixPin_2025-02-06_12-16-12.png)

## 第九步

**进行设置你的密码，其余的一直下一步即可**

![](images/PixPin_2025-02-06_12-21-51.png)

## 第十步

**输入你的密码后点击check验证一下即可下一步**

**在最后有一个会默认启动shell，和可视化控制台，不需要就关闭即可**

![](images/PixPin_2025-02-06_12-25-32.png)

## 总结

**你的默认用户名是root**
**你的密码是你设置的密码**

# 添加环境变量

## 1. window11/window10直接搜索环境变量打开

![](images/PixPin_2025-02-06_12-38-38.png)

## 2. 点击环境变量

![](images/PixPin_2025-02-06_12-41-34.png)

## 3.点击path再点击编辑

![](images/PixPin_2025-02-06_12-42-45.png)

## 4.点击右侧的新建

![](images/PixPin_2025-02-06_12-43-39.png)

## 5. 粘贴MySQL的bin路径

> (默认在c盘，要粘贴上级带server的)`C:\Program Files\MySQL\MySQL Server 8.0\bin`

**然后点击确定关闭其余的即可**

## 6.测试环境变量是否可用

**win+r输入cmd**

> 1. 在cmd命令框输入 `mysql -h 127.0.0.1 -u root -p` 即可启动MySQL
> 2. 再输入你的密码即可进入MySQL
