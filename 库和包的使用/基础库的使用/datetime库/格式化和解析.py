from datetime import datetime

# 1. 获取当前时间并格式化
now = datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("当前时间:", formatted)

# 3. 解析字符串为日期
date_str = "2023-10-10"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print("解析后的日期:", parsed_date)
