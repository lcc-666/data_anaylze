import pymysql
import pandas as pd


# 相关性分析
def corr(avg_sql, sum_sql, conn, name):
    # 食堂日平均消费
    avg_money = pd.read_sql(avg_sql, conn)

    # 食堂日总消费
    sum_money = pd.read_sql(sum_sql, conn)

    Analysis = pd.merge(avg_money, sum_money)
    print(name + ":pearson", Analysis["day_money"].corr(Analysis["Money"]))



conn = pymysql.connect(
    host="www.chaogezuishuai.top",
    user="chao", password="CHAOGE",
    database="data",
    charset="gbk")


# for item in ["第一食堂", "第二食堂", "第三食堂", "第四食堂", "第五食堂", "教师食堂"]:
#     avg_sql = """
#     SELECT
#     DAY (`day`) as day,SUM(Money)/COUNT(DISTINCT CardNo) as day_money
#     FROM `data`.people_money pm
#     WHERE Dept LIKE "{}"
#     GROUP BY DAY (`day`);
#     """.format(item)
#     sum_sql = """
#     SELECT
#     DAY (`day`) as day,SUM(Money) as Money
#     FROM `data`.food_money fm
#     WHERE Dept LIKE "{}"
#     GROUP BY DAY (`day`);
#     """.format(item)
#
#     corr(avg_sql, sum_sql, conn, item)
#     conclusion = "通过pearson算法,我们可以得出结论:四月食堂日收入,和学生的消费金额有着明显的正相关关系,相关性最低的第三食堂,其相关系数也达到了0.3以上,最高的第五食堂则接近0.9"
# print(conclusion)