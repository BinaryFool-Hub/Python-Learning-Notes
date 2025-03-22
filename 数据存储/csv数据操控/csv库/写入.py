import csv

"""
encoding='utf-8' 指定编码utf-8，如果写入utf-8编码还是错误就使用utf-8-sig
newline='' 是可以让写入的时候不会空行，如果不加则写入一行数据后面都有一个空行
"""

ll = [[1, 2, 3, 4],
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [5, 6, 7, 8]]

"""普通行数据"""
with open('data.csv', mode='w', encoding='utf-8', newline='') as f:
    csv_obj = csv.writer(f)  # 创建csv对象，方法是写入传入文件操作对象

    # for i in ll:
    #     csv_obj.writerow(i)  # writerow逐行写入数据

    # 写入多行，支持列表和元组
    csv_obj.writerows(ll)

"""字典数据"""
list_dict = [{'first_name': 'Baked', 'last_name': 'Beans'},
             {'first_name': 'Lovely'},
             {'first_name': 'Wonderful', 'last_name': 'Spam'}]

with open('data1.csv', mode='w', encoding='utf-8', newline='') as f:
    # DictWriter  写入字典数据的方法,
    # fieldnames  传入字典的键, 不能多, 不能少, 不能写错, 最大多少就写多少
    csv_obj = csv.DictWriter(f, fieldnames=['first_name', 'last_name'])  # 传入文件对象和表头

    # 字典数据写入对象有专门写表头的方法
    csv_obj.writeheader()

    # for i in list_dict:
    #     csv_obj.writerow(i)  # writerow逐行写入数据

    # 写入多行，支持列表和元组
    csv_obj.writerows(list_dict)
