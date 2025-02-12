USE databases_name;

CREATE TABLE IF NOT EXISTS table_name
(
    id      INT PRIMARY KEY AUTO_INCREMENT,
    name    VARCHAR(20),
    chinese FLOAT,
    math    FLOAT,
    english FLOAT
);

INSERT INTO table_name (id, name, chinese, math, english)
VALUES (0, '张三', 60, 70.1, 80.1111),
       (0, '李四', 60, 70.2, 80.124343),
       (0, '王五', 60, 70.5, 80.45435),
       (0, '张张1', 60, 70.5, 80.45435),
       (0, '张张2', 60, 70.5, 20),
       (0, '张张3', 60, 70.5, 30),
       (0, '张张4', 60, 70.5, 50),
       (0, '张张5', 60, 70.5, 90),
       (0, '张张6', 60, 70.5, 190),
       (0, '张张6', 60, 70.5, 190),
       (0, '张张6', 60, 70.5, 190),
       (0, '张张6', 60, 70.5, 190),
       (0, '张张7', 60, 70.5, 180),
       (0, '张张8', 60, 70.5, 170),
       (0, '赵六', 60, 70.9, 80.1);