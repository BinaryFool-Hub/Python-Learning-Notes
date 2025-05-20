"""决定使用json还是data就要查看它的请求头，如果是`Content-Type: application/json`则使用json"""

"""json 参数
发送 JSON 格式 的数据（自动序列化字典为 JSON 字符串）。

适用于 REST API 请求，后端通常用 application/json 接收。

特点
requests 会自动：
    将 Python 字典（dict）转换成 JSON 字符串。
    设置请求头 Content-Type: application/json。

适用于大多数现代 API（如 FastAPI、Django REST Framework、Flask 等）。
"""

"""data 参数
发送 表单数据（x-www-form-urlencoded）或 纯文本数据。

适用于传统的 HTML 表单提交（如登录、文件上传等）。

特点
    默认 Content-Type: application/x-www-form-urlencoded。
    如果传入字典，requests 会将其编码为 key=value&key2=value2 格式。
    如果传入字符串，则直接作为请求体发送（需手动设置 Content-Type）。
"""
