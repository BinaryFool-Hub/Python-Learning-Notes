# 进入MySQL shell

```shell
mysql -h 127.0.0.1 -u root -p
```

- win + r 进行输入`cmd`然后再输入即可进入，需要你的`root`用户密码

# 创建用户

```mysql
CREATE USER '用户名'@'%' IDENTIFIED BY '密码';
```

- 将 `用户名` 替换为你想要创建的用户名。
- 将 `密码` 替换为你想要设置的密码。
- `'%'` 表示允许从任意主机连接, 可以替换为`'localhost'`(本地连接)

# 授予权限

```mysql
GRANT ALL PRIVILEGES ON *.* TO '用户名'@'%';
```

- `*.*` 表示授予全部数据库权限和数据库的数据表权限，如果想指定数据库则把`*`替换为对应的数据库即可
- 将 `用户名` 替换为你的实际名称

# 修改权限

```
-- 显示所有数据库
SHOW DATABASES;

-- 使用 mysql 这个数据库
USE mysql;

-- 显示表
show tables;

-- 查询 user 表 的 user, host 这两个表头的信息
select user, host from user;

-- 更新 new_user 用户 的 host 值为 '%'
update user set host='%' where user = 'new_user';
```

# 刷新数据库权限

```mysql
FLUSH PRIVILEGES;
```

