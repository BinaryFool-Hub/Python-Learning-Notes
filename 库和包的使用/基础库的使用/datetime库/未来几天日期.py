from datetime import datetime, timedelta

now = datetime.now()

# 计算7天后的日期
future = now + timedelta(days=7)

print("7天后:", future.date())
