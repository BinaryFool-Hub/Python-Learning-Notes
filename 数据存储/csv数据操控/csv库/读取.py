import csv

"""正常读取"""
# with open('data1.csv', mode='r', encoding='utf-8') as f:
#     print(f.read())

# 以下方法都能从csv中读取数据, DictReader读取出来的数据是字典, reader读取出来的数据是列表
# 读取出来的数据和写入时候的对象类型是没有关系

"""读取时返回对象"""
# with open('data1.csv', mode='r', encoding='utf-8') as f:
#     csv_data = csv.reader(f)  # 返回的是一个对象，可以使用list强转数据类型来查看
#     print(list(csv_data))
#     # for data in csv_data:
#     #     print(data) # 得到列表类型数据

"""读取字典形式，会把第一行默认作为字典的 key"""
with open('data1.csv', mode='r', encoding='utf-8') as f:
    csv_data = csv.DictReader(f)  # 返回的是一个对象，可以使用list强转数据来查看
    print(list(csv_data))
    # for data in csv_data:
    #     print(data)  # 字典类型
