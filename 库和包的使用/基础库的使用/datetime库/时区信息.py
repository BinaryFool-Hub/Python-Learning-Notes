from datetime import datetime, timezone

utc_time = datetime.now(timezone.utc)  # 带时区的UTC时间
print(utc_time)
