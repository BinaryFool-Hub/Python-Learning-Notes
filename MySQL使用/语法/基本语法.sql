-- 语法规则：命令和函数等语句使用大写，数据库名等非命令和函数语句使用小写

-- 显示数据库
SHOW DATABASES;

-- 创建数据库
-- 方法一，简单创建
CREATE DATABASE databases_name;
-- 方法二，指定字符集，有效的防止数据乱码
CREATE DATABASE databases_name CHARACTER SET 'utf8mb4';
-- 方法三，存在则不创建
CREATE DATABASE IF NOT EXISTS databases_name;

-- 删除数据库
DROP DATABASE databases_name;

-- 查看当前使用的数据库
SELECT DATABASE();

-- 切换数据库
USE databases_name;

-- 显示数据库表
SHOW TABLES;

-- 创建数据库表
-- PRIMARY KEY 表格主键，不能进行重复
-- AUTO_INCREMENT 自增长
CREATE TABLE table_name
(
    id      INT PRIMARY KEY AUTO_INCREMENT,
    name    VARCHAR(20),
    chinese FLOAT,
    math    FLOAT,
    english FLOAT
);

-- 查看表结构
DESC table_name;

-- 查看表数据
-- * 查看所有列
SELECT *
FROM table_name;
-- 指定列
SELECT name, chinese
FROM table_name;
-- 别名显示
SELECT name as 姓名, chinese as 语文
FROM table_name;
-- 去重显示 DISTINCT
SELECT DISTINCT name
FROM table_name;
-- 显示操作后的列
-- CONCAT() 数据拼接
SELECT CONCAT(name, '你好') as name, CONCAT(chinese, '_', '这是非str拼接') as 语文成绩
FROM table_name;
-- 查询指定数据
-- 查询单元格值为 张三 的并且显示为 名字 列，name, chinese, math是含带输出的同行字段值
SELECT '张三' as 名字, name, chinese, math
FROM table_name;
-- 条件查询，AND OR，AND比OR更高级，所以先运行AND
SELECT name, chinese, math, english
FROM table_name
WHERE (english >= 80
    OR english < 100)
  AND name = '张三';
-- 条件查询 IN
SELECT name, chinese, math, english
FROM table_name
WHERE name in ('张三', '李四');
-- 模糊查询
-- %这里面填写值% 值包含在列单元格即满足条件
SELECT *
FROM table_name
WHERE name like '%张%';
-- 排序显示
-- 默认升序，DESC 降序
-- 查询英语80（包含）-190区间的数据，并且由english列的行大小排名
-- 多个条件排序会优先排序左侧的
SELECT *
FROM table_name
WHERE english >= 80
  AND english < 190
ORDER BY english, chinese DESC;
-- 分页查询
-- 取5条数据，从第9行开始，开始行是0行
SELECT *
FROM table_name
LIMIT 9,5;
-- 保留几位小数
-- ROUND()
SELECT name, ROUND(english, 2) as 英语成绩
FROM table_name;
-- 返回当前时间戳
SELECT UNIX_TIMESTAMP(NOW());
-- 返回当前年月日
SELECT DATE_FORMAT(NOW(), '%Y-%m-%d');
-- 类似if else判断操作
-- 判断成绩并且说明，最后END给一个列名
SELECT name,
       chinese,
       english,
       CASE
           WHEN english >= 100 THEN '优秀'
           WHEN english >= 80 THEN '良好'
           ELSE '待努力' END '描述'
FROM table_name;


-- 查看创建表的语句
SHOW CREATE TABLE table_name;

-- 插入数据
-- id 为 0 是自增长，不写也是自增长
INSERT INTO table_name (id, name, chinese, math, english)
VALUES (1, '张三', 60, 70, 80),
       (2, '李四', 60, 70, 80),
       (3, '王五', 60, 70, 80),
       (0, '赵六', 60, 70, 80);
-- 插入指定列数据就写指定列即可，如果有自增长会默认进行自增长，无则为null
INSERT INTO table_name (name, chinese, english)
VALUES ('张李', 60, 180),
       ('李四', 60, 180.11);

-- 表插入新的列
-- 在english列后面插入新的列total，指定FLOATt数据类型
ALTER TABLE table_name
    ADD COLUMN total FLOAT AFTER english;
-- FIRST 插入在第一列
ALTER TABLE table_name
    ADD COLUMN total FLOAT FIRST;
-- 不指定位置默认加在最后面
ALTER TABLE table_name
    ADD COLUMN total FLOAT;

-- 表格删除列
ALTER TABLE table_name
    DROP total;

-- 更改表格列的数据类型
-- 更改为整形
ALTER TABLE table_name
    MODIFY COLUMN total INT;

-- 修改表名
-- 方法一
RENAME TABLE table_name TO table_name1;
-- 方法二
ALTER TABLE table_name RENAME table_name1;

-- 表重置
TRUNCATE table_name;

-- 更改数据库名字
-- 数据库名字不能进行更改操作

-- 修改表指定内容
-- 修改id为1的行total列的值
UPDATE table_name
SET total = 100
WHERE id = 1;

-- 删除表指定数据
-- 删除id为2的行
DELETE
FROM table_name
WHERE id = 2;

