# 又称无名函数
# 基本架构：lambda arg1,arg2: arg1 + arg2
# lambda是声明匿名函数，:左侧的为需要传入的参数，:右侧为基本的逻辑语句，会返回语句执行的结果

sum = lambda arg1, arg2: arg1 + arg2
print(sum(1, 3))
