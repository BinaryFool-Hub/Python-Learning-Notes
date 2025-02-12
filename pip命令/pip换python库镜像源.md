

# 国内镜像源:
```
https://pypi.douban.com/simple/ 豆瓣
https://mirrors.aliyun.com/pypi/simple/ 阿里
https://pypi.hustunique.com/simple/ 华中理工大学
https://pypi.sdutlinux.org/simple/ 山东理工大学
https://pypi.mirrors.ustc.edu.cn/simple/ 中国科学技术大学
https://pypi.tuna.tsinghua.edu.cn/simple 清华
```
# 通过镜像源安装库

```
pip install 库名 -i 镜像地址
```

# 把镜像源设置默认
```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
# 查看镜像源
```
pip config list
```

# 更新pip
```
python -m pip install --index-url https://pypi.douban.com/simple --upgrade pip
```

