# 基于jQuery框架的Ajax请求

# json数据请求

```javascript
$.ajax({
    url: '/api/data',
    type: 'GET',  // 或 'POST'
    data: JSON.stringify({  // 序列化json数据，方便数据类型传递
        id: 1,  // 可选：发送的数据
    }),
    async: true,  // 是否异步请求，默认就是true，可以选择不写
    dataType: 'json',  // 返回类型（json/text/html）
    contentType: "application/json",  // 设置请求类型用
    success: function (res) {  // 成功执行的代码
        console.log('成功：', res);
    },
    error: function (err) {  // 失败执行的代码
        console.error('失败：', err);
    }
});
```

# 文件数据请求

```javascript
const form = document.getElementById("myForm");
const formData = new FormData(form); // 自动包含所有表单字段

// 输出查看键值对数据（调试的时候可以使用）
// for (const [key, value] of formData.entries()) {
//     console.log(key, ": ", value);
// }

// 可继续追加额外数据
formData.append("age", "20");

// 发送 AJAX 请求
$.ajax({
    url: "/upload", // 后端接口地址
    type: "POST",
    data: formData,
    contentType: false, // 必须设置为 false，让浏览器自动设置 Content-Type
    processData: false, // 必须设置为 false，防止 jQuery 自动转换数据
    success: function (response) {
        console.log("上传成功", response);
    },
    error: function (err) {
        console.log("上传失败", err);
    }
});
```