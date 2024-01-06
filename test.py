# import requests
#
#
# def search_oracle_docs(query):
#     url = 'https://docs.oracle.com/search'
#     params = {
#         'q': query
#     }
#
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         return response.text
#     else:
#         return None
#
#
# # 调用函数进行检索
# query = 'compute+instance+deleted'
# result = search_oracle_docs(query)
# print(result)


# import pandas as pd
# import os
#
# # 指定文件路径
# file_path = "D:/Samples/单品电商数据.xlsx"
#
# # 获取Excel文件所在目录的完整路径
# base_dir = os.path.dirname(file_path)
#
# # 用pandas导入Excel文件的数据，引擎为"openpyxl"，导入前6行，前6列数据
# df = pd.read_excel(file_path, engine="openpyxl", nrows=6, ncols=6)
#
# # 将导入的数据保存到该路径下的“单品电商数据2.xlsx”中
# save_file_path = os.path.join(base_dir, "单品电商数据2.xlsx")
# df.to_excel(save_file_path, engine="openpyxl", index=False)

# import pandas as pd
#
# # 指定文件路径
# file_path = "D:/Samples/ch02/01 读取Excel文件数据/单品电商数据.xlsx"
#
# # 用pandas导入Excel文件的数据，引擎为"openpyxl"
# df = pd.read_excel(file_path, engine="openpyxl")
#
# # 输出数据的形状
# print("Data Shape: ", df.shape)
#
# # 输出行数
# print("Number of Rows: ", len(df))
#
# # 输出列数
# print("Number of Columns: ", len(df.columns))


# Import pandas library
# import pandas as pd
#
# # Define the file path
# file_path = "D:/Samples/ch02/01 读取Excel文件数据/单品电商数据.xlsx"
#
# # Import the first worksheet of the Excel file using openpyxl engine
# df = pd.read_excel(file_path, sheet_name=0, nrows=6, usecols='A:F', engine='openpyxl')
#
# # Print the first 5 rows of the DataFrame for verification
# print(df.head())


# import pandas as pd
#
# # Define the file path
# # file_path = 'D:/Samples/产品规格.xlsx'
# file_path = "D:/Samples/ch03/01 列操作/02 已有列简单计算得到新列/产品规格.xlsx"
#
#
# # Import the first worksheet of the Excel file using pandas and openpyxl engine
# df = pd.read_excel(file_path, sheet_name=0, nrows=7, engine='openpyxl')
#
# # Add a new column '体积' by multiplying '长', '宽', and '高' columns
# df['体积'] = df['长'] * df['宽'] * df['高']
#
# # Output the table data
# print(df)

# import pandas as pd
#
# # Define the file path and read the first worksheet
# file_path = 'D:/Samples/ch03/02 行操作/05 更改行数据/考试成绩.xlsx'
# df = pd.read_excel(file_path, sheet_name=0, nrows=12, engine='openpyxl', index_col='姓名')
#
# # Calculate the average score for each subject (column) and display the result as a new row
# average_row = df.mean().round().append(pd.Series('平均成绩', index=df.columns))
# print(df.append(average_row))
# df = pd.read_excel(file_path, sheet_name=0, nrows=12, engine='openpyxl')
#
# # Calculate the average score for each subject (column) and display the result as a new row
# average_row = df.mean().round().append(pd.Series('平均成绩', index=df.columns))
# print(df.append(average_row))

# # 用pandas读取Excel文件指定工作表的前12行数据
# # 设置姓名列为索引列,引擎为openpyxl
# df = pd.read_excel(file_path, sheet_name=0, index_col='姓名', nrows=12, engine='openpyxl')
#
# # 计算每列的平均值并取整数
# averages = df.mean().round().astype(int)
#
# # 在原表下面添加一行,索引为'平均成绩',值为平均成绩
# df.loc['平均成绩'] = averages
#
# # 输出修改后的表数据
# print(df)

# # 打开Excel文件，导入数据
# df = pd.read_excel(file_path, engine='openpyxl')
#
# # 将“姓名”列作为索引列
# df.set_index('姓名', inplace=True)
#
# # 计算每列数据的均值，结果取整数
# average = df.iloc[:, 1:].mean().round()
#
# # 将导入的数据和均值输出在同一行下面
# print(df)

# import pandas as pd
#
# # Define the file path and read the first worksheet
# file_path = 'D:/Samples/各部门人员工资.xlsx'
# df = pd.read_excel(file_path, sheet_name=0, nrows=12, engine='openpyxl')
#
# # Insert a new column named "交通补贴" with all values set to 600 before the 4th column
# df.insert(3, '交通补贴', 600)
#
# # Calculate the total salary by adding 600 to the existing total salary column
# df['工资总额'] = df['工资总额'] + 600
#
# # Display the modified DataFrame
# print(df)

# Import required libraries
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Set the display language to Chinese
# plt.rcParams['language'] = 'zh_CN'
#
# # Load the data from the Excel file using Pandas
# df = pd.read_excel('E:\\00_books\\智能分析\\Samples\\提示词模板-代码\\127 饼图(Matplotlib)\\访客年龄.xlsx', index_col=0, header=0, engine='openpyxl')
#
# # Generate a pie chart using Matplotlib
# plt.pie(df['占比'], labels=df.index, autopct='%1.1f%%')
#
# # Set the title of the plot
# plt.title('访客年龄占比', fontsize=16)
#
# # Show the plot
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
#
# df = pd.read_excel(r'E:\\00_books\\智能分析\\Samples\\提示词模板-代码\\127 饼图(Matplotlib)\\访客年龄.xlsx', header=0, index_col=False, engine='openpyxl')
# # 选择列 A和B
# data = df[['访客年龄', '占比']]
#
# # 按 '访客年龄' 列数据进行分组计算,得到总占比
# data['总占比'] = data.groupby('访客年龄')['占比'].sum()
#
# # 计算每个年龄组的分数
# data['分数'] = data['占比'] / data['总占比']
# data.drop('总占比', axis=1, inplace=True)
# fig, ax = plt.subplots()
# def fmt_percent(x, pos):
#     return f"{int(x*100):0.0f}%"
#
# # 设置坐标轴格式
# ax.yaxis.set_major_formatter(ticker.FuncFormatter(fmt_percent))
#
# # 绘制饼图
# ax.pie(data['分数'].values, labels=data['访客年龄'].values, startangle=90, autopct='%1.1f%%', textprops={'fontsize': 9})
#
# # 画轴标题
# ax.set_title('访客年龄分布', fontsize=12)
#
# # 设置图标大小
# plt.rcParams['figure.figsize'] = [8, 6]
#
# plt.show()

# 导入pandas库
# import pandas as pd
# import matplotlib as plt
#
# # 设置Excel文件路径
# file_path = "E:\\00_books\\智能分析\\Samples\\提示词模板-代码\\127 饼图(Matplotlib)\\访客年龄.xlsx"
#
# # 使用pandas读取Excel文件数据，index_col设置第1列为索引列，engine设置引擎为"openpyxl"
# df = pd.read_excel(file_path, index_col=0, engine="openpyxl")
#
# # 获取数据
# age = df["访客年龄"]
# percentage = df["占比"]
#
# # 创建饼图
# plt.pie(percentage, labels=age, autopct="%.2f%%", textprops={"fontsize": 10})
#
# # 设置中文
# plt.rcParams["font.sans-serif"] = ["SimHei"]
#
# # 显示饼图
# plt.show()

# 导入所需模块
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 设置Excel文件路径
# file_path = 'E:\\00_books\\智能分析\\Samples\\提示词模板-代码\\127 饼图(Matplotlib)\\访客年龄.xlsx'
#
# # 用pandas导入Excel数据
# # 索引行为第1行,索引列为第1列
# # 引擎为openpyxl
# df = pd.read_excel(file_path, index_col=0, header=0, engine='openpyxl')
#
# # 生成饼图
# plt.pie(x=df['占比'], # 数据
#         labels=df.index, # 标签
#         autopct='%.1f%%') # 设置百分比的格式
#
# # 设置标题
# plt.title('访客年龄占比')
#
# # 支持中文
# plt.rcParams['font.sans-serif'] = 'SimHei'
#
# # 显示图形
# plt.show()

# # 导入所需的库
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 设置matplotlib支持中文
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# plt.rcParams['axes.unicode_minus'] = False
#
# file_path = 'E:\\00_books\\智能分析\\Samples\\提示词模板-代码\\127 饼图(Matplotlib)\\访客年龄.xlsx'
# # 使用pandas读取Excel文件，第1行为索引行，第1列为索引列，引擎为"openpyxl"
# df = pd.read_excel(file_path, index_col=0, engine='openpyxl')
#
# # 使用pandas的plot直接生成饼图
# df.plot(kind='pie', subplots=True, figsize=(6, 6), legend=False, autopct='%1.1f%%')
#
# # 显示图形
# plt.show()
#
# # 假设您希望显示的标签为"年龄分布"
# # df.plot(kind='pie', subplots=True, figsize=(6, 6), legend=False, autopct='%1.1f%%', labels=['年龄分布'])


# 首先导入pandas库
# import pandas as pd
#
# # 定义Excel文件的路径
# file_path = 'E:\\00_books\\智能分析\\Samples\\提示词模板-代码\\01 读取全部Excel文件数据\\单品电商数据.xlsx'
#
# # 使用pandas的read_excel函数导入Excel数据，并指定引擎为"openpyxl"
# # 注意：需要先安装openpyxl库，在终端或命令行中输入pip install openpyxl即可
# data = pd.read_excel(file_path, engine='openpyxl')
#
# # 输出数据的形状（行数x列数）
# print("数据形状:", data.shape)
#
# # 输出行数
# print("行数:", data.shape[0])
#
# # 输出列数
# print("列数:", data.shape[1])

# # 首先，我们需要引入pandas库
# import pandas as pd
#
# # 定义Excel文件的路径
# file_path = 'E:\\00_books\\智能分析\\Samples\\提示词模板-代码\\02 读取部分Excel文件数据\\单品电商数据.xlsx'
#
# # print(eval("lambda x: x[0:5]"))
#
# # 使用pandas读取Excel文件，并将前6行和前6列的数据导入到一个名为df的数据帧中。
# # 我们使用了openpyxl作为引擎，因为它支持新版的Excel文件格式。
# # df = pd.read_excel(file_path, engine='openpyxl', header=None, usecols=lambda x: x[0:5], nrows=6)
# df = pd.read_excel(file_path, engine='openpyxl', header=None, usecols=lambda x: x[0,5], nrows=6)
#
# # 输出数据
# print(df)

# # 首先，我们需要引入pandas库
# import pandas as pd
#
# # 定义Excel文件的路径
# file_path = 'E:\\00_books\\智能分析\\Samples\\提示词模板-代码\\02 读取部分Excel文件数据\\单品电商数据.xlsx'
#
# # 使用pandas读取Excel文件，并将前6行和前6列的数据导入到一个名为df的数据帧中。
# # 我们使用了openpyxl作为引擎，因为它支持新版的Excel文件格式。
# # 这里，我们没有使用lambda函数，而是直接使用usecols参数提取前6列的数据。
# df = pd.read_excel(file_path, engine='openpyxl', header=None, usecols="A:F", nrows=6)
#
# # 输出数据
# print(df)

# 引入pandas库
import pandas as pd

# 定义Excel文件的路径
file_path = 'E:\\00_books\\智能分析\\Samples\\提示词模板-代码\\11 已有列简单计算得到新列/产品规格.xlsx'

# 使用pandas的read_excel函数导入Excel数据，只导入前7行数据，引擎为'openpyxl'
df = pd.read_excel(file_path, nrows=7, engine='openpyxl')

# 在df的'长'、'宽'和'高'列的值上进行乘法操作，得到'体积'，并将其存储在新的'体积'列中
df['体积'] = df['长'] * df['宽'] * df['高']

# 打印修改后的df
print(df)