class A(object):
    # 声明静态方法
    @staticmethod
    def fun(arg1, arg2, arg3):
        print(arg1, arg2, arg3)


# 实现实例化使用该方法
A().fun(1, 1, 1)

# 也可以不实例化使用该方法
A.fun(1, 1, 1)
