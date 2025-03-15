"""直接 fake 点下去，看提示你需要什么"""
import faker  # pip install faker

# 使用中文生成假数据
fake = faker.Faker('zh_CN')

# 生成中文姓名
chinese_name = fake.name()
print(f"Chinese Name: {chinese_name}")

# 生成中文地址
chinese_address = fake.address()
print(f"Chinese Address: {chinese_address}")
