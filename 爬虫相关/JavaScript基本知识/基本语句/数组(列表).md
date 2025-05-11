# 查找数据

## forEach取值

```javascript
let array = [1, 2, 34, 4, 4, 4];

// 使用forEach结合箭头函数来实现取值操作
array.forEach((value, index, array) => {
    // 参数二三是可选的，不强求使用
    // value：当前元素
    // index：当前索引
    // array：原数组
    console.log(value);
});
```

## for循环取值

```javascript
let array = [1, 2, 34, 4, 4, 4];

for (let i = 0; i < array.length; i++) {
    console.log(array[i])
}
```

# 添加数据

## 末尾添加

```javascript
// 末尾添加
array.push('4'); // 返回值是新长度
```

## 开头添加

```javascript
// 开头添加
array.unshift('4'); // 返回值是新长度
```

## 任意位置插入

```javascript
/**
 * 参数一，start：开始修改数组的位置（索引）
 * 参数二，deleteCount：要删除的元素个数（如果为 0，则不删除）
 * 不定长参数，item1, item2, ...：要插入的元素（可选）
 * */
array.splice(2, 0, "a"); // 在索引 2 处插入 "a"，0表示删除0个元素
```

# 删除数据

## 末尾删除

```javascript
let last = array.pop(); // 返回删除的元素
```

## 开头删除

```javascript
let first = array.shift(); // 返回删除的元素
```

## 任意位置删除

```javascript
array.splice(1, 1); // 从索引 1 开始删除 1 个元素
```

# 查找数据

```javascript
console.log(array.indexOf(3)); // （返回索引）
console.log(array.indexOf(99)); // -1（未找到）
console.log(array.includes(3)); // true（是否存在）
```

