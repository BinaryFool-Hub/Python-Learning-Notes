# 自定义函数和python区别

## 支持默认参数值

- JavaScript形参默认值可以随意放置，但建议放在后面
     ```javascript
     function fun1(a = 2, b, c, d = 1) {
        console.log(a, b, c, d)
     }
     ```

- python形参默认值需要放在未有默认参数的后面
   ```python
   def fun(a, b, c=2):
       print(a, b, c)
   ```

## 参数传递

- JavaScript传递参数只能是位置传递，如果有默认值会覆盖掉，建议默认值放在后面就可以不传入
    ```javascript
    function fun1(a = 2, b, c, d = 1) {
        console.log(a, b, c, d)
    }
    
    fun1(1, 2, 3);  // 忽略了d默认值的传递，就不会覆盖它
    ```

- python可以以是关键字传递也可以是位置传递
    ```python
    def fun(a, b, c=2):
      print(a, b, c)
  
    fun(1, 2, 3)  # 位置传递
    fun(b=2, a=3)  # 关键字传递
    ```

## 不定长参数使用

- JavaScript只能支持一种方式，但是类型不限制
- `...args`形参，获取到的是列表
     ```javascript
     function fun1(a, b, ...args) {
        // args 传递过来的是不定长列表
        console.log(a, b, args);
    }
    
    fun1(1, 2, 24343, 34, 34, 34, 343, 4)
     ```

- python支持两种方式
     ```python
     def fun(*args, **kwargs):
       print(args, kwargs)
    
     # 如果返回args是元组，kwargs是字典
     fun(1, 2, 3, a=2, b=3)  # 使用关键字传参会被处理未一个字典形式，但是需要先传args，然后再传入kwargs
     ```

# 匿名函数

匿名函数很明显就是没有自己名字的函数

```javascript
// fun 是这个函数的别名，不是它自己的名字，结合语境可以不需要别名，直接使用即可
// 需要 return 来获取值，不然没意义
let fun = function () {
    return "返回值";
}

console.log(fun());
```

# 自调用函数

不需要函数名字的自调用方法，它会自己调用自己执行，然后如果有返回值可以用变量来接收一下

```javascript
let value = (function (str1) {
    console.log("我自己会被自己调用执行");
    return 'hello ' + str1;
})('小明');


console.log(value)
```

**如果去掉后面的`("小明")`就表示暂未调用，可以使用别名(接收的变量名)来调用**

```javascript
let value = (function (str1) {
    console.log("我自己会被自己调用执行");
    return 'hello ' + str1;
});

console.log(value('小明'))
```