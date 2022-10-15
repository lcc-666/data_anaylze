from sql import getsql
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties

FontProperties(fname='simhei.ttf')


# 柱状图模版
def muban(res):
    x_data = []
    y_data = []
    for i in res:
        y_data.append(float(i[0]))
        x_data.append(i[1])

    for i in range(len(x_data)):
        plt.bar(x_data[i], y_data[i])

    for a, b in zip(x_data, y_data):
        plt.text(a, b, str(b), horizontalalignment="center")


# 山西农业大学食堂消费平均值
def avg(sql):
    res = getsql(sql)
    muban(res)

    # 设置图片名称
    plt.title("山西农业大学食堂人均消费")
    # 设置x轴标签名
    plt.xlabel("食堂名称")
    # 设置y轴标签名
    plt.ylabel("消费金额")
    # 显示
    plt.show()


# 山西农业大学食堂总收入
def Sum(sql):
    res = getsql(sql)
    muban(res)

    # 设置图片名称
    plt.title("山西农业大学食堂总消费")
    # 设置x轴标签名
    plt.xlabel("食堂名称")
    # 设置y轴标签名
    plt.ylabel("消费金额")
    # 显示
    plt.show()


# 山西农业大学日收入
def avgday(sql):
    res = getsql(sql)
    avg_dict = {}
    for i in res:
        avg_dict[i[1]] = round(float(i[0]), 2)
    sqls = """
    SELECT SUM(Money) as Money ,Dept,datatime  FROM `data`.sum_people WHERE Dept LIKE '第一食堂' GROUP BY datatime ;
    SELECT SUM(Money) as Money ,Dept,datatime  FROM `data`.sum_people WHERE Dept LIKE '第二食堂' GROUP BY datatime ;
    SELECT SUM(Money) as Money ,Dept,datatime  FROM `data`.sum_people WHERE Dept LIKE '第三食堂' GROUP BY datatime ;
    SELECT SUM(Money) as Money ,Dept,datatime  FROM `data`.sum_people WHERE Dept LIKE '第四食堂' GROUP BY datatime ;
    SELECT SUM(Money) as Money ,Dept,datatime  FROM `data`.sum_people WHERE Dept LIKE '第五食堂' GROUP BY datatime ;
    SELECT SUM(Money) as Money ,Dept,datatime  FROM `data`.sum_people WHERE Dept LIKE '教师食堂' GROUP BY datatime ;
    """

    sql_ls = []
    for i in sqls.split("\n"):
        sql_ls.append(i)
    sql_ls.pop(0)
    sql_ls.pop()
    res = getsql(sql_ls)

    name_dict = {"第一食堂": "one", "第二食堂": "two", "第三食堂": "three", "第四食堂": "four", "第五食堂": "five",
                 "教师食堂": "teacher"}
    one = {}
    two = {}
    three = {}
    four = {}
    five = {}
    teacher = {}
    for item in res:
        name = item[0][1]
        ls = eval(name_dict[name])
        for i in item:
            ls[eval(i[-1])] = int(i[0])
        for i in range(1, 31) - ls.keys():
            ls[i] = int(avg_dict[name])

    x = range(1, 31)

    y1 = one.values()
    y2 = two.values()
    y3 = three.values()

    y4 = four.values()
    y5 = five.values()
    y6 = teacher.values()

    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.plot(x, y4)
    plt.plot(x, y5)
    plt.plot(x, y6)

    plt.xlabel("四月食堂消费")
    plt.ylabel("食堂单日消费金额")

    plt.show()


# 食堂消费占比
def rate(sql):
    res = getsql(sql)
    money_dict = {}
    for item in res:
        money_dict[item[1]] = float(item[0])
    ex = [0.05 for _ in range(6)]
    plt.pie(money_dict.values(), explode=ex, labels=money_dict.keys(), autopct='%1.1f%%')

    plt.show()


if __name__ == '__main__':
    # 人均消费
    avgsql = "SELECT AVG(Money) ,Dept  FROM `data`.food  GROUP BY Dept  ;"
    avg(avgsql)
    # 总消费
    # sumsql = "SELECT SUM(Money) ,Dept  FROM `data`.food  GROUP BY Dept  ;"
    # Sum(sumsql)
    # 百分比消费
    #rate(sumsql)
    # 日均消费
    # daysql = "SELECT SUM(Money)/30 ,Dept  FROM `data`.food  GROUP BY Dept  ;"
    # avgday(daysql)
