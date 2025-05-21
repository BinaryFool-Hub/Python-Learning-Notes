async function addUser() {
    // 获取数据
    const info = document.getElementById('info').value;
    if (!info) {
        alert('无数据，不插入');
        return;
    }

    // 执行python的类函数拿到返回结果
    const users = await window.pywebview.api.add_user(info);

    // 获取展示结果元素
    const ul = document.getElementById('result');
    ul.innerHTML = '';  // 清空里面的HTML内容

    // 展示python类函数执行的结果
    for (const user of users) {
        const li = document.createElement('li');  // 创建li元素
        li.textContent = user;  // 写入内容
        ul.appendChild(li);  // 插入数到ul结果框
    }
}

const submit = document.getElementById('submit');
submit.addEventListener('click', addUser);
