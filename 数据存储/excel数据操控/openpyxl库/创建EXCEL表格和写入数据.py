import openpyxl

workbook = openpyxl.Workbook()  # 创建对象
sheet = workbook.active  # 选中活动工作表

# 写入单个单元格
sheet['A1'] = 'Hello, World!'

# 通过行列索引写入数据
sheet.cell(row=2, column=1, value='Python OpenPyXL')

# 写入一行或一列数据，接受列表和元组
data = ['Name', 'Age', 'City']
sheet.append(data)  # 在最后一行追加数据

workbook.save('测试.xlsx')
