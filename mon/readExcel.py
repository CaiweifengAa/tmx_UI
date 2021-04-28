# coding:utf-8
import xlrd  # 导入对应的操作表格的模块
import readconfig

class ReadExcel():

    # 一个表格下有可能多个表格（在表格的底部有sheet），sheet是指所有表格，sheet1表示第一个，依次类推
    # 获取use_API接口数据
    def readExcel(self, fileName, SheetName="test_api"):  # 注意S大写
        # xlrd.open_workbook()函数打开文件，文件名若包含中文，会报错找不到这个文件或目录
        data = xlrd.open_workbook(fileName)
        ##通过名称获取路径下的表格名称
        table = data.sheet_by_name(SheetName)

        # 获取总行数、总列数
        nrows = table.nrows  # 获取总行数
        ncols = table.ncols  # 获取总列数

        # 先判断表格中是否有内容
        if nrows > 1:
            # 获取第一列的内容，列表格式:0代表第一行，依次类推
            keys = table.row_values(0)

            # print(keys)

            listApiData = []
            # 获取每一行的内容，列表格式
            for col in range(1, nrows):  # 根据索引从第二行开始取，直到去完所有的行
                values = table.row_values(col)  # 打印每一行的内容
                # print values
                # keys，values这两个列表一一对应来组合转换为字典
                # 先用zip() 函数可以对具有相同数量的元素的序列进行配对，然后根据dict()方法形成字典——单独讲解下zip方法
                api_dict = dict(zip(keys, values))
                # print(api_dict)
                listApiData.append(api_dict)  # 添加到列表中去
            return listApiData  # 返回列表
        else:
            print("表格未填写数据")
            return None

    # 获取TemplateAPI接口数据
    def TemplateAPIExcel(self, fileName, SheetName="TemplateAPI"):  # 注意S大写
        # xlrd.open_workbook()函数打开文件，文件名若包含中文，会报错找不到这个文件或目录
        data = xlrd.open_workbook(fileName)
        ##通过名称获取路径下的表格名称
        table = data.sheet_by_name(SheetName)

        # 获取总行数、总列数
        nrows = table.nrows  # 获取总行数
        ncols = table.ncols  # 获取总列数

        # 先判断表格中是否有内容
        if nrows > 1:
            # 获取第一列的内容，列表格式:0代表第一行，依次类推
            keys = table.row_values(0)

            # print(keys)

            listApiData = []
            # 获取每一行的内容，列表格式
            for col in range(1, nrows):  # 根据索引从第二行开始取，直到去完所有的行
                values = table.row_values(col)  # 打印每一行的内容
                # print values
                # keys，values这两个列表一一对应来组合转换为字典
                # 先用zip() 函数可以对具有相同数量的元素的序列进行配对，然后根据dict()方法形成字典——单独讲解下zip方法
                api_dict = dict(zip(keys, values))
                # print(api_dict)
                listApiData.append(api_dict)  # 添加到列表中去
            return listApiData  # 返回列表
        else:
            print("表格未填写数据")
            return None

    # 获取TemplateAPI接口数据
    def TelemetryAPIExcel(self, fileName, SheetName="TelemetryAPI"):  # 注意S大写
        # xlrd.open_workbook()函数打开文件，文件名若包含中文，会报错找不到这个文件或目录
        data = xlrd.open_workbook(fileName)
        ##通过名称获取路径下的表格名称
        table = data.sheet_by_name(SheetName)

        # 获取总行数、总列数
        nrows = table.nrows  # 获取总行数
        ncols = table.ncols  # 获取总列数

        # 先判断表格中是否有内容
        if nrows > 1:
            # 获取第一列的内容，列表格式:0代表第一行，依次类推
            keys = table.row_values(0)

            # print(keys)

            listApiData = []
            # 获取每一行的内容，列表格式
            for col in range(1, nrows):  # 根据索引从第二行开始取，直到去完所有的行
                values = table.row_values(col)  # 打印每一行的内容
                # print values
                # keys，values这两个列表一一对应来组合转换为字典
                # 先用zip() 函数可以对具有相同数量的元素的序列进行配对，然后根据dict()方法形成字典——单独讲解下zip方法
                api_dict = dict(zip(keys, values))
                # print(api_dict)
                listApiData.append(api_dict)  # 添加到列表中去
            return listApiData  # 返回列表
        else:
            print("表格未填写数据")
            return None

    # 获取TemplateAPI接口数据
    def SummaryapiExcel(self, fileName, SheetName="Summary_api"):  # 注意S大写
        # xlrd.open_workbook()函数打开文件，文件名若包含中文，会报错找不到这个文件或目录
        data = xlrd.open_workbook(fileName)
        ##通过名称获取路径下的表格名称
        table = data.sheet_by_name(SheetName)

        # 获取总行数、总列数
        nrows = table.nrows  # 获取总行数
        ncols = table.ncols  # 获取总列数

        # 先判断表格中是否有内容
        if nrows > 1:
            # 获取第一列的内容，列表格式:0代表第一行，依次类推
            keys = table.row_values(0)

            # print(keys)

            listApiData = []
            # 获取每一行的内容，列表格式
            for col in range(1, nrows):  # 根据索引从第二行开始取，直到去完所有的行
                values = table.row_values(col)  # 打印每一行的内容
                # print values
                # keys，values这两个列表一一对应来组合转换为字典
                # 先用zip() 函数可以对具有相同数量的元素的序列进行配对，然后根据dict()方法形成字典——单独讲解下zip方法
                api_dict = dict(zip(keys, values))
                # print(api_dict)
                listApiData.append(api_dict)  # 添加到列表中去
            return listApiData  # 返回列表
        else:
            print("表格未填写数据")
            return None


if __name__ == '__main__':
    t = ReadExcel()  # 把这个类实例化
    # 打印只是看清有没读取成功，可以不用打印
    # print(t.readExcel("D:\\TMX _API_Test\\jk1\\user_API.xlsx", "Sheet1"))
    print(t.readExcel(readconfig.data_path, "test_api"))  # fileName, SheetName="Sheet1"
    # print(dict(t.readExcel(readconfig.data_path, "test_api")))
    # print(t.TemplateAPIExcel(readconfig.data_path, "TemplateAPI"))
    # print(t.TemplateAPIExcel(readconfig.data_path, "TelemetryAPI"))
    # print(t.TemplateAPIExcel(readconfig.data_path, "Summary_api"))
# 类是你定义的这个新类型，这个类型可以有很多个实例。
# 比如  a = A()，A是个类，a就是A的一个实例，同样可以b=A()，b也是A的一个实例。
# 初始化函数__init__在实例刚创建完成的时候调用，这里可以对这个实例的属性进行初始化
# class A:
#     def __init__(self,num):
#         self.data = num
# a = A(1)
# b = A(2
