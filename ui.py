from threading import Thread

from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication

from mpl import *



class food(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init = None
        self.food = QUiLoader().load("UI/food.ui")

        self.food.re.clicked.connect(self.back)
        self.food.rate.clicked.connect(self.rate)
        self.food.four.clicked.connect(self.four)
        self.food.all.clicked.connect(self.all)
        self.food.people.clicked.connect(self.people)



        self.food.show()

    def people(self):
        avgsql = "SELECT AVG(Money) ,Dept  FROM `data`.food  GROUP BY Dept  ;"
        avg(avgsql)
        # thread = Thread(target=avg,
        #                 args=(avgsql,)
        #                 )
        # thread.start()



    def all(self):
        sumsql = "SELECT SUM(Money) ,Dept  FROM `data`.food  GROUP BY Dept  ;"
        Sum(sumsql)


    def four(self):
        daysql = "SELECT SUM(Money)/30 ,Dept  FROM `data`.food  GROUP BY Dept  ;"
        avgday(daysql)


    def rate(self):
        sumsql = "SELECT SUM(Money) ,Dept  FROM `data`.food  GROUP BY Dept  ;"
        rate(sumsql)



    def back(self):
        self.init=init()
        self.food.close()


class init(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.food = None
        self.init = QUiLoader().load("UI/init.ui")

        self.init.exit.clicked.connect(self.exit)
        self.init.food.clicked.connect(self.open_food)

    def open_food(self):
        self.food = food()

    def exit(self):
        self.init.close()


app = QApplication([])
stats = init()
stats.init.show()
app.exec_()
