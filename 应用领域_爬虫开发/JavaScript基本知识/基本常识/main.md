# 注意

如果操作不同的数据类型他们会在底层进行隐式转换，不会报错

没特别写的都和python类似

# 注释

```javascript
// 单行注释

/*
* 多行注释
* */

/**
 * 文档注释
 * */
```

# 代码风格

JavaScript的代码风格不固定，如果你习惯写python完全可以类似的写法，但是语句之间的构建可能不一样.

语句结束推荐使用分号，但是不强制要求

你的变量名完全可以按照驼峰或者下划线分割命名，看开发者的喜好

# 输出语句

相当于python的print()函数

```javascript
console.log("hello word");
```

# 定义变量

JavaScript的变量和python一样都可以存储任何类型数据，只是多个关键字声

一般建议：优先用 const，需要变动时用 let，避免使用 var。

| 关键字   | 作用域    | 是否可重复声明	 | 是否可重新赋值	 | 是否提升（hoist）      |
|-------|--------|----------|----------|------------------|
| var   | 函数作用域	 | ✅ 是      | ✅ 是      | ✅ 是（值为undefined） |
| let   | 块级作用域	 | ❌ 否      | ✅ 是      | ✅ 是（但不初始化）       |
| const | 块级作用域	 | ❌ 否      | ❌ 否      | ✅ 是（但不初始化）       |

```javascript
let b = "hello word", l = "你好";

const c = "hello word";

// 不推荐
var a = "hello word";

// 不推荐！！！
/**
 * 变量会自动成为全局变量，即使它在函数内部声明。
 * 容易污染全局作用域，引发命名冲突和难以维护的问题。
 * */
d = "hello word";
```

# 类型

## 所有数据类型

| 类型        | 说明               |
|-----------|------------------|
| string    | 字符串              |
| number    | 数值（包括整数和浮点数）     |
| bigint    | 大整数（如 123n）      |
| boolean   | 布尔值：true / false |
| undefined | 未定义              |
| null      | 空值               |
| symbol    | 唯一值，用于对象属性键      |
| object    | 包括数组、函数、对象等复合结构  |

- string
  ```javascript
  let a = "hello word";
  console.log(a.length);  // 输出长度
  
  // 不同类型拼接会隐式转换，不会报错
  let b = "你好" + 1
  console.log(b)
  ```
- object
  ```javascript
  let b = [1, 2, 3, "nihao"];
  console.log(b.length);  // 输出长度
  ```

## 类型输出

```javascript
// 输出类型，这两种方法都可以
console.log(typeof (a));
console.log(typeof a);  // 只能是后面跟随一个，不能：1+1
```

# 特殊数值

- Infinity
    - 正无穷大(加一个-号就是负无穷)
    - 是一个全局变量，可以直接使用
- NaN
    - Not-a-Number，即“不是一个有效的数值”。
    - 它是 JavaScript 中 number 类型的一个特殊值。
    - NaN 和任何值都不相等，包括它自己
    - 判断是否为 NaN 要用:
      ```javascript
      Number.isNaN(value)   // 推荐
      isNaN(value)          // 会自动类型转换，可能不精确
      ```

# 运算符

## 算数运算

- ++ 运算符
  ```javascript
  let a = 1;
  
  console.log(a++);  // 先返回值后计算
  
  console.log(++a);  // 先计算后返回值
  ```

## 比较运算

- 相等运算符
    - 两个等号只会比较值，不会比较数据类型
       ```javascript
       let a = 1;
       let b = "1";
     
       console.log(a == b)  // true
       ```
    - 三个等号才会比较数据类型和值
      ```javascript
      let a = 1;
      let b = "1";
    
      console.log(a === b)  // false
      ```

## 逻辑运算

| JavaScript | python |
|------------|--------|
| &&         | and    |
| \|\|       | or     |
| !          | not    |
