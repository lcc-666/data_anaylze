import base64

from sql import getsql

import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.serif'] = ['SimHei']

from matplotlib.font_manager import FontProperties

font = FontProperties(fname='simhei.ttf')

from io import BytesIO


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

    plt.figure(figsize=(12,8))

    plt.plot(x, list(y1), label="第一食堂")
    plt.plot(x, list(y2), label="第二食堂")
    plt.plot(x, list(y3), label="第三食堂")
    plt.plot(x, list(y4), label="第四食堂")
    plt.plot(x, list(y5), label="第五食堂")
    plt.plot(x, list(y6), label="教师食堂")

    plt.xlabel("四月食堂消费")
    plt.ylabel("食堂单日消费金额")

    # s="每逢周末以及假期,第二,三,四,五食堂,消费金额明显下滑\n食堂应提前减少菜品储备,降低浪费."
    # plt.annotate(s,(5,2000),(9,800),arrowprops=dict(width=3,headwidth=5,headlength=5),fontsize=20)
    # plt.annotate("", (13, 7000), (11, 3000), arrowprops=dict(width=3, headwidth=5, headlength=5))
    # plt.annotate("", (20, 8000), (14, 3000), arrowprops=dict(width=3, headwidth=5, headlength=5))
    # plt.annotate("", (27, 7000), (17, 3000), arrowprops=dict(width=3, headwidth=5, headlength=5))

    plt.legend()
    #plt.show()

    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())  # 将图片转为base64
    figdata_str = str(figdata_png, "utf-8")  # 提取base64的字符串，不然是b'xxx'

    # 保存为.html
    html = '<img src=\"data:image/png;base64,{}\"/>'.format(figdata_str)
    filename = './html/dayavg.html'
    with open(filename, 'w') as f:
        f.write(html)



# 食堂消费占比
def rate(sql):
    res = getsql(sql)
    money_dict = {}
    for item in res:
        money_dict[item[1]] = float(item[0])
    ex = [0.05 for _ in range(6)]
    plt.pie(money_dict.values(), explode=ex, labels=money_dict.keys(), autopct='%1.1f%%')

    #plt.show()
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())  # 将图片转为base64
    figdata_str = str(figdata_png, "utf-8")  # 提取base64的字符串，不然是b'xxx'

    # 保存为.html
    html = '<img src=\"data:image/png;base64,{}\"/>'.format(figdata_str)
    filename = 'png.html'
    with open(filename, 'w') as f:
        f.write(html)

def sex():
    sql="""
    SELECT *
    FROM `data`.sex_money;
    """
    man=364992
    woman=462509
    ex = [0.05 for _ in range(2)]
    plt.pie(
        [man,woman],
        explode=ex,
        labels=["男","女"],
        autopct='%.2f%%')
    # plt.show()
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())  # 将图片转为base64
    figdata_str = str(figdata_png, "utf-8")  # 提取base64的字符串，不然是b'xxx'

    # 保存为.html
    html = '<img src=\"data:image/png;base64,{}\"/>'.format(figdata_str)
    filename = './html/sex.html'
    with open(filename, 'w') as f:
        f.write(html)

def major():
    sql="""
    SELECT SUM(Money) ,Dept 
    FROM `data`.sex_marjor  sm 
    GROUP BY Major ;
    """
    data={}
    f=open("./major.txt","r",encoding="utf8").readlines()
    for item in f:
        print(item.strip().split("\t"))
        data[item.strip().split("\t")[-1]]=eval(item.strip().split("\t")[0])



if __name__ == '__main__':
    # 人均消费
    # avgsql = "SELECT AVG(Money) ,Dept  FROM `data`.food  GROUP BY Dept  ;"
    # avg(avgsql)
    # 总消费
    # sumsql = "SELECT SUM(Money) ,Dept  FROM `data`.food  GROUP BY Dept  ;"
    # Sum(sumsql)
    # 百分比消费
    # rate(sumsql)
    # 日均消费
    # daysql = "SELECT SUM(Money)/30 ,Dept  FROM `data`.food  GROUP BY Dept  ;"
    # avgday(daysql)
    major()