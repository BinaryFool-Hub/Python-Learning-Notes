import pymysql

# 创建数据库连接
conn = pymysql.connect(
    host="192.168.171.131",  # MySQL服务器主机名
    user="BinaryFool",  # MySQL用户名
    password="123456"  # MySQL密码
)

# 创建游标对象
cursor = conn.cursor()

# 执行SQL查询，列出所有数据库
cursor.execute("SHOW DATABASES")

# 输出结果
for db in cursor.fetchall():
    print(db[0])

# 关闭游标和连接
cursor.close()
conn.close()
